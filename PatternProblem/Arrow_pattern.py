n = int(input())
i = 1
k = 1
n1= (n+1)/2
n2= n1-1
while i <= n1:
    j = 1
    spaces = 1
    while spaces < i:
        print(' ', end = "")
        spaces = spaces + 1
    while j <= i :
        print('*'+" ", end = "")
        j = j + 1
    print()
    i = i + 1
while k <= n2:
    j = 1
    spaces = 1
    while spaces <= n2-k:
        print(' ', end = "")
        spaces = spaces + 1
    while j <= n2 - k +1 :
        print('*'+" ", end = "")
        j = j + 1
    print()
    k = k + 1