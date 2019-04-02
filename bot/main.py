from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
imporpi()
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
