a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

def scores():
    Alice = [a0, a1, a2]
    Bob = [b0, b1, b2]
    alice_score = 0
    bob_score = 0
    index = 0
    for val in Alice:
        if val not in range(1,101) or Bob[index] not in range(1,101):
            index+=1
            pass
        elif val==Bob[index]:
            alice_score+=0
            bob_score+=0
            index+=1
        elif val>Bob[index]:
            alice_score+=1
            index+=1
        elif val<Bob[index]:
            bob_score+=1
            index+=1
    return (str(alice_score) + " " + str(bob_score))       
print(scores())