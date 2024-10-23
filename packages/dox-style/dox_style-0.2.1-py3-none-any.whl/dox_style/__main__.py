from pprint import pprint
from .checks.main import generate_options

if __name__ == "__main__":
    print("Available stylecheck options (and their defaults):\n")
    pprint(generate_options(), sort_dicts=False, width=100, indent=4)
