#Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.


def get_multiplied_digits(number):   #1.Написать функцию get_multiplied_digits и параметр number в ней.
   str_number = str(number)          #2.Создать переменную str_number и записать строковое представление(str) числа number в неё.
   first = int(str_number[0])        #3.создать переменную first и записать в неё первый символ из str_number в числовом представлении(int).
   if int(len(str_number) > 1):      #4.длина str_number больше 1, функция len() возвращает количество элементов в списке.
       return first * get_multiplied_digits(int(str_number[1:]))
                    #5. Возвращаем значение first * get_multiplied_digits(int(str_number[1:])), то есть умножаем
                    # первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
   else:
       return int(str_number)   #6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

result = get_multiplied_digits(40203)
print(result)

