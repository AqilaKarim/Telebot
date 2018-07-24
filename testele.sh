#!/bin/bash 

scp aqila@192.168.44.227:/home/bot/chatid.txt /home/aqila

while IFS= read line
do
  token="your_bot_token"
  msg="Test Message"
  curl -s -F chat_id=$line -F text="$msg" https://api.telegram.org/bot$token/sendMessage > /dev/null
done < /home/aqila/chatid.txt
