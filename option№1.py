def print_less_then_38(arr) -> None: #Функция ничего не возвращает
   
    less_then_38 = [] # пустой массив
    for raw_item in arr: # перебераем элементы в arr
        if isinstance(raw_item, int): # возвращаем True, если raw_item является типом int
            if raw_item < 38: # проверяем условие 
                less_then_38.append(raw_item) # и если все условия True, добовляем в массив raw_item
        elif isinstance(raw_item, str): # возвращаем True, если raw_item является типом str
            item = int(raw_item) # приводим raw_item к типу int
            if item < 38:# проверяем условие 
                less_then_38.append(item) # и если все условия True, добовляем в массив raw_item
        elif isinstance(raw_item, list): # возвращаем True, если raw_item является типом list
            for list_item in raw_item: перебераем элементы в raw_item
                if list_item < 38: # проверяем условие 
                    less_then_38.append(list_item) # и если все условия True, добовляем в массив raw_item
    print(", ".join(str(x) for x in less_then_38)) # используем (", ".join) чтобы между строками стоял разделитель, затем перебераем каждый элемент
    
a = [1, 2, 3, 45, "7", [12, 45, 1], 23, "56"]
print_less_then_38(a)
 
