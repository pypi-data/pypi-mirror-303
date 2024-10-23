import sys
from .auth.actions import Auth
from .projects.actions import Projects
from .utils.config import read_config_file
from .files.actions import Files
from .sim.actions import Sim
from .hardware.actions import Hardware
from .lint.actions import Lint
from .agent.actions import Agent
from .git.actions import Git
from .daemons.actions import Daemons
from .jobs.actions import Jobs
from .organizations.actions import Organizations

from loguru import logger

logger.disable("primitive")


class Primitive:
    def __init__(
        self,
        host: str = "api.primitive.tech",
        DEBUG: bool = False,
        JSON: bool = False,
        token: str = None,
        transport: str = None,
    ) -> None:
        self.host = host
        self.session = None
        self.DEBUG = DEBUG
        self.JSON = JSON

        if self.DEBUG:
            logger.enable("primitive")
            logger.remove()
            logger.add(
                sink=sys.stderr,
                serialize=self.JSON,
                catch=True,
                backtrace=True,
                diagnose=True,
            )

        # Generate full or partial host config
        if not token and not transport:
            # Attempt to build host config from file
            try:
                self.get_host_config()
            except KeyError:
                self.host_config = {}
        else:
            self.host_config = {"username": "", "token": token, "transport": transport}

        self.auth: Auth = Auth(self)
        self.organizations: Organizations = Organizations(self)
        self.projects: Projects = Projects(self)
        self.jobs: Jobs = Jobs(self)
        self.files: Files = Files(self)
        self.sim: Sim = Sim(self)
        self.hardware: Hardware = Hardware(self)
        self.lint: Lint = Lint(self)
        self.agent: Agent = Agent(self)
        self.git: Git = Git(self)
        self.daemons: Daemons = Daemons(self)

    def get_host_config(self):
        self.full_config = read_config_file()
        self.host_config = self.full_config.get(self.host)

        if not self.host_config:
            raise KeyError(f"Host {self.host} not found in config file.")
