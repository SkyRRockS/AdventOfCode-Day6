INPUT_S = '''\
4,1,3,2,4,3,1,4,4,1,2,1,1,1,1,4,1,1,1,2,2,1,3,1,3,1,3,4,5,1,2,2,1,1,1,3,4,4,3,1,1,3,5,3,1,1,5,2,4,1,1,3,5,1,4,3,1,1,4,2,1,1,1,1,1,1,3,1,1,1,1,1,4,5,1,2,5,3,1,1,3,1,1,1,1,5,1,2,5,1,1,1,1,1,1,3,5,1,3,2,1,1,1,1,1,1,1,4,5,1,1,3,1,5,1,1,1,1,3,3,1,1,1,4,4,1,1,4,1,2,1,4,4,1,1,3,4,3,5,4,1,1,4,1,3,1,1,5,5,1,2,1,2,1,2,3,1,1,3,1,1,2,1,1,3,4,3,1,1,3,3,5,1,2,1,4,1,1,2,1,3,1,1,1,1,1,1,1,4,5,5,1,1,1,4,1,1,1,2,1,2,1,3,1,3,1,1,1,1,1,1,1,5'''


datas = {}

numbers = [int(x) for x in INPUT_S.split(',')]

print(numbers)

for i in range(max(9,max(numbers))) :
    datas[i] = 0
for x in numbers :
    datas[x] += 1

for i in range(80) :
    zero = datas[0]
    datas[0] = 0
    for index in range(1, len(datas)) :
        datas[index - 1] += datas[index]
        datas[index] = 0
    datas[6] += zero
    datas[8] += zero

res = 0

for i in datas :
    res += datas[i]

print("Res is : ",res)
