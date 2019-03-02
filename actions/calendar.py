import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Declan123!",
    database="calendar",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

def searchDatabase(formattedDate):
    search = 'SELECT * FROM calendar WHERE dateTime LIKE "{0}%"'.format(formattedDate)
    mycursor.execute(search)
    myresult = mycursor.fetchall()
    events = []
    eventsCount = 0
    if str(formattedDate).endswith('00:00:00'):
        # not time
        for x in myresult:
            eventsCount = eventsCount + 1
            events.append(x[2])
    elif not str(formattedDate).endswith('00:00:00'):
        # time
        for x in myresult:
            eventsCount = eventsCount + 1
            events.append(x[2] + " at " + str(x[1])[11:][:5])

    if myresult == list([]):
        return "You don't have any planned events on that day."
    joinedEvents = " and ".join(events)
    if len(myresult) == 1:
        return str("You have 1 event on that day, which is {0}".format(joinedEvents))
    if len(myresult) > 1:
        return str("You have {0} events on on that day, including {1}".format(eventsCount, joinedEvents))
    return str(myresult)

def addToDatabase(formattedDate, eventText):
    if str(eventText) is not None:
        insert = 'INSERT INTO calendar (dateTime, eventDisc) VALUES ("{0}", "{1}")'.format(formattedDate, eventText)
        mycursor.execute(insert)
        mydb.commit()
        return "I have created the event '{0}' at {1}.".format(eventText, formattedDate)
    else:
        insert = 'INSERT INTO calendar (dateTime, eventDisc) VALUES ("{0}", "{1}")'.format(formattedDate, "Event")
        mycursor.execute(insert)
        mydb.commit()
        return "I have created an event at {0}.".format(formattedDate)

