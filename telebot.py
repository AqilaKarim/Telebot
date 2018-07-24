#!/usr/bin/python

import os
import requests 
from time import sleep 
import subprocess

class BotHandler:

  def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot" + token + "/"

  def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

  def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

  def leave_chat(self, chat_id):
        params = {'chat_id': chat_id}
        method = 'leaveChat'
        resp = requests.post(self.api_url + method, params)
        return resp

  def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
  
  def check(self, chat_id):
    datafile = file('/home/aqila/chatid.txt')
    for line in datafile:
      if str(chat_id) in line:
        return True
    return False

ripe_bot = BotHandler('697263182:AAEljlmqD5wGKO1q6eSb6_Sn710gIOWey0s')  

def main():  
  new_offset = None

  while True:
    ripe_bot.get_updates(new_offset)
    last_update = ripe_bot.get_last_update()
    last_update_id = last_update['update_id']
    last_chat_text = last_update['message']['text']
    last_chat_id = last_update['message']['chat']['id']

    if last_chat_text.lower() == "/start" :
            ripe_bot.send_message(last_chat_id, 'Hello there! You will receive notifications about the probes from now on')
            if ripe_bot.check(last_chat_id) == False:
              command = "echo " + str(last_chat_id) + " >> /home/aqila/chatid.txt"
              os.system(command)
            new_offset = last_update_id + 1

    elif last_chat_text.lower() == "/leave" :
            ripe_bot.send_message(last_chat_id, 'Bye!')
            command = "sed -i /" + str(last_chat_id) + "/d /home/aqila/chatid.txt" 
            os.system(command)
            new_offset = last_update_id + 1


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()

