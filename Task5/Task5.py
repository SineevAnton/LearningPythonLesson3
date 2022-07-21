# Enter a number. Create the Fibonnachi sequence, including negative indexes.

# F−n = (−1)n+1Fn.

def fibonnachi(numsCount):
    if numsCount in [1,2]:
        return 1
    else:
        return fibonnachi(numsCount - 1) + fibonnachi(numsCount -2)

fibList = [0]
for i in range(1, int(input('Please enter number: ')) + 1):
    currentNum = fibonnachi(i)
    fibList.append(currentNum)
    if i % 2 == 0:
        fibList.insert(0, -currentNum)
    else:
        fibList.insert(0, currentNum)

print(fibList)