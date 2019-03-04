## Greeting
* greeting
    - utter_greeting
    - action_test

## User is happy
* mood_happy
    - utter_happy
    
## User is sad
* mood_sad
    - utter_sad

## Goodbye
* goodbye
    - utter_goodbye
    
## Weather
* weather{"location": "Caracas"}
    - action_weather
    
## IP Weather
* IPweather
    - action_get_weather_from_ip

## How far long commute
* workdistance
    - commute_form
    - form{"name": "commute_form"}
    - form{"name": null}

## How far long commute stop but continue
* workdistance
    - commute_form
    - form{"name": "commute_form"}
* stop
    - utter_ask_continue
* mood_deny
    - commute_form
    - form{"name": null}

## How far long commute stop
* workdistance
    - commute_form
    - form{"name": "commute_form"}
* stop
    - utter_ask_continue
* mood_affirm
    - action_deactivate_form
    - form{"name": null}
    - utter_stop

## Breakfast suggestion
* breakfastsuggestion
    - action_suggestbreakfast

## Add to breakfast list form
* addtobreakfast
    - breakfast_form
    - form{"name": "breakfast_form"}
    - form{"name": null}
    - action_wipebreakfast

## Add to breakfast list form stop but continue
* addtobreakfast
    - breakfast_form
    - form{"name": "breakfast_form"}
* stop
    - utter_ask_continue
* mood_deny
    - breakfast_form
    - form{"name": null}
    
## Add to breakfast list form stop
* addtobreakfast
    - breakfast_form
    - form{"name": "breakfast_form"}
* stop
    - utter_ask_continue
* mood_affirm
    - action_deactivate_form
    - form{"name": null}
    - utter_stop

## Check calendar events
* check_calendar
    - action_get_date_value
    - action_search_database
    
## Add to calendar
* add_to_calendar
    - action_get_date_value
    - action_add_to_calendar
    - action_wipe_event_text

## test
* test
    - action_get_date_value
    - utter_test

