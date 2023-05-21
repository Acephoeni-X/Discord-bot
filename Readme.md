# Birthday Reminder Bot

This is a Python program that sends birthday reminders to a Discord server. It uses the Google Sheets API to store and retrieve birthday information and the Discord Webhook API to send birthday messages to the server. The program runs continuously and checks for upcoming birthdays at a specific time every day.

## Installation

To use this program, you can follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies. It is recommended to use Docker for easy installation and isolation:

   ```bash
   docker build -t birthday-reminder .
   ```

3. Create a Discord webhook URL. You can find instructions on how to create a webhook [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

4. Obtain the necessary credentials for accessing the Google Sheets API. Follow the guide [here](https://developers.google.com/workspace/guides/create-credentials) to create a service account and obtain a JSON keyfile.

5. Rename the JSON keyfile to `webhook.json` and place it in the project directory.

## Configuration

Before running the program, you need to configure the following settings:

1. Set the `webhook` variable in the `initialise` class to your Discord webhook URL. Replace `https://discord.com/api/webhooks/879950702905028608/FSZCYPpoMx1O6AwVvjgxrNNoP25r6KEWkvf1d_LJhglx96iK9tyHf0xSj6B0mU371BpB` with your actual webhook URL.

   ```python
   webhook = 'https://discord.com/api/webhooks/your-webhook-url'
   ```

2. Set the name and index of the worksheet in your Google Sheets document. By default, the program uses the worksheet at index 1.

   ```python
   sheet = client.open('Class_Reminders').get_worksheet(1)
   ```

3. Customize the birthday quotes in the `quotes` list. You can add or remove quotes as desired.

## Usage

To start the birthday reminder bot, run the following command:

```bash
docker run -d birthday-reminder
```

The bot will continuously check for upcoming birthdays at 9:30 AM every day. If a birthday is found, it will send a birthday message to the Discord server specified in the webhook URL.

## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests on the [GitHub repository](https://github.com/Acephoeni-X/Discord-bot).
