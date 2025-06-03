ld = 0
rd = 0
arr = []
n = int(input("enter no of rows in array:"))
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    ld = ld + arr[i][i]
for i in range(n):
    rd = rd + arr[i][(n-1)-i]
diff = ld - rd
print(diff)