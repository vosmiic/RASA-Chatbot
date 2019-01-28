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
* no
    - commute_form
    - form{"name": null}

## How far long commute stop
* workdistance
    - commute_form
    - form{"name": "commute_form"}
* stop
    - utter_ask_continue
* yes
    - action_deactivate_form
    - form{"name": null}
    - utter_stop

## Breakfast suggestion
* breakfastsuggestion
    - action_breakfast

## test
* test
    - utter_test
