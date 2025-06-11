import datetime
import time
from GameOBJ import Game
from ScheduleOBJ import Schedule


def main():
    team_code = "EDM"  # Example team code for the Edmonton Oilers
    
    schedule = Schedule(team_code)

    while True:

        schedule.get_schedule()
        game = Game(team_code, schedule.gameIDs[0], schedule.gameTimes[schedule.gameIDs[0]])

        next_game_dt = game.get_game_dt

        # If the current time is less than the next game time sleep for 60 seconds before checking again
        if datetime.now() < next_game_dt:
            time.sleep(60)
        else:
            if game.poll_goal:
                #set gpio pins propper but print for now
                # this is where we check if the mute button is high or low
                print("GOAL")
            
            # Poll every second
            time.sleep(1)


if __name__ == "__main__":
    main()