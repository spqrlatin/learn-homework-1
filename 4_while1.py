"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    """
    Замените pass на ваш код
    """

    while True:
        hello = input("Как дела?: ").strip().lower()
        if hello.strip().lower() == "Хорошо".lower():
            print("Хорошо")
            break
        else:
            print("Вы неправильно ответили: {}".format(hello))

    def find_person():

        names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


        while True:
            name = "Валера"
            if list.pop(names):
                print("Валера нашелся!")
                break
            else:
                print("Валеры нет!")

    find_person()


    def get_answer():
        while True:
            user_say = input('Скажите что-нибудь: ')
            if user_say == "Пока":
                print("Ну, пока!")
                break
            else:
                print("Сам ты {}".format(user_say))

    get_answer()


if __name__ == "__main__":
    hello_user()
