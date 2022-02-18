"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Любишь печенье": "Да, люблю!", "Мама порола?": "Нет, не порола"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input('Задайте вопрос: ')
        if user_say in answers_dict.keys():
            print(answers_dict[user_say])
        else:
            print("Нет такого вопроса {}".format(user_say))

if __name__ == "__main__":
    ask_user(questions_and_answers)
