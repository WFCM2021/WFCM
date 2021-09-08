import requests

def post_message(token, channel, text):
    response=requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

myToken = "xoxb-1610685610342-2019607257925-wq5VcryqFQKyhdEQwuuj6voz"

post_message(myToken,"#project-neo","Hello comrades")