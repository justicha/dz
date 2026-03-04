#Взвешенное интервальное планирование
intervals = [(0, 3, 3),(6,8,2), (1, 2, 2), (3, 5, 4), (4, 7, 2), (0, 2, 3)]

def f(n):
    a = sorted(n)
    k = 0
    
    result = []
    last_end = -1
    
    for i in a:
        start = i[0]
        end = i[1]
        if start >= last_end:
            result.append(i)
            last_end = end

    for i in result:
        k += i[2]
    
    return f"максимальный вес = {k}"

f(intervals)
