'''
Sample program. User picks a range of numbers bounded by upper, lower. Computer uses binary guessing to find the answer in the fewest number of guesses possible.

Sample Input:
0 50
<
<
<
<
>
>

'''
import random

imguessing = True
myguess = None
response = None

lower_bound = int(input("Enter the smaller number: "))
upper_bound = int(input("Enter the larger number:"))
round = 0
while imguessing:
    round += 1
    print(str(lower_bound) + ' ' + str(upper_bound))
    if (myguess == lower_bound + 1 and response == '<') or (myguess == upper_bound -1 and response == '>'):
        print("I'm out of guesses, and you cheated.")
        break
    myguess = int((lower_bound + upper_bound) / 2)
    print(f'Your number is {myguess}')
    response = input("Enter = < >")
    if response == '=':
        print(f"Hooray, I've got it in {round} tries!")
        ImGuessing = False
        break
    elif response == "<":
        upper_bound = myguess
        continue
    else:
        lower_bound = myguess
        continue


