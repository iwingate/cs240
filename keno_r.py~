import random


spots = 0
players_picks = []
house_picks = []

complete_total = 0

total = 0

zero = 0

one = 0

two = 0

three = 0

four = 0
       
five = 0
        
six = 0
        
seven = 0
        
eight = 0
     
nine = 0
   
ten = 0

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
                one += 1
            total += 1

        if spots == 2:
            if total_matched == 2:
                two += 1
            total += 1
        
        if spots == 3:
            if total_matched == 2:
                two += 1
            if total_matched == 3:
                three += 1
            total += 1
        
        if spots == 4:
            if total_matched == 2:
                two += 1
            elif total_matched == 3:
                three += 1
            elif total_matched == 4:
                four += 1
            total += 1

        if spots == 5:
            if total_matched == 3:
                three += 1
            elif total_matched == 4:
                four += 1
            elif total_matched == 5:
                five += 1
            total += 1
        
        if spots == 6:
            if total_matched == 3:
                three += 1
            elif total_matched == 4:
                four += 1
            elif total_matched == 5:
                five += 1
            elif total_matched == 6:
                six += 1
            total += 1
         
        if spots == 7:
            if total_matched == 0:
                zero +=1
            elif total_matched == 4:
                four += 1
            elif total_matched == 5:
                five += 1
            elif total_matched == 6:
                six += 1
            elif total_matched == 7:
                seven += 1
            total += 1

        if spots == 8:
            if total_matched == 0:
                zero +=1
            elif total_matched == 4:
                four += 1
            elif total_matched == 5:
                five += 1
            elif total_matched == 6:
                six += 1
            elif total_matched == 7:
                seven += 1
            elif total_matched == 8:
                eight += 1
            total += 1   

        if spots == 9:
            if total_matched == 0:
                zero +=1
            elif total_matched == 4:
                four += 1
            elif total_matched == 5:
                five += 1
            elif total_matched == 6:
                six += 1
            elif total_matched == 7:
                seven += 1
            elif total_matched == 8:    
                eight += 1
            elif total_matched == 9:
                nine += 1
            total += 1

        if spots == 10:
            if total_matched == 0:
                zero += 1 
            elif total_matched == 5:
                five += 1
            elif total_matched == 6:
                six += 1
            elif total_matched == 7:
                seven += 1
            elif total_matched == 8:
                eight += 1
            elif total_matched == 9:
                nine += 1
            elif total_matched == 10:
                ten += 1
            total += 1
        
        if total == 99999 or total == 199999 or total == 299999 or total == 399999 \
        or total == 499999 or total == 599999 or total == 699999 or total == 799999 \
        or total == 899999 or total == 999999: 
            if spots == 1: 
                percentage = one / (total + 1)
                if one == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - one) / one)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, one, percentage, odds))
                if total == 999999:
                    one_win = 0    
                    total = 0
                
            elif spots == 2: 
                percentage = two / (total + 1)
                if two == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - two) / two)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, two, percentage, odds))
                if total == 999999:
                    two_wins = 0
                    total = 0 
               
            elif spots == 3: 
                sum_spots = two + three
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    two_wins = 0
                    three_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 4: 
                sum_spots = two + three + four
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    two_wins = 0
                    three_wins = 0
                    four_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 5: 
                sum_spots = three + four + five
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    three_wins = 0
                    four_wins = 0
                    five_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 6: 
                sum_spots = three + four + five + six
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    three_wins = 0
                    four_wins = 0
                    five_wins = 0
                    six_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 7: 
                sum_spots = zero + four + five + six + seven
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    zero_wins = 0
                    four_wins = 0
                    five_wins = 0
                    six_wins = 0
                    seven_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 8:
                sum_spots = zero + four + five + six + seven + eight 
                percentage = sum_spots / (total + 1)
                if sum_spots == 0: 
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    zero_wins = 0
                    four_wins = 0
                    five_wins = 0
                    six_wins = 0
                    seven_wins = 0
                    eight_wins = 0
                    total = 0
                    sum_spots = 0
            elif spots == 9: 
                sum_spots = zero + four + five + six + seven + eight + nine
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else:
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    zero_wins = 0
                    four_wins = 0
                    five_wins = 0
                    six_wins = 0
                    seven_wins = 0
                    eight_wins = 0
                    nine_wins = 0
                    total = 0
                    sum_spots = 0
                 
            elif spots == 10: 
                sum_spots = zero + five + six + seven + eight + nine + ten
                percentage = sum_spots / (total + 1)
                if sum_spots == 0:
                    odds = 'N/A'
                else: 
                    odds = '1:{}'.format((total + 1 - sum_spots) / sum_spots)
                print('{}-Spot Game (spots matched)Number of wins[Percentage%]Odds'.format(spots))
                print()
                print('({}){}[{}]{}'.format(complete_total, sum_spots, percentage, odds))
                if total == 999999:
                    zero_wins = 0
                    five_wins = 0
                    six_wins = 0
                    seven_wins = 0
                    eight_wins = 0
                    nine_wins = 0
                    ten_wins = 0
                    total = 0
                    sum_spots = 0


        players_picks = []
        house_picks = []
        total_matched = 0
   





