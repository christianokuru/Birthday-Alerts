# -*- coding: utf-8 -*-

import json
import requests
import time
import socket
from datetime import datetime, timedelta

def get_details():
  name = input("Enter name: ")
  birthday = input("Enter Birthday(MM/DD): ")
  phone_number = input("Enter Phone Number: ")
  email = input("Enter Email Address: ")
  return{"name": name, "birthday": birthday, "phone_number": phone_number, "email": email}

def save_details(details):
  with open("details.json", "w") as f:
    json.dump(details, f)

def check_internet_connection():
  try:
    host = socket.gethostbyname("www.google.com")
    s = socket.create_connection((host, 80), 2)
    return True
  except OSError:
    print("NO INTERNET CONNECTION")
  return False

def list_birthdays():
  with open("details.json", "r") as cow:
    details = json.load(cow)
  print("Saved Birthdays: ")
  for person in details:
    name = person["name"]
    birthday = person["birthday"]
    print("{}: {}".format(name, birthday))

def send_whatsapp_message(phone_number, message):
  if check_internet_connection():
      url = "https://api.whatsapp.com/v1/messages"
      headers = {
          "Authorization": "Bearer <your_auth_token>",
          "Content-Type": "application/json"
      }
      payload = {
          "phoneNumber": phone_number,
          "message": message
      }
      response = requests.post(url, headers=headers, json=payload)
      if response.status_code == 200:
          print("Message sent successfully")
      else:
          print("Failed to send message")

def remind_birthday():
    with open("details.json", "r") as f:
        details = json.load(f)
    today = datetime.today().strftime("%m/%d")
    for person in details:
        name = person["name"]
        birthday = person["birthday"]
        phone_number = person["phone_number"]
        if birthday == today:
            message = "Happy birthday {}!".format(name)
            send_whatsapp_message(phone_number, message)
            print("Sent birthday message to {}".format(name))
        else:
          print("NO BIRTHDAYS TODAY!!")

def keep_checking_birthdays():
    while True:
        remind_birthday()
        time.sleep(86400) # check every 24 hours

if __name__ == "__main__":
    details = []
    while True:
        print("What would you like to do?")
        print("Enter '1' to add a person's details")
        print("Enter '2' to send Reminders")
        print("Enter '3' to keep checking for birthdays")
        print("Enter '4' to list all saved birthdays")
        print("Enter '5' to quit")
        choice = input("Enter your choice ")

        if choice == "1":
            details.append(get_details())
            save_details(details)
        elif choice == "2":
            remind_birthday()
        elif choice == "3":
            keep_checking_birthdays()
        elif choice == "4":
            list_birthdays()
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again")
