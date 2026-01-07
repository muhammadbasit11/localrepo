import random
def guess_game():
    gen_number=random.randint(1,100)
    print(gen_number)
    print("WELCOME TO GUESS A NUMBER GAME ")
    print("I HAVE PICKED A NUMBER BETWEEN 1 AND 100,GUESS IT.")
    
    attempts=0
    user_num=None
    while (user_num!=gen_number):
        user_num=int(input("enter the number: "))
        attempts+=1
        if(user_num>gen_number):
            print("TOO HIGH")
        elif(user_num<gen_number):
            print("TOO LOW")
        else:
            print("YOU GUESS THE NUMBER,YOU WON")
            print(attempts)
        

        
        
guess_game()