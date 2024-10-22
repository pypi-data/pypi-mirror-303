from pathlib import Path
from primitive.utils.actions import BaseAction
import subprocess
from typing import Tuple
from loguru import logger
from ..utils.files import find_files_for_extension
from ..utils.verible import install_verible
from ..utils.cache import get_deps_cache


class Lint(BaseAction):
    def execute(self, source: Path = Path.cwd()) -> Tuple[bool, str]:
        logger.debug(f"Starting linter for source: {source}")
        files = find_files_for_extension(source, ".sv")
        if not files:
            message = "No files found to lint."
            logger.warning(message)
            return False, message

        logger.debug("Checking if verible is installed")
        verible_path = Path("verible-verilog-lint")
        try:
            subprocess.run([str(verible_path), "--version"], capture_output=True)
        except FileNotFoundError:
            logger.debug("Verible not found in $PATH. Looking in deps cache...")
            cache_dir = get_deps_cache()

            possible_dirs = cache_dir.glob("verible*")
            verible_dir = next(possible_dirs, None)

            if verible_dir is not None:
                verible_path = verible_dir / "bin" / verible_path
            else:
                logger.debug("Did not find verible. Installing...")
                try:
                    system_info = self.primitive.hardware.get_system_info()
                    verible_bin = install_verible(system_info=system_info)
                    verible_path = verible_bin / verible_path
                except Exception as exception:
                    message = f"Failed to install verible. {exception}"
                    logger.error(message)
                    return False, message

        try:
            subprocess.run([str(verible_path), "--version"], capture_output=True)
        except FileNotFoundError:
            message = "Verible is not installed. Please install it to run lint."
            logger.error(message)
            return False, message

        # TODO:
        # run is great for now! we will need to switch to Popen if we want to stream the output
        logger.debug("Running linter...")
        result = subprocess.run(
            [str(verible_path), *files],
            capture_output=True,
            text=True,
        )

        logger.debug("Linting complete.")

        message = ""
        if result.stderr:
            logger.error("\n" + result.stderr)
        if result.stdout:
            logger.info("\n" + result.stdout)
        message = "See above logs for linter output."

        if result.returncode != 0:
            if not self.primitive.DEBUG:
                message = result.stdout + result.stderr
            return (False, message)
        else:
            message = "Linting successful."

        return True, message
