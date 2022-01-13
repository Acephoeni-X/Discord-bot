import datetime
from datetime import datetime
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import random, requests
from discord_webhook import *

webhook=''
with open('../Keys/webhook.json', 'r+') as f:
    data = json.load(f)
    webhook = data['birthChannel']

print("Program started on ", datetime.now())

class initialise():

    url = f"{webhook}"
    scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/calendar']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../Keys/key.json', scopes)
    client = gspread.authorize(creds)
    sheet = client.open('Class_Reminders').get_worksheet(1)

    quotes = ["Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!",
              "Happy birthday! We hope all your birthday wishes and dreams come true.",
              "A wish for you on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. Happy birthday!",
              "Another adventure filled year awaits you. Welcome it by celebrating your birthday with pomp and splendor. Wishing you a very happy and fun-filled birthday!",
              "May the joy that you have spread in the past come back to you on this day. Wishing you a very happy birthday!",
              "Happy birthday! Your life is just about to pick up speed and blast off into the stratosphere. Wear a seat belt and be sure to enjoy the journey. Happy birthday!",
              "This birthday, We wish you abundant happiness and love. May all your dreams turn into reality and may lady luck visit your home today. Happy birthday to one of the sweetest people we have ever known.",
              "May you be gifted with life’s biggest joys and never-ending bliss. After all, you yourself are a gift to earth, so you deserve the best. Happy birthday.",
              "Count not the candles…see the lights they give. Count not the years, but the life you live. Wishing you a wonderful time ahead. Happy birthday.",
              "Forget the past; look forward to the future, for the best things are yet to come.",
              "Birthdays are a new start, a fresh beginning and a time to pursue new endeavors with new goals. Move forward with confidence and courage. You are a very special person. May today and all of your days be amazing!",
              "Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful tapestry of the world to make this year the best ever. Enjoy the ride.",
              "Be happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!"]

    def check_birth(self):

        while True:
            if "09:30:00" in str(datetime.now()):
                try:
                    records = self.sheet.get_all_records()
                    for all in records:
                        if re.search(r"\d\d-\d\d ", str(datetime.now()))[0].replace(" ", "") == all['Date']:
                            self.create_request(all['Date'], all['Name'])
                except Exception as e:
                    print("Error in code ")
                    continue


    def call_disco(self, date, name):
        quote = random.choice(self.quotes)
        embed = DiscordEmbed(title=f"Happy Birthday {name}", description=f"{quote}")
        embed.set_author(name="Birthday Reminder 🎉 🥳", url="https://github.com/rishi-Sharma2002")
        print(date)
        print(name)
        return embed

    def create_request(self, date, name):
        webhook = DiscordWebhook(url=self.url)
        embed = self.call_disco(date, name)
        webhook.add_embed(embed)
        webhook.execute()
        requests.post(self.url, data={"content": "@everyone"})

if __name__ == "__main__":
    i = initialise()
    i.check_birth()
