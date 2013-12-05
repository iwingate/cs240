import random


spots = 0
players_picks = []
house_picks = []

complete_total = 0

total = 0

zero_wins = 0

one_win = 0

two_wins = 0

three_wins = 0

four_wins = 0
       
five_wins = 0
        
six_wins = 0
        
seven_wins = 0
        
eight_wins = 0
     
nine_wins = 0
   
ten_wins = 0

l = range(1, 81)

while spots < 11:
    spots += 1
    total_matched = 0 
    total = 0
    for number in range(1000000):

        house_picks += random.sample(l,20)
     
        players_picks += random.sample(l,spots)
        
        for number in players_picks:
            if number in house_picks:
                total_matched += 1
                complete_total += 1

        if spots == 1:
            if total_matched == 1:
                one_win += 1
            total += 1

        if spots == 4 or spots == 3 or spots == 2:
            if total_matched == 2:
                two_wins += 1
            elif total_matched == 3:
                three_wins += 1
            elif total_matched == 4:
                four_wins += 1
            total += 1
    
        if spots == 6 or spots == 5:
            if total_matched == 3:
                three_wins += 1
            elif total_matched == 4:
                four_wins += 1
            elif total_matched == 5:
                five_wins += 1
            elif total_matched == 6:
                six_wins += 1
            total += 1
         
        if spots == 10 or spots == 9 or spots == 8 or spots == 7:
            if total_matched == 0:
                zero_wins += 1 
            elif total_matched == 4:
                four_wins += 1
            elif total_matched == 5:
                five_wins += 1
            elif total_matched == 6:
                six_wins += 1
            elif total_matched == 7:
                seven_wins += 1
            elif total_matched == 8:
                eight_wins += 1
            elif total_matched == 9:
                nine_wins += 1
            elif total_matched == 10:
                ten_wins += 1
            total += 1
        
        if total == 99999 or total == 199999 or total == 299999 or total == 399999 \
        or total == 499999 or total == 599999 or total == 699999 or total == 799999 \
        or total == 899999 or total == 999999: 
            if spots == 1: 
                percentage = one_win / (total + 1)
                if one_win == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - one_win) / one_win)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, one_win, percentage, odds))

            elif spots == 2: 
                percentage = two_wins / (total + 1)
                if two_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - two_wins) / two_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, two_wins, percentage, odds))
        
            elif spots == 3: 
                percentage = three_wins / (total + 1)
                if three_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - three_wins) / three_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, three_wins, percentage, odds))
        
            elif spots == 4: 
                percentage = four_wins / (total + 1)
                if four_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - four_wins) / four_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, four_wins, percentage, odds))
        
            elif spots == 5: 
                percentage = five_wins / (total + 1)
                if five_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - five_wins) / five_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, five_wins, percentage, odds))

            elif spots == 6: 
                percentage = six_wins / (total + 1)
                if six_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - six_wins) / six_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, six_wins, percentage, odds))
        
            elif spots == 7: 
                percentage = seven_wins / (total + 1)
                if seven_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - seven_wins) / seven_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, seven_wins, percentage, odds))
        
            elif spots == 8: 
                percentage = eight_wins / (total + 1)
                if eight_wins == 0: 
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - eight_wins) / eight_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, eight_wins, percentage, odds))
        
            elif spots == 9: 
                percentage = nine_wins / (total + 1)
                if nine_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - nine_wins) / nine_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, nine_wins, percentage, odds))
        
            elif spots == 10: 
                percentage = ten_wins / (total + 1)
                if ten_wins == 0:
                    odds = 'N/A'
                else: 
                    odds = '1:{}'.format((total - ten_wins) / ten_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, ten_wins, percentage, odds))
        
            elif spots == 0: 
                percentage = zero_wins / (total + 1)
                if zero_wins == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total - zero_wins) / zero_wins)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, zero_wins, percentage, odds))


        players_picks = []
        house_picks = []
        total_matched = 0
   





