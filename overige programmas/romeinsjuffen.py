import math

nummers = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
nummerwoorden = [
    "een ",
    "vijf ",
    "tien ",
    "vijftig ",
    "honderd ",
    "vijfhonderd ",
    "duizend ",
    "vijfduizend ",
    "tienduizend ",
    "vijftigduizend ",
    "honderdduizend ",
    "vijfhonderdduizend ",
    "miljoen ",
]

nums = [0, 0]
numsoud = []
n = int(input())


def uitschrijven(num):
    numlist = []
    numwoord = []
    snum = str(num)
    for num in snum:
        numlist = [i * 10 for i in numlist]
        numlist.append(int(num))
    for item in numlist:
        stem = str(item)[0]
        if stem == "1":
            numwoord.append(nummerwoorden[nummers.index(item)])
        elif stem == "2":
            numwoord.append(2 * nummerwoorden[nummers.index(item / 2)])
        elif stem == "3":
            numwoord.append(3 * nummerwoorden[nummers.index(item / 3)])
        elif stem == "4":
            numwoord.append(
                nummerwoorden[nummers.index(item / 4)]
                + nummerwoorden[nummers.index(item / 4) + 1]
            )
        elif stem == "5":
            numwoord.append(nummerwoorden[nummers.index(item)])
        elif stem == "6":
            numwoord.append(
                nummerwoorden[nummers.index(item / 6) + 1]
                + nummerwoorden[nummers.index(item / 6)]
            )
        elif stem == "7":
            numwoord.append(
                nummerwoorden[nummers.index(item / 7) + 1]
                + 2 * nummerwoorden[nummers.index(item / 7)]
            )
        elif stem == "8":
            numwoord.append(
                nummerwoorden[nummers.index(item / 8) + 1]
                + 3 * nummerwoorden[nummers.index(item / 8)]
            )
        elif stem == "9":
            numwoord.append(
                nummerwoorden[nummers.index(item / 9)]
                + nummerwoorden[nummers.index(item / 9) + 2]
            )
    return "".join(numwoord)


def split(word):
    return [char for char in word]


def addnumber(toadd, pos):
    if len(nums) < pos + 2:
        nums.append(0)

    nums[pos] += toadd


def jufcheck(num, pos):
    if num % 7 == 0:
        addnumber(1, pos + 1)
        jufcheck(nums[pos + 1], pos + 1)
    elif "7" in str(num):
        addnumber(1, pos + 1)
        jufcheck(nums[pos + 1], pos + 1)
    elif len(set(split(str(nums[pos])))) <= (len(str(nums[pos]))) / 2:
        addnumber(1, pos + 1)
        jufcheck(nums[pos + 1], pos + 1)
    else:
        return


for i in range(1, n + 1):
    numsoud = []
    for item in nums:
        numsoud.append(item)
    nums[0] = i
    jufcheck(nums[0], 0)
    if True:
        for j in range(len(numsoud) - 1, -1, -1):
            if nums[j] != numsoud[j]:
                f = nums[j]
                print(nums, nums[j], uitschrijven(nums[j]))
                break

