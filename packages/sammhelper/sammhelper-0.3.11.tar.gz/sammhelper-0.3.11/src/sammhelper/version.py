import importlib.metadata
import requests

def version():
    
    """
    Checks whether the newest version of sammhelper is installed.
    """

    installed_version = importlib.metadata.version("sammhelper")

    # Fetch the latest version from PyPI
    try:
        response = requests.get("https://pypi.org/pypi/sammhelper/json")
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
        latest_version = response.json()["info"]["version"]
    except requests.RequestException:
        print("Error: Unable to fetch the latest version of sammhelper from PyPI.")
    
    # Produce feedback for user
    if installed_version == latest_version:
        print(f"The newest version of sammhelper ({installed_version}) is already installed.")
    else:
        print (
            f"A new version of sammhelper is available ({latest_version}).\nIn order to update sammhelper, open your command window and enter: pip install --upgrade sammhelper"
        )