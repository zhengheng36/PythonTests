

b = 1
for a in range(200, 1000000):
    b = 1
    while True:
        if b == a:
            break
        b = b + 1
        k = 1000*(a + b) - a * b
        if k == 500000:
            break
    if k == 500000:
        break

        
print(a)
print(b)
print(a*a + b*b)
