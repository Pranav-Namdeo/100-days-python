import requests

data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data.raise_for_status()
question = data.json()

question_data = question["results"]
