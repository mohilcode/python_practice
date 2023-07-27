#Intuitive
n = int(input())
m = {}
a = list(map(int, input().split())) # Assuming you will input n numbers here
target = int(input())

for i in range(n):
    m[a[i]] = i

for i in range(n):
    dif = target - a[i]
    if dif in m and m[dif] != i:
        print(i, m[dif])
        break

#Non-Intuitive
n = int(input())
nums = list(map(int,input().split()))
target = int(input())
num_to_index = {}
for i in range(n):
    num = nums[i]
    if target - num in num_to_index:
        print(num_to_index[target - num], i)
        break
    num_to_index[num] = i
