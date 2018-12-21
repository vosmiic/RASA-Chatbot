from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "what is the weather like in London"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))