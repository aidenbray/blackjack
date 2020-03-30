import os
os.system("cls") # Windows
import random

def printgreen(text):
    print("\033[1;32;40m" + text + "\033[1;37;40m")

def printred(text):
    print("\033[1;31;40m" + text + "\033[1;37;40m")

def printpurple(text):
    print("\033[1;35;40m" + text + "\033[1;37;40m")

def printhighlight(text):
    print("\033[1;37;44m" + text + "\033[1;37;40m")

printhighlight("======================================================")
printhighlight("AIDEN'S BLACKJACK                                     ")
printhighlight("======================================================")




#################################################################################
# loop
#################################################################################

playerwallet=100


if (playerwallet<=0):
       printred ("bankroped")
       playerplaying=False
       dealerplaying=False
   



while (playerwallet>0):

      
    printpurple("============================")   
    printpurple("new game")
    printpurple("your wallet is " + str(playerwallet))           
    printpurple("============================")

    bet=input("whats your bet ")
    print("your bet is ", bet)
    playerwallet=playerwallet-int(bet)

    playerhand=0
    playerplaying=True
    dealerplaying=True

    
    ######################################################################
    # PLAYER      
    ######################################################################

    while playerplaying:

        print()
        draw = input("draw a card (y/n) ")

        if (draw == "yes" or draw=="y"):
            x = random.randrange(1, 11)
        
            printgreen ("you drew a " + str(x))
            playerhand=playerhand+x
            printpurple ("your hand is " + str(playerhand))

            if playerhand > 21:
                printred ("you lost noob")
                playerplaying=False
                dealerplaying=False
                playerwallet = playerwallet - int(bet)

            if playerhand == 21:
                printgreen ("you win")
                playerplaying=False
                playerwallet = playerwallet + (int(bet) * 2)

        if (draw=="n"):
            playerplaying=False

    ######################################################################
    # DEALER      
    ######################################################################
    if (dealerplaying):
        print("dealers turn") 
    
    dealerhand=0
    while(dealerhand<16 and dealerplaying):
        dealerdraw = random.randrange(1, 11)
        print ("dealer drew a " + str(dealerdraw))
        dealerhand = dealerhand + dealerdraw
        print ("his hand is " + str(dealerhand))
        
        if (dealerhand > 21):
            print("=====================")
            printgreen("dealer busted you win")
            print("=====================")

        if (dealerhand > playerhand):  
            printred ("dealer wins")
            dealerplaying=False
            playerwallet=playerwallet-int(bet)

        if (dealerhand == playerhand):
            printred ("dearler wins") 
            dealerplaying=False
            playerwallet=playerwallet-int(bet) 

        
           

                    
            



            
        
        
        
        playerplaying=False 
    
