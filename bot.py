from telethon.sync import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
import json
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#LOAD API & BOT SECRETS
with open("/home/bot/voting_bot/discourse-voting-bot-telegram/telegram-secrets.json", 'r') as secrets_file:
    secret = json.load(secrets_file)

api_id = secret["id"]
api_hash = secret["hash"]
bot_token = secret["token"]

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

admins = client.get_participants(chat, filter=ChannelParticipantsAdmins)
@bot.on(events.NewMessage(from_users=admins,pattern='/start'+'@'+bot.get_me().username))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hi!')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'+'@'+bot.get_me().username))
async def start(event):
    """Send a message when the command /help is issued."""
    await event.respond("The following commands are at your disposal: /start, /tip and /balance \n \n Initiating command /tip has a specfic format,\n use it like so:" + "\n \n Parameters: \n <user> = target user to tip \n <amount> = amount of votes to send \n \n Tipping format: \n /tip <user> <amount>")
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/tip'+'@'+bot.get_me().username))
async def start(event):
    """Send a message when the command /tip is issued."""
    await event.respond("The following commands are at your disposal: /start, /tip and /balance \n \n Initiating command /tip has a specfic format,\n use it like so:" + "\n \n Parameters: \n <user> = target user to tip \n <amount> = amount of votes to send \n \n Tipping format: \n /tip <user> <amount>")
    raise events.StopPropagation



def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()







# def deposit(bot, update):
# 	user = update.message.from_user.username
# 	if user is None:
# 		bot.send_message(chat_id=update.message.chat_id, text="Please set a telegram username in your profile settings!")
# 	else:
# 		address = "/usr/local/bin/etheruemd"
# 		result = "getAccountAddress"
# 		clean = (result.stdout.strip()).decode("utf-8")
# 		bot.send_message(chat_id=update.message.chat_id, text="@{0} your depositing address is: {1}".format(user,clean))
#
# def tip(bot,update):
# 	user = update.message.from_user.username
# 	target = update.message.text[5:]
# 	amount =  target.split(" ")[1]
# 	target =  target.split(" ")[0]
# 	if user is None:
# 		bot.send_message(chat_id=update.message.chat_id, text="Please set a telegram username in your profile settings!")
# 	else:
# 		machine = "@VoteAndTipBot"
# 		if target == machine:
# 			bot.send_message(chat_id=update.message.chat_id, text="HODL.")
# 		elif "@" in target:
# 			target = target[1:]
# 			user = update.message.from_user.username
# 			result = 1000
# 			balance = float(result)
# 			amount = float(amount)
# 			if balance < amount:
# 				bot.send_message(chat_id=update.message.chat_id, text="@{0} you have insufficent funds.".format(user))
# 			elif target == user:
# 				bot.send_message(chat_id=update.message.chat_id, text="You can't tip yourself silly.")
# 			else:
# 				balance = str(balance)
# 				amount = str(amount)
# 				tx = "move"
# 				bot.send_message(chat_id=update.message.chat_id, text="@{0} tipped @{1} of {2} VOTES".format(user, target, amount))
# 		else:
# 			bot.send_message(chat_id=update.message.chat_id, text="Error that user is not applicable.")
#
# def balance(bot,update):
# 	price = float(100)
# 	user = update.message.from_user.username
# 	if user is None:
# 		bot.send_message(chat_id=update.message.chat_id, text="Please set a telegram username in your profile settings!")
# 	else:
# 		balance  = float(1000)
# 		fiat_balance = balance * price
# 		fiat_balance = str(round(fiat_balance,3))
# 		balance =  str(round(balance,3))
# 		bot.send_message(chat_id=update.message.chat_id, text="@{0} your current balance is: {1} VOTES ≈  ${2}".format(user,balance,fiat_balance))
#
# def price(bot,update):
# 	price = 10
# 	fiat = "EUR"
# 	kkz = ("eur")
# 	percent = 5
# 	btc = 200
# 	sats = 200023
# 	bot.send_message(chat_id=update.message.chat_id, text="Powerledger is valued at {0} Δ {1} ≈ {2}".format(price,percent,sats) + " ฿")
#
# def withdraw(bot,update):
# 	user = update.message.from_user.username
# 	if user is None:
# 		bot.send_message(chat_id=update.message.chat_id, text="Please set a telegram username in your profile settings!")
# 	else:
# 		target = update.message.text[9:]
# 		address = target[:35]
# 		address = ''.join(str(e) for e in address)
# 		target = target.replace(target[:35], '')
# 		amount = float(target)
# 		balance = float(1000)
# 		if balance < amount:
# 			bot.send_message(chat_id=update.message.chat_id, text="@{0} you have insufficent funds.".format(user))
# 		else:
# 			amount = str(amount)
# 			bot.send_message(chat_id=update.message.chat_id, text="@{0} has successfully withdrew to address: {1} of {2} VOTES" .format(user,address,amount))
