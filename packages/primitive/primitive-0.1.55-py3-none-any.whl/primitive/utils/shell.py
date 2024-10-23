from pathlib import Path
import subprocess


def add_path_to_shell(path: Path):
    if not path.exists():
        raise Exception(f"{path} does not exist.")

    try:
        subprocess.run(["fish_add_path", path], capture_output=True)
        return True
    except FileNotFoundError:
        pass

    profile_path = None

    if Path.home().joinpath(".bash_profile").exists():
        profile_path = Path.home().joinpath(".bash_profile")
    elif Path.home().joinpath(".bashrc").exists():
        profile_path = Path.home().joinpath(".bashrc")
    elif Path.home().joinpath(".zshrc").exists():
        profile_path = Path.home().joinpath(".zshrc")
    elif Path.home().joinpath(".profile").exists():
        profile_path = Path.home().joinpath(".profile")
    elif Path.home().joinpath(".bash_login").exists():
        profile_path = Path.home().joinpath(".bash_login")
    else:
        raise Exception(f"Failed to add {path} to PATH")

    with open(profile_path, "a") as file:
        file.write(f"export PATH={path}:$PATH\n")

    return True
