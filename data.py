import requests


class GiveQuestionData():
    
    def __init__(self) :
        parameters = {
            "amount": 10,
            "type": "boolean"
        }
        response = requests.get(url="https://opentdb.com/api.php", params = parameters)
        response.raise_for_status()
        self.Data = response.json()
        self.QuestionBank = self.Data["results"]