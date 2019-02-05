import random
import csv

from rasa_core_sdk.events import SlotSet


def addToCsv(result):
    with open('actions/storage/breakfast.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow({result})

        csvfile.close()

        return "Added {0} to breakfast suggestions list.".format(result)


def getRandom():
    dataSet = set()

    with open('actions/storage/breakfast.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            dataSet.add(', '.join(row))

    dataSet.discard("")

    print(dataSet)

    randomValue = random.sample(dataSet, 1)

    return "I suggest {0} for breakfast.".format(str(randomValue)[2:-2])
