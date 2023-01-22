# TODO Написать 3 класса с документацией и аннотацией типов
from datetime import datetime
from typing import List


class user:
    """
     Создание и подготовка к работе класса "user"
    """

    def __init__(self, first_name: str, last_name: str, login: str, last_visit: datetime, premium_status: bool, friends=None):
        if friends is None:
            friends = []
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.last_visit = last_visit
        self.premium_status = premium_status
        self.friends = friends

    def add_new_friend(self, friend) -> None:
        """
        Добавление нового друга в список
        :param friend:  User friend
        :return: None
        """
        self.friends.append(friend)

    def delete_friend_by_login(self, login: str) -> None:
        """
        Удаление друга из списка друзей по логину
        :param login: login name str
        :return: None
        """
        delete_index = None
        for index, friend in enumerate(self.friends):
            if friend.login == login:
                delete_index = index
        if delete_index:
            self.friends.pop(delete_index)

    def set_login(self, login: str) -> None:
        """
        Установка нового логина
        >>> user = User("Aleksandr", "Savinskiy", "piter78", datetime.now(), False)
        >>> user.login
        "piter78"
        >>> user.set_login("piter78")
        >>> user.login
        piter78
        :param login: new login
        :return: None
        """
        self.login = login


class Chat:
    """
    Создание и подготовка к работе класса "Сhat"
    """

    def __init__(self, name: str, admin: user, mute_notification: bool, members: List[user]):
        self.name = name
        self.admin = admin
        self.mute_notification = mute_notification
        self.members = members

    def get_chat_name(self) -> str:
        """
        Именование чата
        :return: str (chat name)
        """
        return self.name

    def set_chat_name(self, name) -> None:
        """
        :param name: new chat name
        :return: None
        """
        self.name = name

    def change_chat_mute_notification_status(self) -> None:
        """
        Изменение уведомлений чата
        :return: None
        """
        self.mute_notification = not self.mute_notification


class Message:
    """
    Создание и подготовка к работе класса "Message"
    """

    def __init__(self, sender: user, message_content: str, send_time: datetime, chat: Chat, read_status: bool):
        self.sender = sender
        self.message_content = message_content
        self.send_time = send_time
        self.chat = chat
        self.read_status = read_status

    def change_read_status(self) -> None:
        """
        Изменение статуса сообщения
        :return: None
        """
        self.read_status = not self.read_status

    def get_message_content(self) -> str:
        """
        Получение содержания сообщения
        :return: str
        """
        return self.message_content

    def refactor_message_content(self, content: str) -> None:
        """
        :param content: message content
        :return: None
        """
        self.message_content = content


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
