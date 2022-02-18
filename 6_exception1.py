"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    """
    Замените pass на ваш код
    """
    try:
        while True:
        # try:
            hello = input("Как дела?: ").strip().lower()

            if hello.strip().lower() == "Хорошо".lower():
                print("Хорошо")
                break
            else:
                print("Вы неправильно ответили: {}".format(hello))

    except KeyboardInterrupt:
        print("\nПока")

if __name__ == "__main__":
    hello_user()
