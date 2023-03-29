import os 
from dotenv import load_dotenv
from pathlib import Path
from __main__ import *
import slack
from datetime import datetime
# import bot
x=0
channel_id = "CV81M2N9Z"

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
conversation_history = []

try:
    
    result = client.conversations_history(channel=channel_id)
    conversation_history = result["messages"][x]
    ts = float(conversation_history['ts'])
    time_n = datetime.fromtimestamp(ts).strftime("%d/%m/%Y")
    m = client.users_profile_get(user= conversation_history['user'])['profile']
    # bot.write_on_cell(m,time_n,conversation_history,x)
    x+=1
    alet = datetime.now().strftime("%d/%m/%Y")

    while(alet == time_n):
        conversation_history = result["messages"][x]
        ts = float(conversation_history['ts'])
        time_n = datetime.fromtimestamp(ts).strftime("%d/%m/%Y")
        m = client.users_profile_get(user= conversation_history['user'])['profile']
        x+=1
        # bot.write_on_cell(m,time_n,conversation_history,x)
    

except SlackApiError as e:
   print(e)


 
