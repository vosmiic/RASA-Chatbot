from typing import List, Text

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted

from .getWeather import getLocationWeather
from .getLocation import getAPI
from .getMapsDistance import getDistance
from .breakfastSuggestion import getRandom, addToCsv
from .formatteddate import getDate
from .calendar import searchDatabase, addToDatabase


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


class ActionSetHome(Action):
    def name(self):
        return "action_sethome"

    def run(self, dispatcher, tracker, domain):

        return []


class ActionSetWork(Action):
    def name(self):
        return "action_setwork"

    def run(self, dispatcher, tracker, domain):

        return []


class CommuteForm(FormAction):
    def name(self):
        return "commute_form"

    def required_slots(self, tracker):
        return ["worklocation", "homelocation"]

    def submit(self, dispatcher, tracker, domain):

        dispatcher.utter_message(getDistance(tracker.get_slot("homelocation"), tracker.get_slot("worklocation")))

        return []


class ActionSuggestBreakfast(Action):
    def name(self):
        return "action_suggestbreakfast"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        dispatcher.utter_message(getRandom())
        return


class BreakfastForm(FormAction):
    def name(self):
        return "breakfast_form"

    def required_slots(self, tracker):
        return ["breakfast"]

    def submit(self, dispatcher, tracker, domain):

        dispatcher.utter_message(addToCsv(tracker.get_slot("breakfast")))

        return []


class ActionWipeBreakfastSlot(Action):
    def name(self):
        return "action_wipebreakfast"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):

        return [SlotSet("breakfast", None)]


class ActionGetDateValue(Action):
    def name(self):
        return "action_get_date_value"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        return [SlotSet("formattedDate", getDate(tracker.get_slot("date")))]


class ActionSearchDatabase(Action):
    def name(self):
        return "action_search_database"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        dispatcher.utter_message(searchDatabase(tracker.get_slot("formattedDate")))
        return []

class ActionAddToCalendar(Action):
    def name(self):
        return "action_add_to_calendar"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        dispatcher.utter_message(addToDatabase(tracker.get_slot("formattedDate"), tracker.get_slot("eventText")))
        return []

class ActionWipeEventText(Action):
    def name(self):
        return "action_wipe_event_text"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        return [SlotSet("eventText", None)]
