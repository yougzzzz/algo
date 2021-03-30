mot1 =input("1er mot: ")
mot2 =input("2eme mot: ")
l = 0
grand = None
while grand == None :
    if mot1[l] == mot2[l]:
        l +=1
    elif mot1[l] < mot2[l]:
        grand = True
    elif mot1[l] > mot2[l]:
        grand = False

state = mot1 if grand else mot2
print(state)