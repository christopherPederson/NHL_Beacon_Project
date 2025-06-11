import requests
import json
import datetime
import GameOBJ
import datetime

class Schedule:
    def __init__(self, teamID):

        self.gameIDs = []
        self.gameTimes = {}
        self.teamID = teamID

    def get_schedule(self):
        # Retreiving game schedule

        # I did it this way, rather than contiuously polling the API, 
        # to prevent needlessly polling the API

        url = f"https://api-web.nhle.com/v1/club-schedule/{self.teamID}/week/now"
        response = requests.get(url)
        data = response.json()

        games = data["games"]


        # Extract game IDs
        for game in games:
            self.gameIDs.append(game["id"])

        # Map game IDs to start times
        for game in games:
            self.gameTimes[game["id"]] = self.convert_API_time(game["startTimeUTC"])

    def convert_API_time(self, timeString):
        # Convert time string to datetime object
        time_format = "%Y-%m-%dT%H:%M:%SZ"
        dt = datetime.datetime.strptime(timeString, time_format)
        # Convert to local time
        local_dt = dt.astimezone()

        return local_dt
    
    