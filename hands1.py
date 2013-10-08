import random
import itertools
def main():
    while True:  
        try:
            num_hands = int(input('How many hands to evaluate? '))
            hand_size = int(input('5 or 7 cards? '))
            break
        except ValueError:
            print('What?')
            
        
    record = {'royal flush': 0, 'straight flush': 0, 'four of a kind': 0, 'full house': 0, \
    'flush': 0, 'straight': 0, 'three of a kind': 0, 'two pair': 0, 'pair': 0, 'high card': 0, 'total': 0}
    for num in range(0, num_hands):
        
        h, s, h_list = generate_hand(hand_size)
        if hand_size == 5:
            rank = evaluate_hand(h, s, h_list)
            record[rank] += 1
            record['total'] += 1
        else: 
            for hand in h_list:
                h = [hand[0], hand[1], hand[2], hand[3], hand[4]]
                print(h)
                s = [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]
                print(s)
                s.sort()
                rank = evaluate_hand(h, s, h_list)
                record[rank] += 1
                record['total'] += 1 
    pretty_print(record)

def generate_hand(hand_size):
    suits = ['0', '1', '2', '3']
    card_rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cards = []
    for n in card_rank:
        cards.append((suits[0],n))
        cards.append((suits[1],n))
        cards.append((suits[2],n))
        cards.append((suits[3],n))
    h = []
    if hand_size == 5:
        h = random.sample(cards, 5)
        h.sort()
        s = [h[0][1], h[1][1], h[2][1], h[3][1], h[4][1]]
        s.sort()
        h_list = []
        return h, s, h_list
    else:
       h = random.sample(cards, 7)
       h_list = list(itertools.combinations(h, 5))
       s = []
       return h, s, h_list
       
def evaluate_hand(h, s, h_list):
    if s == [1, 10, 11, 12, 13] and h[0][0] == h[1][0] == h[2][0] == h[3][0] == h[4][0]: 
       return 'royal flush'
        
    elif h[0][0] == h[1][0] == h[2][0] == h[3][0] == h[4][0] \
        and s[4] - s[3] == s[3] - s[2] == s[2] - s[1] == s[1] - s[0] == 1:
        return 'straight flush'
        
    elif (s[0] == s[1] == s[2] == s[3]) or (s[1] == s[2] == s[3] == s[4]):
        return 'four of a kind'
        
    elif (s[0] == s[1] == s[2] and s[3] == s[4]) \
        or (s[0] == s[1] and s[2] == s[3] == s[4]):
        return 'full house'
        
    elif h[0][0] == h[1][0] == h[2][0] == h[3][0] == h[4][0]:
        return 'flush'
        
    elif s[4] - s[3] == s[3] - s[2] == s[2] - s[1] == s[1] - s[0] == 1:
        return 'straight'
        
    elif (s[0] == s[1] == s[2] and s[2] != s[3] and s[3] != s[4]) \
        or (s[0] != s[1] and s[1] == s[2] == s[3] and s[3] != s[4]) \
        or (s[0] != s[1] and s[1] != s[2] and s[2] == s[3] == s[4]):
        return 'three of a kind'
        
    elif (s[0] == s[1] and s[1] != s[2] and s[2] == s[3] and s[3] != s[4]) \
        or (s[0] == s[1] and s[1] != s[2] and s[2] != s[3] and s[3] == s[4]) \
        or (s[0] != s[1] and s[1] == s[2] and s[2] != s[3] and s[3] == s[4]):
        return 'two pair'
        
    elif (s[0] == s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]) \
        or (s[0] != s[1] and s[1] == s[2] and s[2] != s[3] and s[3] != s[4]) \
        or (s[0] != s[1] and s[1] != s[2] and s[2] == s[3] and s[3] != s[4]) \
        or (s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] == s[4]):
        return 'pair'
        
    else:
        return 'high card'
        
  

def pretty_print(record):
    print('Total hands: ', record['total'])
    print('Hand counts by rank number: ', record['high card'], record['pair'],
    record['two pair'], \
    record['three of a kind'], record['straight'], record['flush'], record['full house'], \
    record['four of a kind'], record['straight flush'], record['royal flush'])

    print('Probability:')
    print(' of nothing:          {:>9.4%} '.format(record['high card'] / record['total']))
    print(' of one pair:         {:>9.4%} '.format(record['pair'] / record['total']))
    print(' of two pairs:        {:>9.4%} '.format(record['two pair'] / record['total']))
    print(' of three of a kind:  {:>9.4%} '.format(record['three of a kind'] / record['total']))
    print(' of a straight:       {:>9.4%} '.format(record['straight'] / record['total']))
    print(' of a flush:          {:>9.4%} '.format(record['flush'] / record['total']))
    print(' of a full house:     {:>9.4%} '.format(record['full house'] / record['total']))
    print(' of four of a kind:   {:>9.4%} '.format(record['four of a kind'] / record['total']))
    print(' of a straight flush: {:>9.4%} '.format(record['straight flush'] / record['total']))
    print(' of a royal flush:    {:>9.4%} '.format(record['royal flush'] / record['total']))

if __name__ == '__main__':
    main()


