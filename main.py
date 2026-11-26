
try:
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    result = a / b
    print("Результат:", result)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")


try:
    x = int(input("\nЗадание 2. Введи число для деления 10/x: "))
    res = 10 / x
    print("Результат:", res)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print("Всё прошло хорошо.")
finally:
    print("Программа завершена.\n")


with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Пока\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
print(lines)
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))


with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Ещё одна строка\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())


class Hero:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def to_line(self):
        return f"{self.name};{self.level};{self.hp}"

def hero_from_line(line):
    name, level, hp = line.strip().split(";")
    return Hero(name, int(level), int(hp))

def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")

def load_from_file(filename):
    heroes = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                heroes.append(hero_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return heroes

heroes = [
    Hero("Артас", 60, 2500),
    Hero("Сильвана", 78, 1800),
    Hero("Джайна", 45, 1200)
]
save_to_file(heroes, "data.txt")

heroes = []  
loaded = load_from_file("data.txt")
for h in loaded:
    print(f"Герой: {h.name}, уровень {h.level}, здоровье {h.hp}")