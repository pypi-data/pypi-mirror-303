import asyncio
import os
import subprocess
import webbrowser
import json
import shlex
import logging
from typing import Optional
from cmd import Cmd
from art import tprint
from grid.sdk.manager import GRIDSessionManager
from grid.sdk.commander import Commander

class GRIDRepl(Cmd):
    prompt = 'grid> '
    intro = tprint("\nGRID", "colossal")

    def __init__(self):
        super().__init__()

        print("General Robot Intelligence Development Platform Console \nDeveloped by Scaled Foundations, Inc.\n")
        
        self.session_manager: GRIDSessionManager = GRIDSessionManager()
        self.commander: Commander = Commander()
        self.commander.set_node_data(self.session_manager.resource_data["resources"])

        self.loop = asyncio.get_event_loop()
        self._setup_logging()

        self.sample_session_config = {
            "airgen": {
            "env_name": "blocks",
            "geo": False,
            "settings": {
                "SimMode": "Car",
            "Vehicles": {
                "Drone": {
                    "VehicleType": "Chaos",
                    "VehicleModel": "MCR"
                }
                },
                "OriginGeopoint": {
                "Latitude": 47.62094998919241,
                "Longitude": -122.35554810901883,
                "Altitude": 100
                }
            }
            },
            "grid": {
            "entities": {
                "robot": [{"name": "airgen-drone", "kwargs": {}}],
                "model": []
            }
            }
        }

        print("Type 'help' or 'license' for more info.\n")

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def cmdloop(self, intro=None):
        while True:
            try:
                super().cmdloop(intro)
                break
            except Exception as e:
                self.logger.error(f"An error occurred: {str(e)}", exc_info=False)
                intro = ''

    def handle_node_command(self, arg, default_node='local'):
        args = arg.split()
        if len(args) > 1:
            print(f"Invalid command. Use '{arg.split()[0]}' or '{arg.split()[0]} @nodename'.")
            return None
        node_name = default_node
        if arg and arg.startswith('@'):
            node_name = arg[1:]
        return node_name

    def do_exit(self, _):
        """Exit the console."""
        if self.session_manager.session_nodes:
            print("\033[93mWarning: There are active sessions running. Are you sure you want to exit?\033[0m")
            response = input("Enter 'Y' to exit or 'N' to cancel: ")
            if response.lower() == 'y':
                print("Exiting GRID Console...")
                return True
            else:
                print("Exit cancelled.")
                return False
        else:
            print("Exiting GRID Console...")
            return True

    def do_EOF(self, _):
        """Exit the console on EOF (Ctrl+D)"""
        print("\nExiting GRID Console...")
        return True
    
    def do_license(self, _):
        """Display the license terms."""
        print("Opening license page in the browser...")
        url = "https://scaledfoundations.ai/enterprise-license"

        webbrowser.open(url)

    def _connect_to_session_manager(self, resource_config_file_path: str):
        self.session_manager = GRIDSessionManager(resource_config_file_path)

    def do_login(self, arg):
        """Login to the GRID registry using username and password/access token

        login @nodename : Login through the specified node (localhost by default)"""

        node_name = self.handle_node_command(arg)

        username = self.session_manager.resource_data["tokens"]["username"]
        password = self.session_manager.resource_data["tokens"]["password"]
        self.commander.login_registry(node_name, username, password)


    def do_init(self, arg):
        """Spin up the GRID containers.

        init @nodename : Start the containers on specified node (localhost by default)"""

        node_name = self.handle_node_command(arg)
        self.commander.init_containers(node_name)

    def do_terminate(self, arg):
        """Terminate the GRID containers.

        terminate @nodename : Stop the containers on specified node (localhost by default)"""

        node_name = self.handle_node_command(arg)
        self.commander.kill_containers(node_name)

    def do_update(self, arg):
        """Update the GRID containers.

        update @nodename : Update the containers on specified node (localhost by default)"""

        node_name = self.handle_node_command(arg)
        print(f"Checking for updates...")
        self.commander.update_containers(node_name)

    def do_clear(self, _):
        """Clear the terminal output."""
        os.system("clear")

    def do_node(self, arg):
        """Manage nodes:

        node list : List all nodes with their IP addresses"""
        args = arg.split()
        if len(args) < 1:
            print("Invalid node command. Use 'node list'.")
            return

        command = args[0]
        if command == 'list':
            self.session_manager.list_nodes()
        else:
            print("Invalid node command.")

    def do_session(self, arg):
        """Manage sessions:

        session start <session_id> <config_path> @<resource_name>  : Start a session
        session stop <session_id> : Stop the specified session
        session list : List currently active sessions"""
        if self.session_manager is None:
            print("Session manager not initialized. Use 'connect' command first.")
            return

        args = arg.split()
        if len(args) < 1:
            print("Invalid session command. Use 'session start', 'session stop', or 'session list'.")
            return

        node_name = "local"
        for arg in args:
            if arg.startswith('@'):
                node_name = arg[1:]
                break

        command = args[0]
        if command == 'start' and len(args) >= 2:      
            if not self.commander.check_grid_containers(node_name):
                print("\033[93mOne or more GRID containers are not up. Please run `init` before attempting to run session commands.\033[0m")
                return

            session_config_path = None
            if len(args) == 4:
                session_config_path = args[2]
            else:
                session_config_path = "~/.grid/sample_session_config.json"
                print(f"No session configuration was passed. Using a sample configuration from {session_config_path}...")

                if not os.path.exists(os.path.abspath(os.path.expanduser(session_config_path))):
                    with open(os.path.abspath(os.path.expanduser(session_config_path)), 'w') as output_file:
                        json.dump(self.sample_session_config, output_file, indent=4)         
      
            self.loop.run_until_complete(self._start_session(args[1], session_config_path, node_name))
        elif command == 'stop' and len(args) == 2:
            self.loop.run_until_complete(self._stop_session(args[1]))
        elif command == 'list':
            self.loop.run_until_complete(self._list_sessions())
        else:
            print("Invalid session command.")

    def do_open(self, arg):
        """Open an entity (notebook, simulation, or telemetry): open <session_name> <nb | sim | viz>"""
        args = arg.split()
        if len(args) < 2:
            print("Invalid open command. Use 'open nb | sim | viz @node_name'.")
            return
        self._open_entity(args[0], args[1])

    async def _start_session(self, session_id: str, config_path: str, resource: str):
        node_ip = self.session_manager.get_ip_for_resource(resource)
        if not node_ip:
            print(f"Error: Resource '{resource}' not found in the configuration.")
            return None

        await self.session_manager.start_session(session_id, config_path, node_ip)

    async def _stop_session(self, session_id: str):
        await self.session_manager.stop_session(session_id)

    async def _list_sessions(self):
        await self.session_manager.list_sessions()

    def _open_entity(self, entity: str, node_id: str):
        node_name = self.handle_node_command(node_id)
        node_ip = self.session_manager.node_data[node_name]["ip"]
        urls = {
            'sim': f"http://{node_ip}:3080",
            'viz': f"http://{node_ip}:9090/?url=ws://{node_ip}:9877",
            'nb': f"http://{node_ip}:8890"
        }

        url = urls.get(entity)
        if url:
            print(f"Opening {entity} from node {node_name} in default browser at {url}")
            webbrowser.open(url)
        else:
            print(f"Unknown entity: {entity}")

def repl():
    GRIDRepl().cmdloop()

if __name__ == "__main__":
    repl()
