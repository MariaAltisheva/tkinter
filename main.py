import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Авторизация')
        self.dict_of_data = {}

        # создаю рамки
        self.login_frame = tkinter.Frame(self.main_window)
        self.password_frame = tkinter.Frame(self.main_window)

        # создаю виджеты
        self.login_label = tkinter.Label(self.login_frame, text='Логин: ')
        self.login_entry = tkinter.Entry(self.login_frame, width=10)

        self.login_label.pack(side='left')
        self.login_entry.pack(side='left')



        # упаковка виджетов логина
        self.password_label = tkinter.Label(self.password_frame, text='Пароль: ')
        self.password_entry = tkinter.Entry(self.password_frame, width=10)
        self.password_label.pack(side='left')
        self.password_entry.pack(side='left')

        # Сделаем кнопочку
        self.registration = tkinter.Button(self.main_window, text='Регистрация', command=self.registration)
        self.authorise = tkinter.Button(self.main_window, text='Авторизация', command=self.autorization)
        self.exit = tkinter.Button(self.main_window, text='Выйти', command=self.main_window.destroy)

        self.registration.pack(side='bottom')
        self.authorise.pack(side='bottom')
        self.exit.pack(side='bottom')


        # упаковка рамок
        self.login_frame.pack()
        self.password_frame.pack()

        tkinter.mainloop()

    def registration(self, ):
        # получает логин и пароль, сохраняет их в словарь

        self.login = str(self.login_entry.get())
        self.password = str(self.password_entry.get())

        self.dict_of_data.update({"login": self.login, "password": self.password})

        return tkinter.messagebox.showinfo('Все прошло успешно', 'Вы зарегистрированы')

    def autorization(self, ):
        self.login = str(self.login_entry.get())
        self.password = str(self.password_entry.get())

        if self.login == self.dict_of_data["login"] and self.password == self.dict_of_data["password"]:
            return tkinter.messagebox.showinfo('Все прошло успешно', 'Вы авторизованы')
        else:
            return tkinter.messagebox.showinfo('Ошибка', 'Неверно введен логин или пароль')


if __name__ == '__main__':
    my_gui = MyGUI()
    