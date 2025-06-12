import requests

class Game:
    def __init__(self, teamID, gameID, dt):
        self.teamID = teamID
        self.gameID = gameID
        self.dt = dt
        self.prevScore = 0
        self.currScore = 0
        self.url = f"https://api-web.nhle.com/v1/gamecenter/{self.gameID}/boxscore"
    
    def poll_goal(self):
        # light weight polling to get most acurate live data

        response = requests.get(self.url)
        data = response.json()

        # Extract scores and state
        self.currScore = data["homeTeam"]["score"]

        if self.currScore <= self.prevScore:
            # accounting for ref reverting decision
            self.prevScore == self.currScore

            return False
        else:
            # update score
            self.prevScore == self.currScore
            
            return True
    
    def get_game_dt(self):
        return self.dt