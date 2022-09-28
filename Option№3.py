from typing import Any, List, Union

def get_numeric_elements(arr: List[Union[str, int, List[int]]]) -> List[int]: #-> List[int] означает, что функция должна возвращать список целых чисел
                                                                              # с помощью аннотации List[Union[...]] мы указываем, что будем работать со списком который будет содержать целые числоа, строки и список с целыми числами
    
    numeric_elements = [] # пустой массив
    for elem in arr: #  перебераем элементы в arr
        if isinstance(elem, int): # возвращаем True, если raw_item является типом int
            numeric_elements.append(elem) # если все услове True, добовляем в массив raw_item
        if isinstance(elem, str): # возвращаем True, если raw_item является типом str
            try: # запускаем проверку
                numeric_elements.append(int(elem)) # если элемент который мы хотим добавить в numeric_elements не являеться целым числом
            except ValueError: # сработает исключение 
                print("Неверный формат строки '{}' (допустимы только числа)".format(elem)) # format() форматирует указанные значения и вставляет их внутрь строки-заполнителя '{}'
                continue # как итог мы не будем добовлять elem в список  numeric_elements
        elif isinstance(elem, list): # возвращаем True, если raw_item является типом list
            numeric_elements.extend(get_numeric_elements(elem)) # запускаеться рекурсия , тем самым мы проверим каждый список и возможные списки в списке
    return numeric_elements # вернем функции get_numeric_elements список numeric_elements
 
 
def print_less_then_38(arr: List[Union[str, int, List[int]]]): # с помощью аннотации Union мы указываем, что будем работать со списком который будет содержать целые числоа, строки и список с целыми числами
    matches = [item for item in get_numeric_elements(arr) if item < 38] # добавляем список в котором переберием элементы списка полученного с помощью get_numeric_elements(arr) и проверяем на условие 
    print(", ".join(str(x) for x in matches))
    
a = [1, 2, 3, 45, "7", [12, 45, 1], 23, "56"]
print_less_then_38(a)    
