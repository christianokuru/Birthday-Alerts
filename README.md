# Birthday-Alerts
This repo contians the codes for creating a Birthday reminder and alert.

For those of us who regularly forget the birthdays of our family and friends, this code was developed for us.

When you initially execute the script, it will request some personal information of your friends, including their name, birthday (which excludes the year of birth), phone number, and email. 

All these detials will be stored in the json file.

The script will check today's date and compare it to the birthdays in the json file... If any of the matches, it will send a happy birthday message to that person's number(assuming the number is connected to whatsapp).

For best use, run this script on a server repeatedly so that it will keep checking the json file for birthdays.
