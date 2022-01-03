
import datetime
from time import time
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

from pyasn1_modules.rfc2459 import Name

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\pc owner\\Desktop\\Complete-Python-3-Bootcamp-master\\MySavedFiles\\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("timecardsheet").sheet1



class User():
    def __init__(self,name,id,department=None):
        self.name=name
        self.id=id
        self.department=department

#enter name/id/department
name=input("Enter name: ")
id=input("Enter ID: ")
department=input('Enter department: ')

thedate = datetime.now().date()

person=User(name,id,department)
print(person.name + ' ' + person.id + ' ' + person.department)

#punch in time
question_in=None
while question_in not in ('y','n'):
    question_in=input("Do you want to punch in? 'y' or 'n' ")
    if question_in=='y':
        punch_in = datetime.now()
        print(punch_in)
    elif question_in =='n':
        print('have a nice day')
        exit()

#going on lunch or punching out?
question_lunch_out=None
question_lunch_out=input("Are you taking a lunch? 'y'? ")
if question_lunch_out=='y':
    lunch_punch_out=datetime.now()
    print(lunch_punch_out)
    question_lunch_in=input("Are you back from lunch? 'y'? ")
    if question_lunch_in=='y':
        lunch_punch_in=datetime.now()
        print(lunch_punch_in)
elif question_lunch_out=='n':
    pass

#punch out time
question_out=None
while question_out not in ('y','n'):
    question_out=input("Do you want to punch out? 'y' or 'n' ")
    if question_out=='y':
        punch_out = datetime.now()
        print(punch_out)
    elif question_out=='n':
        pass

#display time between punches if lunch taken
#send to google sheets
if question_lunch_out =='y':
    shift_with_lunch = (punch_out - punch_in) - (lunch_punch_in - lunch_punch_out)
    print(f'{name}, id:{id}, your shift time was {shift_with_lunch}')
    sheet.insert_row((name, id, department, punch_in.strftime("%I:%M %p"), lunch_punch_in.strftime("%I:%M %p"), lunch_punch_out.strftime("%I:%M %p"), punch_out.strftime("%I:%M %p"), str(shift_with_lunch), str(thedate)),2)

#display time between punches if no lunch
#send to google sheets
else:
    shift_time = punch_out - punch_in
    print(f'{name}, id:{id}, your shift time was {shift_time}')
    sheet.insert_row((name, id, department, punch_in.strftime("%I:%M %p"), 'None', 'None', punch_out.strftime("%I:%M %p"), str(shift_time), str(thedate)),2)

