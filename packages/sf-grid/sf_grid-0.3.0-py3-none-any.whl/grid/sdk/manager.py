import os
import json
import sys
import jwt
import asyncio
import httpx
from typing import Dict, List, Optional
from tabulate import tabulate


class GRIDSessionManager:
    def __init__(self) -> None:
        resource_config = self.load_resource_config()

        if 'tokens' not in resource_config:
            raise ValueError("The resource config file must contain 'tokens'.")

        self.resource_data = resource_config

        if 'resources' in resource_config:
            self.node_data = self.resource_data["resources"]
        else:
            self.node_data = {}
            print("No machine config specified in resource configuration. GRID will use localhost by default.")

        self.user_id = resource_config["tokens"]["username"]
        self.platform_auth_token = self.generate_jwt_token()
        self.session_nodes = {}

    def load_resource_config(self):
        resource_config_path = os.path.expanduser('~') + '/.grid/resource_config.json'
        if not os.path.exists(resource_config_path):
            os.makedirs(os.path.dirname(resource_config_path), exist_ok=True)
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")
            storage_token = input("Enter your storage token: ")
            with open(resource_config_path, 'w') as f:
                json.dump({"tokens": {"username": user_name, "password": password, "storage_token": storage_token}, "resources": {"local": {"ip": "localhost"}}}, f)
                print("Resource configuration file created successfully.")

        print(f"Loading resource configuration from {resource_config_path}...")

        with open(resource_config_path) as f:
            resource_config = json.load(f)

        return resource_config

    def generate_jwt_token(self) -> str:
        secret_key = "rainbowboymonkeysyndromemyelectronicstoremyelectronicstorelastchancetoevacuateplanetearthbeforeitisrecycled"
        payload = {"user_id": self.user_id, "session_id": "test_session"}  # Adjust payload as needed
        return jwt.encode(payload, secret_key, algorithm="HS512")

    def create_config(self, session_config_file_path: str, session_id: str) -> Dict:
        session_config_file_path = os.path.abspath(os.path.expanduser(session_config_file_path))
        with open(session_config_file_path, 'r') as config_file:
            config_data = json.load(config_file)

        # Check if the required keys exist in the config_data
        if 'airgen' not in config_data or 'grid' not in config_data:
            raise ValueError("The session config file must contain 'airgen' and 'grid' configuration.")

        token_data = {
                "openai_api_key": "openaikeygoeshere",
                "airgen_blob_account_name": "gridportalresources",
                "airgen_blob_container_id": "airgenbins"
            }

        token_data["airgen_blob_container_sas_token"] = self.resource_data["tokens"]["storage_token"]

        config_dict = {
            "tokens": token_data,
            "user": {"user_id": self.user_id},
            "session": {
                "session_id": session_id,
                "airgen": config_data["airgen"],
                "grid": config_data["grid"],
            },
        }
        return config_dict

    def get_ip_for_resource(self, resource_name: str) -> Optional[str]:
        return self.resource_data["resources"].get(resource_name)["ip"]

    async def start_session(self, session_id: str, session_config_file_path: str, node_ip: str) -> Optional[bool]:
        """
        Start a session on the specified node.

        Args:
            session_id (str): The ID of the session to start.
            session_config_file_path (str): The path to the session configuration file.
            node_ip (str): The IP address of the node.

        Returns:
            Optional[bool]: True if the session started successfully, False otherwise.
        """

        print(f"Starting session {session_id} ...")
        config = self.create_config(session_config_file_path, session_id)

        async with httpx.AsyncClient(
            base_url=f"http://{node_ip}:8000", timeout=600
        ) as client:
            try:
                response = await client.post(
                    "/start_session",
                    json={"session_config": config},
                    headers={"Authorization": f"Bearer {self.platform_auth_token}"},
                )
                async for line in response.aiter_lines():
                    if line:
                        data = json.loads(line)
                        print(f"{data['msg_type']}: {data['msg_content']}")
                        sys.stdout.flush()  # Ensure the output is flushed immediately
                        if data["msg_type"] == "response_end":
                            if data["success"]:
                                print("Session started successfully.")
                                self.session_nodes[session_id] = node_ip  # Store the mapping
                            else:
                                print("Failed to start session.")
                            return data["success"]
            except httpx.RequestError as e:
                print(f"Request error: {e}")
                sys.stdout.flush()  # Ensure the output is flushed immediately
                return None

    async def stop_session(self, session_id: str) -> bool:
        print(f"Stopping session {session_id} ...")

        node_ip = self.session_nodes.get(session_id)
        if not node_ip:
            print(f"No node found for session {session_id}")
            return False

        async with httpx.AsyncClient(
            base_url=f"http://{node_ip}:8000", timeout=600
        ) as client:
            try:
                response = await client.post(
                    "/terminate_session",
                    json={"session_id": session_id, "user_id": self.user_id},
                    headers={"Authorization": f"Bearer {self.platform_auth_token}"},
                )
                response_data = response.json()
                if response_data.get("success"):
                    print("Session stopped successfully.")
                    del self.session_nodes[session_id]  # Remove the mapping
                else:
                    print("Failed to stop session.")
                    print("Response:", response_data)
                return response_data.get("success", False)
            except httpx.RequestError as e:
                print(f"Request error: {e}")
                return False

    async def list_sessions(self) -> List[Dict]:
        if not self.session_nodes:
            print("No active sessions found.")
            return []

        async def get_session_info(session_id: str, node_ip: str) -> Dict:
            async with httpx.AsyncClient(
                base_url=f"http://{node_ip}:8000", timeout=600
            ) as client:
                try:
                    response = await client.get(
                        "/is_idle",
                        params={"session_id": session_id},
                        headers={"Authorization": f"Bearer {self.platform_auth_token}"},
                    )
                    data = response.json()
                    return {
                        "session_id": session_id,
                        "node_ip": node_ip,
                        "is_idle": data.get("is_idle", "N/A"),
                        "last_active_time": data.get("last_active_time", "N/A"),
                    }
                except httpx.RequestError as e:
                    print(f"Request error while fetching session info for {session_id}: {e}")
                    return {
                        "session_id": session_id,
                        "node_ip": node_ip,
                        "is_idle": "Error",
                        "last_active_time": "Error",
                    }

        tasks = [get_session_info(session_id, node_ip) for session_id, node_ip in self.session_nodes.items()]
        session_info_list = await asyncio.gather(*tasks)

        if session_info_list:
            headers = ["Session ID", "Node IP", "Last Active Time"]
            table_data = [
                [info["session_id"], info["node_ip"], info["last_active_time"]]
                for info in session_info_list
            ]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No active sessions found.")

        return session_info_list

    def list_nodes(self):
        if not self.node_data:
            print("No nodes found in the configuration.")
            return

        node_list = [{"Node Name": node, "IP Address": details["ip"]} for node, details in self.node_data.items()]
        if node_list:
            print(tabulate(node_list, headers="keys", tablefmt="grid"))
        else:
            print("No nodes found in the configuration.")
