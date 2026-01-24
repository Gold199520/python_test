from abc import ABC, abstractmethod


class Employee(ABC):                                                 # АБСТРАКЦИЯ: создание абстрактного класса Employee
    def __init__(self, name: str, position: str, salary: float ):    # ИНКАПСУЛЯЦИЯ: скрытие данных внутри объекта
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'{self.name},{self.position},{self.salary}'


    @abstractmethod
    def calculate_bonus(self):          # Абстрактный метод
        pass


class Developer(Employee):                                          # НАСЛЕДОВАНИЕ: Developer наследует от Employee
    def __init__(self, name: str, salary: float ):
        # Передаем позицию "Developer" родительскому классу
        super().__init__(name, 'Developer', salary)


    # Разработчики получают 10% бонус
    def calculate_bonus(self):                                      # ПОЛИМОРФИЗМ: своя реализация calculate_bonus
        bonus = self.salary * 0.1
        return bonus

class Manager(Employee):                                            # НАСЛЕДОВАНИЕ: Manager наследует от Employee
    def __init__(self, name: str, salary: float ):
        # Передаем позицию "Manager" родительскому классу
        super().__init__(name, 'Manager', salary)


    # Менеджеры получают 10% бонус
    def calculate_bonus(self):                                      # ПОЛИМОРФИЗМ: своя реализация calculate_bonus
        bonus = self.salary * 0.1
        return bonus

# Создаем объекты сотрудников
dev = Developer("Alice", 60000)
mrg = Manager('Bob', 80000)

# Выводим информацию о сотрудниках
print(dev.get_info())
print(mrg.get_info())

# Выводим бонусы сотрудников
print(dev.calculate_bonus())
print(mrg.calculate_bonus())


