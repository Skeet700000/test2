from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import get_pictures
login, password = "89581779173","700000pam2"
vk_session = vk_api.VkApi(token="b1d6094d3c8cd58620946a28eafe67429c84ecc58ad8e9dc9a447396f67f039001aedab6c83be993c6886")

# token = "ЗдесьЕстьВашТокен"
# vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "1":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
                elif response == "2":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Пока, друг!', 'random_id': 0})
                elif response == "котики":
                    attachment = get_pictures.get(vk_session,-130670107,session_api)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи котиков!', 'random_id': 0, "attachment": attachment})
