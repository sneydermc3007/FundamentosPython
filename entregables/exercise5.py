a, b = 0, 1

arrayFibo = [a, b]

for i in range(b, 100):
    a = arrayFibo[i-1]
    b = arrayFibo[i] + a
    arrayFibo.append(b)

    if(b >= 1597):
        break

print(f"Esta es la seria fibonacci: {arrayFibo}")