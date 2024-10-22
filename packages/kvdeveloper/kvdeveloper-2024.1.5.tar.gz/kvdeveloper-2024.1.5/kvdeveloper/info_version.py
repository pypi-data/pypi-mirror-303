import requests
import pkg_resources
from rich.console import Console
from rich.panel import Panel
from datetime import datetime, timedelta
from pathlib import Path
import threading

console = Console()

# File to store the last checked timestamp
LAST_CHECK_FILE = Path.home() / ".kvdeveloper_last_version_check"


def check_new_version(package_name: str):
    print("checking")
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        latest_version = response.json()["info"]["version"]
        installed_version = pkg_resources.get_distribution(package_name).version

        if latest_version != installed_version:
            console.print(
                Panel(
                    f"[bold yellow]A new version of {package_name} is available! "
                    f"(Installed: {installed_version}, Latest: {latest_version})\n"
                    "Run [bold green]pip install --upgrade {package_name}[/bold green] to update.",
                    title="[bold red]Update Available![/bold red]",
                    expand=False,
                )
            )
        else:
            console.print(f"\nUsing the latest version v{latest_version}.")
    except Exception as e:
        console.print(f"[red]Error checking version: {e}[/red]")


def should_check_version() -> bool:
    if LAST_CHECK_FILE.exists():
        with LAST_CHECK_FILE.open("r") as file:
            last_checked = datetime.strptime(file.read().strip(), "%Y-%m-%d")
        return datetime.now() - last_checked > timedelta(days=10)
    else:
        return True


def update_last_checked_date():
    with LAST_CHECK_FILE.open("w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d"))


# Function to run version checking in the background
def background_version_check(package_name: str):
    if should_check_version():
        check_new_version(package_name)
        update_last_checked_date()


def start_version_check_thread(package_name: str):
    thread = threading.Thread(
        target=background_version_check, args=(package_name,), daemon=True
    )
    thread.start()
