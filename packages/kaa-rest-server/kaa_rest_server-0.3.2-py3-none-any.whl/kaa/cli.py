import os
import time
import sys
import threading
from wsgiref.simple_server import make_server

from . import NAME, VERSION, KaaServer, StartKaaError
from .server import Server
from .kaa_definition import KaaDefinition, DefinitionException


class Cli:
    def __init__(self):
        self.argv = sys.argv[:]
        self.server: KaaServer
        self.wsgi_server = None
        self.__init_configuration()

    def execute(self):
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = "help"

        if subcommand == "version":
            msg = self.__get_version()
        elif subcommand == "help":
            msg = self.__get_help()
        elif subcommand == "serve":
            self.__run_server()
            return
        elif subcommand == "dev":
            path = self.definitions.get_base_path()
            monitor_thread = threading.Thread(
                target=self.__monitor_changes, args=(path,)
            )
            monitor_thread.daemon = True
            monitor_thread.start()
            self.__run_server()
            return
        else:
            msg = "Invalid command. Try help"

        sys.stdout.write(msg + "\n")

    @classmethod
    def __get_name(cls):
        return NAME

    @classmethod
    def __get_version(cls):
        return VERSION

    def __get_help(self):
        commands = [
            ("version", "Returns Kaa version"),
            ("serve", "Starts a server for development"),
            ("dev", "Starts server for development in reload mode"),
        ]
        return "\n".join(["{}\t\t{}".format(*cmd) for cmd in commands])

    def __init_configuration(self):
        try:
            self.definitions = KaaDefinition()
        except DefinitionException as err:
            raise StartKaaError(err.message) from err

    def __run_server(self):
        try:
            self.__serve()
        except KeyboardInterrupt:
            print("Server stopped.")
            sys.exit(0)

    def __serve(self):
        self.__set_host_port()
        sys.stdout.write(f"{self.__get_name()} version {self.__get_version()}\n")
        sys.stdout.write(
            f"{self.definitions.get_name()} version {self.definitions.get_version()}\n"
        )
        host = self.definitions.get_host()
        port = self.definitions.get_port()
        sys.stdout.write(f"Server started at http://{host}:{port}\n\n")
        if not hasattr(self, "server") or self.server is None:
            self.server = Server().get_server()
        self.wsgi_server = make_server(
            host=host,
            port=int(port),
            app=lambda env, start_response: self.server.serve(env, start_response),
        )
        self.wsgi_server.serve_forever()

    def __monitor_changes(self, path, interval=1):
        last_mtime = None
        while True:
            curtent_mtime = max(
                os.path.getmtime(root)
                for root, _, files in os.walk(path)
                for f in files
            )
            if last_mtime and curtent_mtime > last_mtime:
                sys.stdout.write("Changes detected. Restarting server...")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            last_mtime = curtent_mtime
            time.sleep(interval)

    def __set_host_port(self):
        try:
            porthost = self.argv[2].split(":")
            if len(porthost) == 1:
                self.definitions.set_port(porthost[0])
            elif len(porthost) == 2:
                self.definitions.set_host(porthost[0])
                self.definitions.set_port(porthost[1])
            else:
                raise StartKaaError("Invalid host:port")
        except IndexError:
            pass


def main():
    # Add current working directory for load app modules
    sys.path.insert(0, os.getcwd())

    # Start
    try:
        Cli().execute()
    except StartKaaError as err:
        sys.stdout.write(err.message + "\n")
        sys.exit(1)
