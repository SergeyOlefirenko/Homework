
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

    def get_title(self):
        return self.__title

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

#Создаем метод Save для сохранение и перезаписи объектов класса person
#Сoздаем метод Add для добавления записи о студентах и учителях в файл

#Метод позволяет записать в файл объект класса
    def save(self):
        import sys
        person_stdout = sys.stdout
        with open('people.txt', mode='a', encoding='utf-8') as file:
            sys.stdout = file
            print(teacher)
            print(student)
            sys.stdout = person_stdout

    def add(self):
        with open('people.txt', mode='a', encoding='utf-8') as file:
            file.write(self.__str__() + '\n')

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

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

student = Student('Михаил', 'Самохвалов', '+380501232323,', 'Студент,', 'ПГС-21')

class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, title: str, subject: str):
        super().__init__(firstname, lastname, phone, title)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

teacher = Teacher('Василий', 'Пупкин', '+380501111111,','Преподаватель,','Химия')


person.save()

#Добавляем весь список студентов в файл при такой необходимости

studentList = []

studentList.append(Student('Вася', 'Котов', '+380501234567', 'Student', 'Python11'))
studentList.append(Student('Коля', 'Николаев', '+387415874165', 'Student', 'Python21'))
studentList.append(Student('Анна', 'Чечушкова', '+44784512358', 'Student', 'C++14'))
studentList.append(Student('Светлана', 'Лобода', '+380671111111','Student', 'Python11'))
studentList.append(Student('Михаил', 'Федоров', '+99123475611', 'Student','C++17'))

for i in studentList:
    i.add()

#Добавляем весь список учителей в файл при такой необходимости

teacherList = []

teacherList.append(Teacher('Николай', 'Котовасин', '+380501234567', 'Teacher', 'Python11'))
teacherList.append(Teacher('Максим', 'Чечушков', '+387415874165', 'Teacher', 'Python21'))
teacherList.append(Teacher('Алевтина', 'Чечушкова', '+44784512358', 'Teacher', 'C++14'))
teacherList.append(Teacher('Инна', 'Мороз', '+380671234567', 'Teacher', 'Python11'))
teacherList.append(Teacher('Алексей', 'Семихвостов', '+99123475611', 'Teacher', 'C++17'))

for i in teacherList:
    i.add()
person.load()
#Добавляем студентов и учителей в файл по отдельности

studentList[0].add()
studentList[1].add()
studentList[2].add()
studentList[3].add()
studentList[4].add()
teacherList[0].add()
teacherList[1].add()
teacherList[2].add()
teacherList[3].add()
teacherList[4].add()

import json

studentGroup = {
    'Name': student.get_firstname(),
    'Lastname': student.get_lastname(),
    'Phone number': student.get_phone(),
    'Title': student.get_title(),
    'Group': student.get_group()
}
teacherGroup = {
'Name': teacher.get_firstname(),
    'Lastname': teacher.get_lastname(),
    'Phone number': teacher.get_phone(),
    'Title': teacher.get_title(),
    'Subject': teacher.get_subject()
}
Group ={
    'Students': studentGroup,
    'Teachers': teacherGroup
}

with open('serialize.txt', mode='w', encoding='UTF-8') as file:
     json.dump(Group, file, indent = 4)

with open('serialize.txt', mode='r', encoding='UTF-8') as file:
    deserialize = json.load(file)
    print(deserialize)

p = Person
#Данное действие позволяет записать данные из списка в файл, создав, при этом словарь, а также дописать данные
for p in studentList:
    import sys
    person_stdout = sys.stdout
    with open('serialize.txt', mode='a', encoding='utf-8') as file:
        json_string = json.dumps(p.__dict__, indent=4)
        sys.stdout = file
        print(json_string)
        sys.stdout = person_stdout
#Строки десериализирует если раскомментировать но получить декодированные данные из самого файла не получается
    Person = json.loads(json_string)
    print(Person)

#Данное действие позволяет записать данные из списка в файл, создав, при этом словарь, а также дописать данные
for p in teacherList:
    import sys
    person_stdout = sys.stdout
    with open('serialize.txt', mode='a', encoding='utf-8') as file:
        json_string = json.dumps(p.__dict__, indent=4)
        sys.stdout = file
        print(json_string)
        sys.stdout = person_stdout
# Строки десериализирует если раскомментировать но получить декодированные данные из самого файла не получается
    Person = json.loads(json_string)
    print(Person)

# Не получается десериализировать данные из файла, (load) тоже не работает
# Пока нет понимания как декодировать TextIOWrapper в строку
# with open('serialize.txt', mode='r', encoding='UTF-8') as file:
#     deserialize = json.loads(file)
#     print(deserialize)

# Если раскомментировать - считывает строки из файла в одну строку без декодирования...
# import json
# with open('serialize.txt', 'r') as f:
#     json_str = json.dumps(f.readlines())
# print(json_str)


