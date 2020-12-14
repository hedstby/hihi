def run_game():
    import time
    import random
    mode=input('Choose your game mode. (computer(c) or double(d))')
    answer = ''  
    a_count=0 
    b_count=0 
    
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    random.shuffle(items)
    start=time.time()
    for i in range(4):
        answer+=str(items[i])
    if (mode == "c"):
        name=input('Please enter your name')
        while(True):
            number=input('Enter the number: ')
            if not number.isdigit() or len(number) != 4:
                print('Please enter four digits')
            else:
                if number==answer:
                    print('{},you guess the correct number!' .format(name))
                    break
                for i in range(4):

                    for j in range(4):
                        if i==j and number[i]==answer[j]:
                            a_count+=1
                        elif number[i]==answer[j]:
                            b_count+=1
                print('{0}A{1}B'.format(a_count,b_count))
                a_count=0
                b_count=0
    else:
        name1=input('Please player1 enter your name')
        name2=input('Please player2 enter your name')
        L1=input('{} ,please enter the code' .format(name1))

        while(True):
            number=input('{},Enter the number: ' .format(name2))
            if not number.isdigit() or len(number) != 4:  
                print('Please enter four digits')
            else:
                if number==L1:
                    print('{},you guess the correct number!' .format(name2))
                    break
                for i in range(4):
                    for j in range(4):
                        if i==j and number[i]==L1[j]:
                            a_count+=1
                        elif number[i]==L1[j]:
                            b_count+=1
                print('{0}A{1}B'.format(a_count,b_count))
                a_count=0
                b_count=0
    end=time.time()
    second1=int(end-start)
    minute=second1//60
    second2=second1-minute*60
    if second1<60:
        print('共使用%d秒'%second1)
        again = str(input("Do you want to play again (type yes or no): "))
        if again=="yes":
            run_game()
        else:
            exit()
    else:
        print('共使用%d分%d秒'%(minute,second2))
        again = str(input("Do you want to play again (type yes or no): "))
        if again=="yes":
            run_game()
        else:
            exit()
run_game()
