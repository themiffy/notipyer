import json
import schedule
import time
from tkinter import messagebox, Tk

def show_notification(notification):
    messagebox.showinfo(notification['name'], notification['text'])
    root.update()

with open('settings.json') as f:
    data = json.load(f)

notifications = data['notifications']

root = Tk()
root.withdraw()

for notification in notifications:
    schedule.every().day.at(notification['time']).do(show_notification, notification)

while True:
    schedule.run_pending()
    time.sleep(60)