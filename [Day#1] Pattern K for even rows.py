import math

#length = int(input())

def half(sV, reverse = True):
    x = 1 if reverse else -1
    sV2 = sV*int(reverse)
    for i in range(sV+1):
        print("*", end="")
        for j in range(sV2):
            print(end=" ")
        sV2 -= x
        print("*")
      
spaceValue = math.ceil(int(input())/2)-1
half(spaceValue)
half(spaceValue, False)
 
end = input()
