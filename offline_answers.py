import os
import webbrowser
import datetime
import random
from win10toast import ToastNotifier
import threading
import time

# Initialize Windows toast notifications
toaster = ToastNotifier()

# Dictionary to keep track of opened apps (for safer closing)
opened_apps = {}

# Function to show reminder popup after a delay
def set_reminder(reminder_text, reminder_time):
    """
    reminder_text: message to show
    reminder_time: datetime object when to show the reminder
    """
    def reminder_thread():
        while True:
            now = datetime.datetime.now()
            if now >= reminder_time:
                toaster.show_toast("Reminder", reminder_text, duration=10)
                break
            time.sleep(5)  # check every 5 seconds
    threading.Thread(target=reminder_thread).start()


def run_command(message):
    msg = message.lower()

    # Greetings
    if "hello" in msg or "hi" in msg:
        return "Hello Abhishek. How can I help you?"

    # Time & Date
    if "time" in msg:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M")
    if "date" in msg:
        return "Today's date is " + datetime.datetime.now().strftime("%d %B %Y")

    # Open websites
    if "open google" in msg:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    if "open youtube" in msg:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # Open apps
    if "open notepad" in msg:
        os.system("notepad")
        opened_apps['notepad'] = "notepad.exe"
        return "Opening Notepad"

    if "open calculator" in msg:
        os.system("start calculator:")
        opened_apps['calculator'] = "ApplicationFrameHost.exe"
        return "Opening Calculator"

    if "open camera" in msg:
        os.system("start microsoft.windows.camera:")
        opened_apps['camera'] = ["WindowsCamera.exe", "ApplicationFrameHost.exe"]
        return "Opening Camera"

    # Jokes
    if "joke" in msg:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer go to the doctor? Because it had a virus.",
            "Why was the computer cold? It left its Windows open."
        ]
        return random.choice(jokes)

    # Calculator via text
    if "calculate" in msg:
        try:
            exp = msg.replace("calculate", "").strip()
            result = eval(exp)
            return "The result is " + str(result)
        except:
            return "Sorry I could not calculate that."

    # Close apps
    if "close" in msg:
        # Check what app user wants to close
        if "notepad" in msg:
            os.system("taskkill /f /im notepad.exe")
            opened_apps.pop('notepad', None)
            return "Closed Notepad"

        if "calculator" in msg:
            os.system("taskkill /f /im ApplicationFrameHost.exe")
            opened_apps.pop('calculator', None)
            return "Closed Calculator"

        if "camera" in msg:
            os.system("taskkill /f /im WindowsCamera.exe")
            os.system("taskkill /f /im ApplicationFrameHost.exe")
            opened_apps.pop('camera', None)
            return "Closed Camera"

        if "chrome" in msg:
            os.system("taskkill /f /im chrome.exe")
            opened_apps.pop('chrome', None)
            return "Closed Chrome"

        return "Please specify which app to close (Notepad, Calculator, Camera, Chrome, etc.)"

    # Reminder
    if "remind me" in msg:
        try:
            # Expected format: "remind me to [task] at HH:MM"
            parts = msg.split(" at ")
            reminder_text = parts[0].replace("remind me to", "").strip()
            reminder_time = datetime.datetime.strptime(parts[1].strip(), "%H:%M")
            # Set reminder for today
            now = datetime.datetime.now()
            reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day)
            set_reminder(reminder_text, reminder_time)
            return f"Reminder set: '{reminder_text}' at {reminder_time.strftime('%H:%M')}"
        except:
            return "Sorry, I could not set the reminder. Use format: 'remind me to [task] at HH:MM'"

    return None