a = list(map(int, input().split()))
key = int(input())

f = False

for i in range(len(a)):
    if a[i] == key:
        print("Found at index", i)
        f = True
        break

if not f:
    print("Not Found")
