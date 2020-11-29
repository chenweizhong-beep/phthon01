'''
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
'''
import yaml


class Animal():
    name: str = "zoo"
    color: str = "black"
    age: int = 0
    sex: str = "公"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def shout(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.color}的{self.sex}{self.name}会跑")


class Cat(Animal):
    pelage: str = ""

    def __init__(self, pelage, name, color, age, sex):
        self.pelage = pelage
        super().__init__(name, color, age, sex)

    def introduce(self):
        print(f"Hi,我的名字叫{self.name}，"
              f"一只{self.color}的猫，"
              f"今年{self.age}岁了，"
              f"一只{self.sex}猫，"
              f"一只{self.pelage}猫。")

    def shout(self):
        print(f"{self.name}喵喵叫")

    def catch_mouse(self):
        print(f"{self.name}抓老鼠")


class Dog(Animal):
    pelage: str = ""

    def __init__(self, pelage, name, color, age, sex):
        self.pelage = pelage
        super().__init__(name, color, age, sex)

    def introduce(self):
        print(f"Hi,我的名字叫{self.name},"
              f"一只{self.color}的狗，"
              f"今年{self.age}岁了，"
              f"一只{self.sex}狗，"
              f"一只{self.pelage}狗。")

    def shout(self):
        print(f"{self.color}的{self.name}汪汪叫")

    def watch_house(self):
        print(f"{self.name}看家")


if __name__ == '__main__':
    with open(yaml.safe_load('data.yml'), encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        # print(datas)
        pelage = datas['deafult']['pelage']
        name = datas['deafult']['name']
        color = datas['deafult']['color']
        age = datas['deafult']['age']
        sex = datas['deafult']['sex']
        pelage1 = datas['deafult']['pelage1']
        name1 = datas['deafult']['name1']
        color1 = datas['deafult']['color1']
        age1 = datas['deafult']['age1']
        sex1 = datas['deafult']['sex1']

    cat = Cat(pelage, name, color, age, sex)
    cat.introduce()
    cat.run()
    cat.shout()
    cat.catch_mouse()
    print()
    dog = Dog(pelage1, name1, color1, age1, sex1)
    dog.introduce()
    dog.run()
    dog.shout()
    dog.watch_house()
