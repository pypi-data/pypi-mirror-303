from subprocess import Popen, PIPE
import threading
import shlex
from loguru import logger


class Process:
    def __init__(
        self,
        cmd,
        env,
        workdir: str = ".",
    ):
        self.cmd = shlex.split(cmd)
        self.env = env
        self.workdir = workdir
        self.process = None
        self.stdout_thread = None
        self.stderr_thread = None
        self._errors = 0

    def start(self):
        # Start the process
        logger.info(f"cmd: {self.cmd}")
        logger.info(f"workdir: {self.workdir}")
        self.process = Popen(
            self.cmd,
            env=self.env,
            cwd=self.workdir,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
        )

        # Function to read and log output from a pipe
        def log_output(pipe, level):
            for line in iter(pipe.readline, ""):
                if line:
                    logger.log(level, line.rstrip())
                    if level == "ERROR":
                        self._errors += 1

            pipe.close()

        # Create threads for stdout and stderr
        self.stdout_thread = threading.Thread(
            target=log_output, args=(self.process.stdout, "INFO")
        )
        self.stderr_thread = threading.Thread(
            target=log_output, args=(self.process.stderr, "ERROR")
        )

        # Start the threads
        self.stdout_thread.start()
        self.stderr_thread.start()

    def wait(self):
        if self.process:
            # Wait for the process to complete
            self.process.wait()
            # Wait for the threads to finish reading output
            self.stdout_thread.join()
            self.stderr_thread.join()

    def run(self):
        """Start and wait for the process."""
        self.start()
        self.wait()

    def is_running(self):
        """Check if the process is still running."""
        return self.process and self.process.poll() is None

    def finish(self):
        """Make sure that logging finishes"""
        self.stderr_thread.join()
        self.stderr_thread.join()

        return self.process.poll()

    def terminate(self):
        """Terminate the process."""
        if self.process:
            self.process.terminate()

    def kill(self):
        """Kill the process."""
        if self.process:
            self.process.kill()

    @property
    def errors(self) -> int:
        return self._errors
