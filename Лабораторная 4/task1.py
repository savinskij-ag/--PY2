from datetime import datetime
from typing import List

if __name__ == "__main__":
    class SocialNetwork:
          """
          Abstract social network
          """

    def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                 count_of_users: int) -> None:
        self.creators = creators
        self.created_date = created_date
        self.servers = servers
        self.name = name
        self.count_of_users = count_of_users

    def __str__(self) -> str:
        """
        social network string representation
        :return: str
        """
        return f"Social network's name is: {self.name}, " \
               f"Creators: {self.creators}, current number of users: {self.count_of_users}"

    def __repr__(self) -> str:
        """
        social network object representation
        :return: str
        """
        return f"SocialNetwork(name={self.name}, creators={self.creators}, created_date={self.created_date}, " \
               f"Servers={self.servers}, count_of_users={self.count_of_users})"

    def add_new_user(self) -> None:
        """
        Add new user to network
        :return: None
        """
        self.count_of_users += 1

    class VK(SocialNetwork):
        """
        VK network
        """

        def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                     count_of_users: int, mail_ru_users: int) -> None:
            super().__init__(name, creators, created_date, servers, count_of_users)
            self.mail_ru_users = mail_ru_users
            self.__secret_data = "SECRET VK DATA"

        def __str__(self) -> str:
            """
            vk string representation
            :return: str
            """
            return f"VK: creators-{self.creators}, VK users-{self.count_of_users}, " \
                   f"Mail users-{self.mail_ru_users}"

        def __iter_through_secret_data(self) -> None:
            """
            Just iter
            Viewing this information should only be available inside the class
            :return: None
            """
            for data in self.__secret_data:
                print(data)

        def add_new_user(self) -> None:
            """
            Registration occurs immediately both in VK and in Mail
            :return: None
            """
            self.count_of_users += 1
            self.mail_ru_users += 1


    class Facebook(SocialNetwork):
        """
        Facebook network
        """

        def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                     count_of_users: int, instagram_users: int) -> None:
            super().__init__(name, creators, created_date, servers, count_of_users)
            self.instagram_users = instagram_users
            self.__secret_data = "SECRET FACEBOOK DATA"

        def __get_users_statistic(self) -> int:
            """
            get Facebook and inst users
            getting statistics only inside the class for Facebook internal algorithms
            :return: int
            """
            return self.count_of_users + self.instagram_users

        def __str__(self) -> str:
            """
            facebook string representation
            :return: str
            """
            return f"Facebook: creators-{self.creators}, facebook users-{self.count_of_users}, " \
                   f"Instagram users-{self.instagram_users}"

        def add_new_user(self) -> None:
            """
            Registration takes place immediately on both Facebook and Instagram
            :return: None
            """
            self.count_of_users += 1
            self.instagram_users += 1

    pass
