import random
def bull(string1, string2):

    times = 0
    for ind, lett in enumerate(string2):
        if lett == string1[ind]:
            times += 1

    return times

digit =["1","2","3","4","5","6","7","8","9","0"]
random.shuffle(digit)

secret =digit[0:4]

print("you will have to guess a didgit with number with no repeting digets,bulls mean its in the right spot and cows mean its in the line but not in the right spot")
bulls=0
cow=0
tries=0
while bulls < 4 :
    
    guess = input("Guess a 4 number string: ")
    cow=0
    bulls=0

    for number in guess:
        cow += secret.count(number)
    
    bulls = bull(guess,secret)
    cow -= bulls
    print(f"you have {bulls} bulls and {cow} cows ")

    tries += 1
print(f"you took {tries} tries")
#i like it
