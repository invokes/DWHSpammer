credit = """
█▄░▄█ ▄▀▄ █▀▄ █▀▀     █▀▄ ▀▄░▄▀     ▀ █▄░█ ▐▌░▐▌ ▄▀▄ █░▄▀ █▀▀ 
█░█░█ █▀█ █░█ █▀▀     █▀█ ░░█░░     █ █░▀█ ░▀▄▀░ █░█ █▀▄░ █▀▀ 
▀░░░▀ ▀░▀ ▀▀░ ▀▀▀     ▀▀░ ░░▀░░     ▀ ▀░░▀ ░░▀░░ ░▀░ ▀░▀▀ ▀▀▀ 
"""
print(credit)

import time
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookurl = input("Enter the url of the webhook: ")
titlemsg = input("Enter the message title: ")
msgcontent = input("Enter the message you'd like to spam: ")
waitime = input("Enter how long would you like to wait before another message is spammed: ")



spam = True

while spam:
    time.sleep(waitime)
    webhook = DiscordWebhook(url=webhookurl)
    embed = DiscordEmbed(title=titlemsg, description=msgcontent)
    webhook.add_embed(embed)
    response = webhook.execute()