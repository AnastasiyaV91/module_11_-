def introspection_info(obj):
    info = {}
    info["type"] = type(obj).__name__           # Добавляем в словарь тип объекта
    info["attributes"] = dir(obj)               # Добавляем в словарь атрибуты объекта
    info["methods"] = [method for method in dir(obj) if callable(getattr(obj, method))]  # Добавляем в словарь
                                                                                         # вызываемые атрибуты
    if isinstance(obj, str):                    # Если obj является строкой, то
        info["len"] = len(obj)                  # записываем в значение словаря "длинна строки"
    if isinstance(obj, list):                   # Если obj является списком, то
        info["len"] = len(obj)                  # записываем в значение словаря "длинна списка"
    info["module"] = type(obj).__module__       # Добавляем в словарь информацию кому принадлежит объект
    return info

class My_Class:                                 # Класс для примера
    def __init__(self, number):
        self.number = number
    def my_method(self):
        print(self.number)


number_info = introspection_info(42)
print(number_info)
obj = My_Class(42)
obj_info = introspection_info(obj)
print(obj_info)