from datetime import datetime
import json
from pytz import timezone
from discord_webhook import DiscordEmbed, DiscordWebhook
import gspread, random, time, requests
from oauth2client.service_account import ServiceAccountCredentials


formatH  = "%H"
formatM  = "%M"
formatS  = "%S"
webhook=''

with open('../Keys/webhook.json', 'r+') as f:
    data = json.load(f)
    webhook = data['classChannel']

print("Program started on ", datetime.now())

class initialise():

    # To access spreadsheet
    scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/calendar']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../Keys/key.json', scopes)
    client = gspread.authorize(creds)
    sheet = client.open('Class_Reminders').sheet1

    # To access discord webhook embed
    url = f"{webhook}"
    def embed_(self, class_time, links):
        colors = ["FF0000", "2B00FF", "59FF83", "932EFF", "FBFF2B", "FF00EA", "FFB700", "FF6912", "EAFF2E"]
        colors = random.choice(colors)
        link, class_ = "", ""
        embed = DiscordEmbed(title=f'{class_}', description=f'{link} \n Class Time: {class_time} \n Class Link: {links}',color=colors)
        embed.set_author(name="Class Reminder", url="https://github.com/Rishi-Sharma2002", icon_url="https://i.imgur.com/Balxh6q.gif")
        embed.set_thumbnail(url="https://i.imgur.com/XcMT1mH.png")

        return embed

    # Check google sheets
    def checkSheet(self):
        while True:
            try:
                records = self.sheet.get_all_records()
                for j in range(len(records)):
                    now_utc = datetime.now(timezone('UTC'))
                    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

                    hour = now_asia.strftime(formatH)
                    minute= now_asia.strftime(formatM)
                    sec  = now_asia.strftime(formatS)


                    if int(sec)>=2 and int(sec)<=50:
                        time.sleep(60-int(sec))


                    if str(hour+':'+minute+':00') in str(records[j]['Time']) and records[j]['Days'] == datetime.today().weekday():
                        print(f"Send Message on {now_asia} at {records[j]['Time']} on {records[j]['Days']} with message: {records[j]['Link']}.")
                        self.create_request(records[j]['Time'], records[j]['Link'])
                        self.googleChat(records[j]['Time'], records[j]['Link'])
                        time.sleep(3)
            except Exception:
                continue

    # making request to the discord
    def create_request(self, times, links):
        webhook = DiscordWebhook(url=i.url)
        embed = i.embed_(times, links)
        webhook.add_embed(embed)
        webhook.execute()
        requests.post(self.url, data={"content": "@everyone"})


if __name__ == "__main__":
        i = initialise()
        i.checkSheet()
        #requests.post(i.url, data={"content": "@everyone"})

