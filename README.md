# Telebot
Telegram Bot for sending maintenance alerts from RIPE GSM Autoprobe in https://github.com/draskolnikova/ripe-gsm
Replace "your_bot_token" with your Telegram Bot token

# How to use:
Run the telebot.py script on a server to listen for incoming telegram requests. From your Telegram, add the RIPE Atlas Bot and type "/start" to register your ID to chats list. The bot will broadcast notifications to all the IDs in chats list. 
Type "/leave" to remove your ID from the chats list. 
Don't forget to change the path to the chatid file to your desired path.

# Sending notifications
Use the testele.sh script to send messages to all IDs in the chats list. Integrate the commands in this script to your own script.
