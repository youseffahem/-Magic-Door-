'''
Assignment #3-4 | The Magic Door
You are on a quest to open the Magic Door
that leads to a treasure room. To open the
door, you need to solve a few simple coding
tasks.
'''


print("Welcom In my door ")
print("you must solve all tasks..")

points=0

s=input(" Enter the first word of palindrome: ")
def is_palindrome(s=s):
    return s==s[::-1]

if is_palindrome(s):
    print("great")
    points=1
    
    f=input("Enter the secound word of palindrome: ")
    if is_palindrome(f):
        print("great")
        points=2
       
        g = input("Enter the third word of palindrome: ")

        if is_palindrome(g):
            print("great")
            points=3
           
        else:
            print("Nooooo و You had to solve all three puzzles")
            points=2
        
    else:
        print("Nooooo و You had to solve all three puzzles")
        points=1

else:
    print("Noooooو You had to solve all three puzzles")
    points=0
    
if points==3:
    print("congrath ")
    

else:
    print("sorry you cannt open this door")
   
    
