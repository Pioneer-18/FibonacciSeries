s = int(input("Numbers in Fibonacci Series: "))
first,second= 0, 1
print(first, second, end=' ')    # intial numbers
i = 0
while (i < s-2):
    next= first + second
    print(next, end=' ')
    first = second
    second = next
    i = i + 1