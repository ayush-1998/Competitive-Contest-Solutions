from collections  import Counter

n= int(input())
ans = []

for i in range(n):
    d = int(input())

    li= []
    k=0
    r=0
    c=0

    for j in range(d):
        row = list(map(int,input().split()))

        li.append(row)

        dup = [item for item,count in Counter(row).items() if count > 1 ]

        if len(dup) >= 1:
            r+=1


    for numbers in range(len(li)):
        k+=li[numbers][numbers]

    column = []

    new = [num for list_ in li for num in list_]

    for thing in range(d):
        tempList = []
        index = thing

        for a in range(d):
            tempList.append(new[index])
            index+=d

        column.append(tempList)

        duplistC = [item for item,count in Counter(tempList).items() if count > 1]
        if len(duplistC) >= 1:
            c+=1

    tempList2 = []
    tempList2.append(i+1)
    tempList2.append(k)
    tempList2.append(r)
    tempList2.append(c)
    ans.append(tempList2)
for list_ in ans:
    print("Case #{}: {} {} {}".format(list_[0], list_[1], list_[2],list_[3]))