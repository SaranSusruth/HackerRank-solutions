ld = 0
rd = 0
<<<<<<< HEAD
arr = []
n = int(input("enter no of rows in array:"))
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    ld = ld + arr[i][i]
for i in range(n):
    rd = rd + arr[i][(n-1)-i]
=======
ar = []
n = int(input("enter no of rows in array:"))
for i in range(n):
    row = list(map(int, input().split()))
    ar.append(row)
for i in range(n):
    ld = ld + ar[i][i]
for i in range(n):
    rd = rd + ar[i][(n-1)-i]
>>>>>>> 29b76267eea3584586d9991fe47f680a2c723e1c
diff = ld - rd
print(diff)