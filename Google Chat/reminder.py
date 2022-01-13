from datetime import datetime
from pytz import timezone
import gspread, time, json
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

formatH  = "%H"
formatM  = "%M"
formatS  = "%S"
webhook = ''

with open('../Keys/webhook.json', 'r+') as f:
    data = json.load(f)
    webhook = data['gmailChannel']

print("Program started on ", datetime.now())


class initialise():

    # To access spreadsheet
    scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/calendar']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../Keys/key.json', scopes)
    client = gspread.authorize(creds)
    sheet = client.open('Class_Reminders').sheet1

    def googleChat(self, time, link):

        url = f'{webhook}'

        bot_message = {
            'text' : f'Time: {time}\nLink: {link}'
        }

        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=json.dumps(bot_message),
        )


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
                        self.googleChat(records[j]['Time'], records[j]['Link'])
                        time.sleep(3)
            except Exception:
                continue

if __name__ == "__main__":
        i = initialise()
        i.checkSheet()