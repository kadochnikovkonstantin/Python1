def bank(X, Y): 
    
    for i in range(Y):

        X*=1.1

    return X
#print(bank(10,2))
X = float(input("Введите начальную сумму вклада: "))
Y = int(input("Введите срок вклада в годах: "))
result = bank(X, Y)
print("Итоговая сумма на вкладе: ", result)