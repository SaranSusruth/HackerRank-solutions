ld=0
ar = []
n = int(input("enter no of rows in array:"))
for i in range(n):
    row = list(map(int, input().split()))
    ar.append(row)
for i in range(n):
    ld = ld +ar[i][i]
print(ld)