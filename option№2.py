from typing import Any, List, Union
 
 
def print_less_then_38(arr: List[Union[List[int], str, int]]) -> None: # с помощью аннотации Union мы указываем, что будем работать со списком который будет содержать целые числоа, строки и список с целыми числами
  
    less_then_38 = [] # пустой массив
    for raw_item in arr: #  перебераем элементы в arr
        if isinstance(raw_item, int): # возвращаем True, если raw_item является типом int
            if raw_item < 38: # проверяем условие
                less_then_38.append(raw_item) # и если все условия True, добовляем в массив raw_item
        elif isinstance(raw_item, str): # возвращаем True, если raw_item является типом str
            try: # сделаем проверку
                item = int(raw_item) # если str мы не можем привети к int , допустим ('текст')
            except ValueError: # будет срабатывать исключение
                print("Неверный формат строки '{}' (допустимы только числа)".format(raw_item)) # и выводиться этот символ 
                continue
            if item < 38: # проверяем условие 
                less_then_38.append(item)  # и если все условия True, добовляем в массив raw_item
        elif isinstance(raw_item, list): # возвращаем True, если raw_item является типом list
            for list_item in raw_item: # перебераем элементы в raw_item
                if list_item < 38: # проверяем условие 
                    less_then_38.append(list_item) # и если все условия True, добовляем в массив raw_item
        else: 
            print("Неподдерживаемый тип значения '{}' - {}".format(raw_item, type(raw_item))) # если же тип значения не подходит , допустим ({ 1 : 2 }), нам будут об этом сообщать 
            # Неподдерживаемый тип значения '{ 1 : 2}' - class 'dist'
    print(", ".join(str(x) for x in less_then_38))  # используем (", ".join) чтобы между строками стоял разделитель, затем перебераем каждый элемент
    
a = [1, 2, 3, 45, "7", [12, 45, 1], 23, "56"]
print_less_then_38(a)
