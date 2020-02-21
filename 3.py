# task1
class Student:
    __id = 0

    def __init__(self, firstName: str, secondName: str, name: str, birthday: str, adress: str, phone: str, facult: str,
                 course: int, group: int):
        self.__student = {
            "firstName": firstName,
            "secondName": secondName,
            "name": name,
            "birthday": birthday,
            "adress": adress,
            "phone": phone,
            "facult": facult,
            "course": course,
            "group": group,
        }
        print("Студент создан")
        self.__student["id"] = self.__class__.__id
        self.__class__.__id += 1

    def __del__(self):
        print("Студент уничтожен")
    def setName(self,name:str):
        if type(name) == str and len(name)>1:
            self.__student["name"] = name

    def getName(self):
        return self.__student["name"]

    def getGroup(self):
        return self.__student["group"]

    def getFacult(self):
        return self.__student["facult"]

    def getAge(self):
        '''function returns age'''
        lst = self.__student["birthday"].split(".")
        lst = [int(x) for x in lst]
        dt = datetime.datetime(lst[2], lst[1], lst[0])
        now = datetime.datetime.now()
        return ((now - dt).days // 365)

    def showInfo(self):
        '''function shows information'''
        for i, item in self.__student.items():
            print(str(i) + ': ' + str(item))

collection = [
    Student("Колесникович", "Александрович", "Вова", "12.12.1999", "ул.Белорусская", "+375297441171", "FIT", 2, 5),
    Student("Новик", "Александрович", "Дима", "12.12.1909", "ул.Белорусская", "+3752973453345", "FIT", 3, 4),
    Student("Петров", "Владимирович", "Гена", "12.12.1999", "ул.Белорусская", "+375297333171", "FIT", 2, 5),
    Student("Петров", "Владимирович", "Олег", "12.12.1999", "ул.Белорусская", "+375297333171", "PIM", 2, 5),
    Student("Петров", "Владимирович", "Юра", "12.12.1999", "ул.Белорусская", "+375297333171", "PIM", 2, 4),
]
n = int(input("Insert n:\n"))
query1 = [x for x in collection if x.getGroup() == n]
for i in query1:
    print(i.getName())
f = input("Введите факультет(FIT ли PIM):\n")
query2 = [x for x in collection if x.getFacult() == f]
for i in query2:
    print(i.getName())


# task2
class Stem:  # стебель
    def __init__(self, height: int):
        self.height = height


class Flower:  # цветок
    name = ""

    def __init__(self, height: int):
        self.stem = Stem(height)


class Rose(Flower):  # роза
    name = "Роза"


class Chrysanthemum(Flower):  # хризантема
    name = "Хризантема"


class Bouquet:  # букет

    def __init__(self):
        self.__bouquet = []

    def add(self, flower: Flower):  # добавляю в букет цветок
        self.__bouquet.append(flower)

    def __iter__(self):
        for i in self.__bouquet:
            yield i

    def __len__(self):
        return len(self.__bouquet)


f1 = Rose(5)
f2 = Chrysanthemum(10)
f3 = Rose(11)
f4 = Chrysanthemum(3)
bouquet = Bouquet()
bouquet.add(f1)
bouquet.add(f2)
bouquet.add(f3)
bouquet.add(f4)
for i in bouquet:
    print(i.name, i.stem.height)