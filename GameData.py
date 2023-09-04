# ---------------------------- LIBRARIES ------------------------------- #
import requests

# ---------------------------- CONSTANTS ------------------------------- #
PARAMETERS = {
    'amount': 10,
    'type': 'boolean'
}

# ---------------------------- QUESTION REQUESTS ------------------------------- #
response = requests.get('https://opentdb.com/api.php', params=PARAMETERS)
gamedata = response.json()['results']
