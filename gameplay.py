# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

information_sets_player1 = [('J',1)]
cards = ['JK', 'JQ', 'QK','QJ','KJ','KQ']
game_tree = {'JK':
    {
        'Bet1':
            {
                'Bet2': -2, 'Fold2': 1
            }
        ,
        'Check1':
            {
                'Bet2':

                        {
                            'Bet1': -2, 'Fold1': -1,
                        }
                    ,
                'Check2': -1
            }


    },
    'JQ':
        {
            'Bet1':
                {
                    'Bet2': -2, 'Fold2': 1
                }
            ,
            'Check1':
                {
                    'Bet2':

                            {
                                'Bet1': -2, 'Fold1': -1,
                            }
                        ,
                    'Check2': -1
                }


        },
    'QK':
    {
        'Bet1':
            {
                'Bet2': -2, 'Fold2': 1
            }
        ,
        'Check1':
            {
                'Bet2':

                        {
                            'Bet1': -2, 'Fold1': -1,
                        }
                    ,
                'Check2': -1
            }


    },
    'QJ':
    {
        'Bet1':
            {
                'Bet2': 2, 'Fold2': 1
            }
        ,
        'Check1':
            {
                'Bet2':

                        {
                            'Bet1': 2, 'Fold1': -1,
                        }
                    ,
                'Check2': 1
            }


    },
    'KJ':
    {
        'Bet1':
            {
                'Bet2': 2, 'Fold2': 1
            }
        ,
        'Check1':
            {
                'Bet2':

                        {
                            'Bet1': 2, 'Fold1': -1,
                        }
                    ,
                'Check2': 1
            }


    },
    'KQ':
    {
        'Bet1':
            {
                'Bet2': 2, 'Fold2': 1
            }
        ,
        'Check1':
            {
                'Bet2':
                    {
                            'Bet1': 2, 'Fold1': -1,
                        }
                    ,
                'Check2': 1
            }


    },

}
def player1_strategy(card, node, strategy):
    if node == 1:
        if card == 'J':
            return strategy[0]
        elif card == 'K':
            return strategy[1]
        elif card == 'Q':
            return strategy[2]
    elif node == 2:
        if card == 'J':
            return strategy[3]
        if card == 'Q':
            return strategy[4]
        if card == 'K':
            return strategy[5]

def player2_strategy(card, opp_strategy, strategy):
    if opp_strategy == 'Bet':
        if card == 'J':
            return strategy[0]
        elif card == 'K':
            return strategy[1]
        elif card == 'Q':
            return strategy[2]
    elif opp_strategy == 'Check':
        if card == 'J':
            return strategy[3]
        if card == 'Q':
            return strategy[4]
        if card == 'K':
            return strategy[5]

# Press the green button in the gutter to run the script.


def information_set_prob1(opp_strategies_pos, prior=0.5):
    info_sets_prob_1 = []
    for i in range(3):
        info_sets_prob_1.append((prior, 1-prior))
    bet = 1
    info_set_prob_1 = (player2_strategy('Q', 'Check', opp_strategies_pos)[bet] * prior) / ((player2_strategy('Q', 'Check', opp_strategies_pos)[bet]  * prior) +
                                                            (player2_strategy('K', 'Check', opp_strategies_pos)[bet] * (1 - prior)))
    info_sets_prob_1.append((info_set_prob_1, 1 - info_set_prob_1))

    info_set_prob_1 = (player2_strategy('J', 'Check', opp_strategies_pos)[bet] * prior) / (
                (player2_strategy('J', 'Check', opp_strategies_pos)[bet] * prior) +
                (player2_strategy('K', 'Check', opp_strategies_pos)[bet] * (1 - prior)))
    info_sets_prob_1.append((info_set_prob_1, 1 - info_set_prob_1))

    info_set_prob_1 = (player2_strategy('J', 'Check', opp_strategies_pos)[bet] * prior) / (
                (player2_strategy('J', 'Check', opp_strategies_pos)[bet] * prior) +
                (player2_strategy('Q', 'Check', opp_strategies_pos)[bet] * (1 - prior)))
    info_sets_prob_1.append((info_set_prob_1, 1 - info_set_prob_1))

    return info_sets_prob_1


def information_set_prob2(opp_strategies_pos, prior=0.5):
    info_sets_prob_2 = []

    bet=1
    check=0
    actions = [check,bet]

    for action in actions:
        info_set_prob_1 = (player1_strategy('Q', 1, opp_strategies_pos)[action] * prior) / (
                (player1_strategy('Q', 1, opp_strategies_pos)[action] * prior) +
                (player1_strategy('K', 1, opp_strategies_pos)[action] * (1 - prior)))
        info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    for action in actions:
        info_set_prob_1 = (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) / (
                (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) +
                (player1_strategy('K', 1, opp_strategies_pos)[action] * (1 - prior)))
        info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    for action in actions:
        for action in actions:
            info_set_prob_1 = (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) / (
                    (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) +
                    (player1_strategy('Q', 1, opp_strategies_pos)[action] * (1 - prior)))
            info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    return info_sets_prob_2

def strategies_player1(opp_strategies, beliefs):
    





def game_play():
    strategies_1 = [(0.6, 0.4),(0.5, 0.5),(0.7,0.3),(0.34,0.66),(0.87,0.13),(0.27,0.73)]
    strategies_2 = [(0.12,0.88),(0.45,0.55),(0.28,0.72),(0.39,0.61),(0.67,0.33),(0.9,0.1)]
    print(information_set_prob1(strategies_2))
    print(information_set_prob2(strategies_1))
    card_shuffle = np.random.choice(cards)
    print(card_shuffle)
    actions = []
    player1_card = card_shuffle[0]
    player2_card = card_shuffle[1]
    player1_reward = 0
    player2_reward = 0
    print('Action 1(P1)...')
    strategy_prob = player1_strategy(player1_card, 1, strategies_1)
    num = np.random.randn()
    if num < strategy_prob[0]:
        print('Player 1: Bets')
        actions.append('Bet1')
    else:
        print('Player 1: Checks')
        actions.append('Check1')
    print('Action 2(P2)...')
    opp_action = actions[0][:-1]
    strategy_prob = player2_strategy(player2_card, opp_action, strategies_2)
    num = np.random.randn()
    if num < strategy_prob[0]:
        print('Player 2: Bets')
        actions.append('Bet2')
        if actions[0] == 'Bet1':
            return game_tree[card_shuffle][actions[0]][actions[1]]
    else:
        if actions[0] == 'Check1':
            print('Player 2: Checks')
            actions.append('Check2')
        else:
            print('Player 2: Folds')
            actions.append('Fold2')
        return game_tree[card_shuffle][actions[0]][actions[1]]
    print('Action 3(P1)...')
    strategy_prob = player1_strategy(player1_card,2,strategies_1)
    num = np.random.randn()
    if num < strategy_prob[0]:
        print('Player 1: Bets again')
        actions.append('Bet1')
        return game_tree[card_shuffle][actions[0]][actions[1]][actions[2]]
    else:
        print('Player 1: Folds')
        actions.append('Fold1')
        return game_tree[card_shuffle][actions[0]][actions[1]][actions[2]]





if __name__ == '__main__':
    print_hi('PyCharm')
    payoff = game_play()
    print('payoff =', payoff)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
