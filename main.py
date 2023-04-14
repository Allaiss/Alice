# import time
# start_time = time.time()
arr = input().split(' ')
# arr = ['2', '3', '1', '1', '4']
j = 0
# print(arr)
for i in range(len(arr)):
    if arr[i] == '':
        arr.pop(i)
        j += 1
    if j != 0:
        arr[i-j] = int(arr[i-j])
    else:
        arr[i] = int(arr[i])


i = 0
j = 0
while(True):
    if arr[i] <= 0:
        j = 0
        break

    else:
        i += arr[i]
        j += 1

    if i > len(arr):
        break
    # print(arr[i])
    if i == len(arr):
        if i >= len(arr):
            break
        elif arr[i] != 0:
            break

if j == 0: print(f'\n{False}')
else: print(f'\n{True}')

# print("--- %s seconds ---" % (time.time() - start_time))

