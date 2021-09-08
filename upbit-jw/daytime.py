import requests
from datetime import datetime
import pyupbit

#upbit
secret = "SGVXHE7ITVvhSZWvunxpQXFPjqhxA0gwlHlxUYsP"
access = "z2mHQKCNtJUeHgvc8nIW5DYFGCCrNQGfh9ipd3Az"
upbit = pyupbit.Upbit(access,secret)

#posting the message
def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
                            headers={"Authorization": "Bearer "+token},
                            data={"channel": channel,"text": text}
                            )
#checking current bitcoin price
def get_current_bit():
    price=pyupbit.get_current_price("KRW-BTC")
    print(price)
    return price

#message part
def making_message():
    mess = get_current_bit()
    return mess


SLACK_BOT_TOKEN = "xoxb-1610685610342-2491172937392-YapJAJkYcZ96IOFocfQ2ljHA"
#sending a message
def send_message():
    message = making_message()
    print(message)
    post_message(SLACK_BOT_TOKEN, "#project-neo" ,message) #to send


send_message()