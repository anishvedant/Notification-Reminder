import time
from plyer import notification

if __name__ == '__main__':
    # Call the notify method from the plyer library
    notification.notify(
        title = "Study Book",  # Title of the notification
        app_name = "Reading",  # Name of the application sending the notification
        ticker = "Hello",  # Ticker text for the notification
        message = ("By creating a bedtime routine that includes reading, you can signal "
                   "to your body that it is time to sleep. Therefore, by setting your phone "
                   "aside and picking up a book, you are telling your brain that it is time to quiet down"),  # Notification message
        app_icon = "Paomedia-Small-N-Flat-Book-bookmark.ico",  # Icon for the notification
        timeout = 20  # Duration in seconds for the notification to stay visible
    )
