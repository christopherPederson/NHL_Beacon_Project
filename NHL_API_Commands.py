import requests

def get_schedule(teamCode):
    # retreiving game schedule 

    url = f"https://api-web.nhle.com/v1/club-schedule/{teamCode}/week/now"

    response = requests.get(url)
    data = response.json()
    print("in get_schedule")
    print(data)