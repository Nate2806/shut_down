def shutdown(): #FUNCTION DEFINITION
    user_input=input("DO YOU WANT TO SHUTDOWN (Yes/No)")#FUNCTION BODY
    if user_input in ('Yes''YES''yes'):
        print("SHUTTING DOWN")
    elif user_input in ('No''NO''no'):
        print("ABORT SHUTDOWN")
    else:
        print("Sorry, Invalid input")
#FUNCTION CALL
shutdown()
    

