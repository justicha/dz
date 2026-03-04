#Взвешенное интервальное планирование
intervals = [(0, 3, 3), (0, 2, 2), (3, 5, 4), (4, 7, 2), (0, 1, 3)]

def f(n):
    start_number = {}
    c = 0
    
    for i in n:
        start = i[0]
        dlina = i[1] - i[0]
        
        if start not in start_number or dlina < start_number[start][1] - start_number[start][0]:
            start_number[start] = i
    
    info = list(start_number.values())
    print(info)

    for i in info:
        c += i[2]
    
    return f"максимальный вес = {c}"

f(intervals)
