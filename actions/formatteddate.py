from rasa_nlu.model import Interpreter
import json


def getDate(date):
    interpreter = Interpreter.load("./models/current/nlu")
    result = interpreter.parse(date)
    data = json.dumps(result, indent=2)
    stringData = json.loads(data)
    formattedData = str(stringData["entities"][0]["value"]).replace("T", " ")[:19]

    return formattedData


def testGetDate(date):
    interpreter = Interpreter.load("./models/current/nlu")
    result = interpreter.parse(date)
    data = json.dumps(result, indent=2)
    stringData = json.loads(data)
    return str(stringData["entities"][0]["value"]).replace("T", " ")[:19]
