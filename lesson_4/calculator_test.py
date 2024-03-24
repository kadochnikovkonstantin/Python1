# import pytest
# from calculator import Calculator

# calculator = Calculator()

# def test_sum_positive_nums():
#     calculator = Calculator()
#     res = calculator.sum(4, 5)
#     assert res == 9

# def test_sum_negative_nums(): #поменяли название теста
#     calculator = Calculator()
#     res = calculator.sum(-6, -10) #поменяли параметры
#     assert res == -16 #заменили число на ошибочное

# def test_sum_positive_and_negative_nums(): #поменяли название теста
#     calculator = Calculator()
#     res = calculator.sum(-6, 6) #поменяли параметры
#     assert res == 0 #поменяли ожидаемую сумму

# from calculator import Calculator 

# calculator = Calculator()

# @pytest.mark.skip(reason="починить тест позже")
# def test_sum_positive_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(4, 5)
#     assert res == 9

# def test_sum_negative_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(-6, -10)
#     assert res == -16

# def test_sum_positive_and_negative_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(-6, 6)
#     assert res == 0

# def test_sum_float_nums(): #проверка сложения десятичных дробей
#     calculator = Calculator()
#     res = calculator.sum(5.6, 4.3)
#     res = round(res, 1)  
#     assert res == 9.9

# def test_sum_zero_nums(): #проверка сложения целого числа и нуля
#     calculator = Calculator()
#     res = calculator.sum(10, 0)
#     assert res == 10

# def test_div_positive(): #проверка деления чисел
#     calculator = Calculator()
#     res = calculator.div(10, 2)
#     assert res == 5

# def test_div_by_zero(): #проверка деления на ноль
#     calculator = Calculator()
#     with pytest.raises(ArithmeticError):
#             res = calculator.div(10, 0)
 

# def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
#     calculator = Calculator()
#     numbers = []
#     res = calculator.avg(numbers)
#     assert res == 0

# def test_avg_positive(): #проверка нахождения среднего для списка
#     calculator = Calculator()
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
#     res = calculator.avg(numbers)
#     assert res == 5

#res = calculator.sum(4, 5)
#assert res == 9

#res = calculator.sum(-6, -10)
#assert res == -16

#res = calculator.sum(-6, 6)
#assert res == 0

#res = calculator.sum(5.6, 4.3) #Python посчитает сумму
#res = round(res, 1) #округлит ее до одного знака после запятой
#print(res) #напечатает сумму
#assert res == 9.9 #сравнит с предполагаемым значением

#res = calculator.sum(10, 0)
#assert res == 10

#res = calculator.div(10, 2)
#assert res == 5

#res = calculator.div(10, 0)
#assert res == None

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
#res = calculator.avg(numbers)
#print(res)
#assert res == 5