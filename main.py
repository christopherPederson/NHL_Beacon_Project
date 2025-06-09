# import API from NHL_API_Commands import get_schedule
import requests
from NHL_API_Commands import get_schedule

def main():
    team_code = "EDM"  # Example team code for the Edmonton Oilers
    get_schedule(team_code)

if __name__ == "__main__":
    main()