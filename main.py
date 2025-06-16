import datetime
import time
from GameOBJ import Game
from ScheduleOBJ import Schedule
# import RPi.GPIO as GPIO


# def main():
#     team_code = "EDM"  # Example team code for the Edmonton Oilers
    
#     schedule = Schedule(team_code)

#     # Output to controll relay for light
#     GPIO.setmode(GPIO.BCM)     # Use GPIO pin numbers (not board numbers)
#     GPIO.setwarnings(False)
#     GPIO.setup(5, GPIO.OUT)

#     while True:

#         schedule.get_schedule()
#         game = Game(team_code, schedule.gameIDs[0], schedule.gameTimes[schedule.gameIDs[0]])

#         next_game_dt = game.get_game_dt()

#         # If the current time is less than the next game time sleep for 60 seconds before checking again
#         if datetime.datetime.now().astimezone() < next_game_dt:
#             time.sleep(60)
#         else:
#             if game.poll_goal():
#                 GPIO.output(5, GPIO.HIGH) # Turn ON pin 5
#                 time.sleep(3)
#                 GPIO.output(5, GPIO.LOW)  # Turn OFF pin 5
            
#             # Poll every 500ms
#             time.sleep(0.5)
    
#     GPIO.cleanup()


#DEBUG main function for running on PC
def main():
    team_code = "EDM"  # Example team code for the Edmonton Oilers
    
    schedule = Schedule(team_code)

    while True:

        schedule.get_schedule()
        game = Game(team_code, schedule.gameIDs[0], schedule.gameTimes[schedule.gameIDs[0]])

        next_game_dt = game.get_game_dt()

        # If the current time is less than the next game time sleep for 60 seconds before checking again
        if datetime.datetime.now().astimezone() < next_game_dt:
            print(f"Non Active {datetime.datetime.now()}")
            time.sleep(60)
        else:
            if game.poll_goal():
                print(f"GOAL {datetime.datetime.now()}")

            # Poll every 500ms
            time.sleep(0.5)
            print(f"        No goal detected {datetime.datetime.now()}")
    GPIO.cleanup()


if __name__ == "__main__":
    main()