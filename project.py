import random
#get Guess
def guess():
    return list(input("Enter The number"))
    length=len(list)
    return length


#generate and compute
def generate_code():
    digit=[str(num) for num in range(10000)]
    random.shuffle(digit)
    return digit[:3]
#generate the clue
def generate_clue(code,user_guess):
    if code == user_guess:
        return "Code Cracked"
    clue=[]
    for ind, num in enumerate(user_guess):
        print(ind)
        if num==code[ind]:
            clue.append("match")
        elif num in code:
            clue.append("close")
    if clue==[]:
        return["NOPE"]
    else:
        return clue

#raun game logic
print("Welcome user")
secret_code = generate_code()
clue_report = []
while clue_report != "Code Cracked":
    guess1 = guess()
    if guess1==3:
        clue_report = generate_clue(guess1,secret_code)
        print("Result is:")
        for i in clue_report:
            print(i)
    else:
        print("plaese Enter 3 Digit Only!")
