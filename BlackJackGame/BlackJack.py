import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def tot(my_list):
    sum=0
    for items in my_list:
        sum += items
    return sum

cards = [11,2,3,4,5,6,7,8,9,10]
should_continue=True
game_over=False
computer = [random.choice(cards),random.choice(cards)]
dealer = [random.choice(cards),random.choice(cards)]
print(logo)
while should_continue:
    print(f"Your cards : {dealer}")
    print(f"Computer Cards : {computer[:-1]}")
    computer_tot = tot(computer)
    dealer_tot = tot(dealer)
    if(computer_tot == 21):
        should_continue=False
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("Computer win...!!!")
        game_over=True
        continue
    if(dealer_tot == 21):
        should_continue=False
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("You win...!!!")
        game_over=True
        continue
    if(dealer_tot > 21):
        if(dealer[0] == 11) or (dealer[1] == 11):
            if(dealer_tot - 10 < 21):
                dealer_tot = dealer_tot - 10
                continue
            elif (dealer_tot - 10 == 21):
                print(f"Your cards : {dealer}")
                print(f"Computer Cards : {computer}")
                print("You win...!!!")
                game_over=True
                should_continue=False
                continue
            else:
                should_continue=False
                print(f"Your cards : {dealer}")
                print(f"Computer Cards : {computer}")
                print("Computer win...!!!")
                game_over=True
                continue
        else:
            should_continue=False
            print(f"Your cards : {dealer}")
            print(f"Computer Cards : {computer}")
            print("Computer win...!!!")
            game_over=True
            continue
    else:
        dealer_choice = input("Do you want to draw another card, Type Y or N ?").lower()
        if(dealer_choice == 'y'):
            dealer.append(random.choice(cards))
        else:
            should_continue=False

should_continue=True
while should_continue and not game_over:
    if(computer_tot < 17):
        computer.append(random.choice(cards))
        computer_tot=tot(computer)
    else:
        break
    if(computer_tot > 21):
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("You win...!!!")
        should_continue=False
        game_over=True
        break
    elif(computer_tot == 21):
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("Computer win...!!!")
        should_continue=False
        game_over=True
        break

if(should_continue) and not game_over :
    if(computer_tot < dealer_tot):
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("You win...!!!")
    elif(computer_tot > dealer_tot):
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("Computer win...!!!")
    else:
        print(f"Your cards : {dealer}")
        print(f"Computer Cards : {computer}")
        print("Its a Draw...!!!")


