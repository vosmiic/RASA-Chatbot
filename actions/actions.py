from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted
from .getWeather import getLocationWeather


class ActionWeather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(getLocationWeather(tracker.get_slot("location")))

        return []


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Successful test")
        return []
