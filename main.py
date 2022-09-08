#Дописать приложение, Необходимо добавить возможность хранения в одном списке/файле
# студентов и прподавателей.
# Обратить внимание на методы чтения/записи в файл.

#Создаем класс Person

class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()
    __title = str()

    def __init__(self, firstname: str, lastname: str, phone: str, title: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)
        self.set_title(title)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_title(self, title: str):
        self.__title = title

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone} {self.__title}'

#Создаем метод Save и сохраняем в файл объект класса person

    def save(self):
        import sys
        person_stdout = sys.stdout
        with open('people.txt', mode='a', encoding='utf-8') as file:
            sys.stdout = file
            print(teacher)
        with open('people.txt', mode='a', encoding='utf-8') as file:
            sys.stdout = file
            print(student)
            sys.stdout = person_stdout

    def load(self):
        reader = open('people.txt', mode='r', encoding='UTF-8')
        text = reader.read()
        print(text)
        reader.close()
person = Person('Имя', 'Фамилия','Номер телефона', 'Должность')

#Создаем 2 класса Student и Teacher

class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, title: str, group: str):
        super().__init__(firstname, lastname, phone, title)
        self.set_group(group)

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def to_file(self, filename: str):
        with open(filename, mode='a', encoding='utf-8') as file:
            file.write(self.__str__() + '\n')

    def from_file(self, filename: str):
        with open(filename, mode='r', encoding='utf-8') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_title(res[3])
            self.set_group(res[4])

    def __str__(self):
        return f'{super().__str__()} {self.__group}'


student = Student('Михаил', 'Самохвалов', '+380501232323,', 'Студент -', 'ПГС-21')

class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, title: str, subject: str):
        super().__init__(firstname, lastname, phone, title)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def to_file(self, filename: str):
        with open(filename, mode='a', encoding='utf-8') as file:
            file.write(self.__str__() + '\n')

    def from_file(self, filename: str):
        with open(filename, mode='r', encoding='utf-8') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_title(res[3])
            self.set_subject(res[4])

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

teacher = Teacher('Василий', 'Пупкин', '+380501111111,','Преподаватель -','Химия')
person.save()
# person.load()

studentList = []
studentList.append('Ivasyk Bulkin trinolyatrulyalya Студент Python11')
studentList.append('Grigoiy Terkin +387415874165 Студент Python21')
studentList.append('Anna Chechetkina +04478451235 Студент C++14')
studentList.append('Svetlana Bulkina trinolyatrulyalya2 Студент Python11')
studentList.append('Anatloiy Fedorov 0991234756 Студент C++17')
def add():
    import sys
    person_stdout = sys.stdout
    with open('people.txt', mode='a', encoding='utf-8') as file:
        sys.stdout = file
        for i in studentList:
            print(i)
        sys.stdout = person_stdout
add()
# person.load()

studList = []

studList.append(Student('Вася', 'Котов', '+380501234567', 'Student', 'Python11'))
studList.append(Student('Коля', 'Николаев', '+387415874165', 'Student', 'Python21'))
studList.append(Student('Анна', 'Чечушкова', '+44784512358', 'Student', 'C++14'))
studList.append(Student('Светлана', 'Лобода', '+380671111111','Student', 'Python11'))
studList.append(Student('Михаил', 'Федоров', '+99123475611', 'Student','C++17'))

for i in studList:
    i.to_file('people.txt')

teacherList = []

teacherList.append(Teacher('Николай', 'Котовасин', '+380501234567', 'Teacher', 'Python11'))
teacherList.append(Teacher('Максим', 'Чечушков', '+387415874165', 'Teacher', 'Python21'))
teacherList.append(Teacher('Алевтина', 'Чечушкова', '+44784512358', 'Teacher', 'C++14'))
teacherList.append(Teacher('Инна', 'Мороз', '+380671234567', 'Teacher', 'Python11'))
teacherList.append(Teacher('Алексей', 'Семихвостов', '+99123475611', 'Teacher', 'C++17'))

for i in teacherList:
    i.to_file('people.txt')
person.load()
#     print(i)
# studList[0].to_file('people.txt') # Не работает. Если вводить studList[0][1][2][3][4]-выдает ошибку
# studList[0].from_file('people.txt')# Не работает. Если вводить studList[0][1][2][3][4]-выдает ошибку
student.from_file('people.txt') #Не работает либо работает но я не понимаю как
teacher.from_file('people.txt') #Не работает либо работает но я не понимаю как

# def decorator(funk):
#     def add():
#         import sys
#         person_stdout = sys.stdout
#         with open('people.txt', mode='a', encoding='utf-8') as file:
#             sys.stdout = file
#             for i in studentList:
#                 print(i)
#             sys.stdout = person_stdout
#         funk()
#     return add()
#
# def save():
#     person.save()
#     # person.load()
# dec_funktion = decorator(save)




