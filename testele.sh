#!/bin/bash 

scp aqila@192.168.44.227:/home/bot/chatid.txt /home/aqila

while IFS= read line
do
  token="697263182:AAEljlmqD5wGKO1q6eSb6_Sn710gIOWey0s"
  msg="Test Message"
  curl -s -F chat_id=$line -F text="$msg" https://api.telegram.org/bot$token/sendMessage > /dev/null
done < /home/aqila/chatid.txt
