import numpy as np
import matplotlib.pyplot as plt

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#information_sets_player1 = [('J',1)]
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
        elif card == 'Q':
            return strategy[1]
        elif card == 'K':
            return strategy[2]
    elif node == 2:
        if card == 'J':
            return strategy[3]
        if card == 'Q':
            return strategy[4]
        if card == 'K':
            return strategy[5]

def player2_strategy(card, opp_strategy, strategy):
    if card == 'Q':
        if opp_strategy == 'Check':
            return strategy[0]
        elif opp_strategy == 'Bet':
            return strategy[1]
    elif card == 'K':
        if opp_strategy == 'Check':
            return strategy[2]
        elif opp_strategy == 'Bet':
            return strategy[3]
    elif card == 'J':
        if opp_strategy == 'Check':
            return strategy[4]
        elif opp_strategy == 'Bet':
            return strategy[5]

# Press the green button in the gutter to run the script.


def information_set_prob1(opp_strategies_pos, prior=0.5):
    info_sets_prob_1 = []
    for i in range(3):
        info_sets_prob_1.append((prior, 1-prior))
    bet = 0
    temp_info_prob1 = player2_strategy('Q', 'Check', opp_strategies_pos)[bet]
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

    bet=0
    check=1
    actions = [check,bet]

    for action in actions:
        temp1 = player1_strategy('Q', 1, opp_strategies_pos)[action]
        info_set_prob_1 = (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) / (
                (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) +
                (player1_strategy('K', 1, opp_strategies_pos)[action] * (1 - prior)))
        info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    for action in actions:
        info_set_prob_1 = (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) / (
                (player1_strategy('J', 1, opp_strategies_pos)[action] * prior) +
                (player1_strategy('Q', 1, opp_strategies_pos)[action] * (1 - prior)))
        info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    for action in actions:
        temp1 = player1_strategy('Q', 1, opp_strategies_pos)[action]
        info_set_prob_1 = (player1_strategy('Q', 1, opp_strategies_pos)[action] * prior) / (
                (player1_strategy('Q', 1, opp_strategies_pos)[action] * prior) +
                (player1_strategy('K', 1, opp_strategies_pos)[action] * (1 - prior)))
        info_sets_prob_2.append((info_set_prob_1, 1 - info_set_prob_1))

    return info_sets_prob_2

def strategies_player1(lamda, opp_strategies, beliefs):
    player1_strategies = []
    ''' FOR K 2nd turn'''
    bet_payoff_KJ = game_tree['KJ']['Check1']['Bet2']['Bet1']
    fold_payoff_KJ = game_tree['KJ']['Check1']['Bet2']['Fold1']
    bet_payoff_KQ = game_tree['KJ']['Check1']['Bet2']['Bet1']
    fold_payoff_KQ = game_tree['KJ']['Check1']['Bet2']['Fold1']
    bet_payoff_K = (bet_payoff_KJ * beliefs[5][0] + bet_payoff_KQ * beliefs[5][1])
    fold_payoff_K = (fold_payoff_KJ * beliefs[5][0] + fold_payoff_KQ * beliefs[5][1])
    strategy_K_2 = (np.exp(lamda * bet_payoff_K) / (np.exp(lamda * bet_payoff_K) + np.exp(lamda * fold_payoff_K)),
                   np.exp(lamda * fold_payoff_K) / (np.exp(lamda * bet_payoff_K) + np.exp(lamda * fold_payoff_K)))
    player1_strategies.insert(0,strategy_K_2)
    ''' FOR Q 2nd turn'''
    bet_payoff_QJ = game_tree['QJ']['Check1']['Bet2']['Bet1']
    fold_payoff_QJ = game_tree['QJ']['Check1']['Bet2']['Fold1']
    bet_payoff_QK = game_tree['QK']['Check1']['Bet2']['Bet1']
    fold_payoff_QK = game_tree['QK']['Check1']['Bet2']['Fold1']
    bet_payoff_Q = (bet_payoff_QJ * beliefs[4][0] + bet_payoff_QK * beliefs[4][1])
    fold_payoff_Q = (fold_payoff_QJ * beliefs[4][0] + fold_payoff_QK * beliefs[4][1])
    strategy_Q_2 = (np.exp(lamda * bet_payoff_Q) / (np.exp(lamda * bet_payoff_Q) + np.exp(lamda * fold_payoff_Q)),
                    np.exp(lamda * fold_payoff_Q) / (np.exp(lamda * bet_payoff_Q) + np.exp(lamda * fold_payoff_Q)))
    player1_strategies.insert(0, strategy_Q_2)
    ''' FOR J in 2nd turn'''
    bet_payoff_JQ = game_tree['JQ']['Check1']['Bet2']['Bet1']
    fold_payoff_JQ = game_tree['JQ']['Check1']['Bet2']['Fold1']
    bet_payoff_JK = game_tree['JK']['Check1']['Bet2']['Bet1']
    fold_payoff_JK = game_tree['JK']['Check1']['Bet2']['Fold1']
    bet_payoff_J = (bet_payoff_JQ * beliefs[3][0] + bet_payoff_JK * beliefs[3][1])
    fold_payoff_J = (fold_payoff_JQ * beliefs[3][0] + fold_payoff_JK * beliefs[3][1])
    strategy_J_2 = (np.exp(lamda * bet_payoff_J) / (np.exp(lamda * bet_payoff_J) + np.exp(lamda * fold_payoff_J)),
                    np.exp(lamda * fold_payoff_J) / (np.exp(lamda * bet_payoff_J) + np.exp(lamda * fold_payoff_J)))
    player1_strategies.insert(0, strategy_J_2)
    ''' FOR K in 1st Turn'''
    expected_payoff_KJ_2 = (strategy_K_2[0]*game_tree['KJ']['Check1']['Bet2']['Bet1'] + strategy_K_2[1]*game_tree['KJ']['Check1']['Bet2']['Fold1'])
    expected_payoff_KQ_2 = (strategy_K_2[0] * game_tree['KQ']['Check1']['Bet2']['Bet1'] + strategy_K_2[1] *
                            game_tree['KQ']['Check1']['Bet2']['Fold1'])

    expected_payoff_K_bet_1 = (opp_strategies[5][1]*game_tree['KJ']['Bet1']['Fold2']*beliefs[2][0] + opp_strategies[1][1]*game_tree['KQ']['Bet1']['Fold2']*beliefs[2][1]) + (opp_strategies[5][0]*game_tree['KJ']['Bet1']['Bet2']*beliefs[2][0] + opp_strategies[1][0]*game_tree['KQ']['Bet1']['Bet2']*beliefs[2][1])
    expected_payoff_K_check_1 = (opp_strategies[4][1]*game_tree['KJ']['Check1']['Check2']*beliefs[2][0] + opp_strategies[0][1]*game_tree['KQ']['Check1']['Check2']*beliefs[2][1]) + (opp_strategies[4][0]*expected_payoff_KJ_2*beliefs[2][0] + opp_strategies[0][0]*expected_payoff_KQ_2*beliefs[2][1])
    strategy_K_1 = (np.exp(lamda * expected_payoff_K_bet_1)/(np.exp(lamda * expected_payoff_K_bet_1) + np.exp(lamda * expected_payoff_K_check_1)), np.exp(lamda * expected_payoff_K_check_1)/(np.exp(lamda * expected_payoff_K_bet_1) + np.exp(lamda * expected_payoff_K_check_1)))
    player1_strategies.insert(0, strategy_K_1)
    '''FOR Q in 1st Turn'''
    expected_payoff_QJ_2 = (strategy_Q_2[0] * game_tree['QJ']['Check1']['Bet2']['Bet1'] + strategy_Q_2[1] *
                            game_tree['QJ']['Check1']['Bet2']['Fold1'])
    expected_payoff_QK_2 = (strategy_Q_2[0] * game_tree['QK']['Check1']['Bet2']['Bet1'] + strategy_Q_2[1] *
                            game_tree['QK']['Check1']['Bet2']['Fold1'])

    expected_payoff_Q_bet_1 = (opp_strategies[5][1] * game_tree['QJ']['Bet1']['Fold2'] * beliefs[1][0] +
                               opp_strategies[3][1] * game_tree['QK']['Bet1']['Fold2'] * beliefs[1][1]) + (
                                          opp_strategies[5][0] * game_tree['QJ']['Bet1']['Bet2'] * beliefs[1][0] +
                                          opp_strategies[3][0] * game_tree['QK']['Bet1']['Bet2'] * beliefs[1][1])
    expected_payoff_Q_check_1 = (opp_strategies[4][1] * game_tree['QJ']['Check1']['Check2'] * beliefs[1][0] +
                                 opp_strategies[2][1] * game_tree['QK']['Check1']['Check2'] * beliefs[1][1]) + (
                                            opp_strategies[4][0] * expected_payoff_QJ_2 * beliefs[1][0] +
                                            opp_strategies[2][0] * expected_payoff_QK_2 * beliefs[1][1])
    strategy_Q_1 = (np.exp(lamda * expected_payoff_Q_bet_1) / (
                np.exp(lamda * expected_payoff_Q_bet_1) + np.exp(lamda * expected_payoff_Q_check_1)),
                    np.exp(lamda * expected_payoff_Q_check_1) / (
                                np.exp(lamda * expected_payoff_Q_bet_1) + np.exp(lamda * expected_payoff_Q_check_1)))
    player1_strategies.insert(0, strategy_Q_1)
    '''FOR J in 1st Turn'''
    expected_payoff_JQ_2 = (strategy_J_2[0] * game_tree['JQ']['Check1']['Bet2']['Bet1'] + strategy_K_2[1] *
                            game_tree['JQ']['Check1']['Bet2']['Fold1'])
    expected_payoff_JK_2 = (strategy_J_2[0] * game_tree['JK']['Check1']['Bet2']['Bet1'] + strategy_K_2[1] *
                            game_tree['JK']['Check1']['Bet2']['Fold1'])

    expected_payoff_J_bet_1 = (opp_strategies[1][1] * game_tree['JQ']['Bet1']['Fold2'] * beliefs[0][0] +
                               opp_strategies[3][1] * game_tree['JK']['Bet1']['Fold2'] * beliefs[0][1]) + (
                                          opp_strategies[1][0] * game_tree['JQ']['Bet1']['Bet2'] * beliefs[0][0] +
                                          opp_strategies[3][0] * game_tree['JK']['Bet1']['Bet2'] * beliefs[0][1])
    expected_payoff_J_check_1 = (opp_strategies[0][1] * game_tree['JQ']['Check1']['Check2'] * beliefs[0][0] +
                                 opp_strategies[2][1] * game_tree['JK']['Check1']['Check2'] * beliefs[0][1]) + (
                                            opp_strategies[0][0] * expected_payoff_JQ_2 * beliefs[0][0] +
                                            opp_strategies[2][0] * expected_payoff_JK_2 * beliefs[0][1])
    strategy_J_1 = (np.exp(lamda * expected_payoff_J_bet_1) / (
                np.exp(lamda * expected_payoff_J_bet_1) + np.exp(lamda * expected_payoff_J_check_1)),
                    np.exp(lamda * expected_payoff_J_check_1) / (
                                np.exp(lamda * expected_payoff_J_bet_1) + np.exp(lamda * expected_payoff_J_check_1)))
    player1_strategies.insert(0, strategy_J_1)
    return player1_strategies

def strategies_player2(lamda, opp_strategies, beliefs):
    player2_strategies = []
    '''FOR IS 1'''
    expected_payoff_JQ_2 = opp_strategies[3][1] * game_tree['JQ']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[3][0] * game_tree['JQ']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_KQ_2 = opp_strategies[5][1] * game_tree['KQ']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[5][0] * game_tree['KQ']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_IS_1_check = beliefs[0][0] * game_tree['JQ']['Check1']['Check2'] * -1 + beliefs[0][1] * game_tree['KQ']['Check1']['Check2'] * -1
    expected_payoff_IS_1_bet = beliefs[0][0] * expected_payoff_JQ_2 + beliefs[0][1] * expected_payoff_KQ_2
    strategy_IS_1 = (np.exp(lamda * expected_payoff_IS_1_bet)/(
            np.exp(lamda * expected_payoff_IS_1_check) + np.exp(lamda * expected_payoff_IS_1_bet)),
                     np.exp(lamda * expected_payoff_IS_1_check)/(
                             np.exp(lamda * expected_payoff_IS_1_check) + np.exp(lamda * expected_payoff_IS_1_bet)))
    player2_strategies.append(strategy_IS_1)
    '''FOR IS 2'''
    expected_payoff_IS_2_fold = beliefs[1][0] * game_tree['JQ']['Bet1']['Fold2'] * -1 + beliefs[1][1] * game_tree['KQ']['Bet1']['Fold2'] * -1
    expected_payoff_IS_2_bet  = beliefs[1][0] * game_tree['JQ']['Bet1']['Bet2'] * -1  + beliefs[1][1] * game_tree['KQ']['Bet1']['Bet2'] * -1
    strategy_IS_2 = (np.exp(lamda * expected_payoff_IS_2_bet) / (
            np.exp(lamda * expected_payoff_IS_2_fold) + np.exp(lamda * expected_payoff_IS_2_bet)),
                     np.exp(lamda * expected_payoff_IS_2_fold) / (
                             np.exp(lamda * expected_payoff_IS_2_fold) + np.exp(lamda * expected_payoff_IS_2_bet)))
    player2_strategies.append(strategy_IS_2)
    '''FOR IS 3'''
    expected_payoff_JK_2 = opp_strategies[3][1] * game_tree['JK']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[3][
        0] * game_tree['JK']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_QK_2 = opp_strategies[4][1] * game_tree['QK']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[4][
        0] * game_tree['QK']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_IS_3_check = beliefs[2][0] * game_tree['JK']['Check1']['Check2'] * -1 + beliefs[2][1] * \
                                 game_tree['QK']['Check1']['Check2'] * -1
    expected_payoff_IS_3_bet = beliefs[2][0] * expected_payoff_JK_2 + beliefs[2][1] * expected_payoff_QK_2
    strategy_IS_3 = (np.exp(lamda * expected_payoff_IS_3_bet) / (
            np.exp(lamda * expected_payoff_IS_3_check) + np.exp(lamda * expected_payoff_IS_3_bet)),
                     np.exp(lamda * expected_payoff_IS_3_check) / (
                             np.exp(lamda * expected_payoff_IS_3_check) + np.exp(lamda * expected_payoff_IS_3_bet)))
    player2_strategies.append(strategy_IS_3)
    '''FOR IS 4'''
    expected_payoff_IS_4_fold = beliefs[3][0] * game_tree['JK']['Bet1']['Fold2'] * -1 + beliefs[3][1] * \
                                game_tree['QK']['Bet1']['Fold2'] * -1
    expected_payoff_IS_4_bet = beliefs[3][0] * game_tree['JK']['Bet1']['Bet2'] * -1 + beliefs[3][1] * \
                               game_tree['QK']['Bet1']['Bet2'] * -1
    strategy_IS_4 = (np.exp(lamda * expected_payoff_IS_4_bet) / (
            np.exp(lamda * expected_payoff_IS_4_fold) + np.exp(lamda * expected_payoff_IS_4_bet)),
                     np.exp(lamda * expected_payoff_IS_4_fold) / (
                             np.exp(lamda * expected_payoff_IS_4_fold) + np.exp(lamda * expected_payoff_IS_4_bet)))
    player2_strategies.append(strategy_IS_4)
    ''' FOR IS 5'''
    expected_payoff_KJ_2 = opp_strategies[5][1] * game_tree['KJ']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[5][
        0] * game_tree['KJ']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_QJ_2 = opp_strategies[4][1] * game_tree['QJ']['Check1']['Bet2']['Fold1'] * -1 + opp_strategies[4][
        0] * game_tree['QJ']['Check1']['Bet2']['Bet1'] * -1
    expected_payoff_IS_5_check = beliefs[4][0] * game_tree['KJ']['Check1']['Check2'] * -1 + beliefs[4][1] * \
                                 game_tree['QJ']['Check1']['Check2'] * -1
    expected_payoff_IS_5_bet = beliefs[4][0] * expected_payoff_KJ_2 + beliefs[4][1] * expected_payoff_QJ_2
    strategy_IS_5 = (np.exp(lamda * expected_payoff_IS_5_bet) / (
            np.exp(lamda * expected_payoff_IS_5_check) + np.exp(lamda * expected_payoff_IS_5_bet)),
                     np.exp(lamda * expected_payoff_IS_5_check) / (
                             np.exp(lamda * expected_payoff_IS_5_check) + np.exp(lamda * expected_payoff_IS_5_bet)))
    player2_strategies.append(strategy_IS_5)
    '''FOR IS 6'''
    expected_payoff_IS_6_fold = beliefs[5][0] * game_tree['KJ']['Bet1']['Fold2'] * -1 + beliefs[5][1] * \
                                game_tree['QJ']['Bet1']['Fold2'] * -1
    expected_payoff_IS_6_bet = beliefs[5][0] * game_tree['KJ']['Bet1']['Bet2'] * -1 + beliefs[5][1] * \
                               game_tree['QJ']['Bet1']['Bet2'] * -1
    strategy_IS_6 = (np.exp(lamda * expected_payoff_IS_6_bet) / (
            np.exp(lamda * expected_payoff_IS_6_fold) + np.exp(lamda * expected_payoff_IS_6_bet)),
                     np.exp(lamda * expected_payoff_IS_6_fold) / (
                             np.exp(lamda * expected_payoff_IS_6_fold) + np.exp(lamda * expected_payoff_IS_6_bet)))
    player2_strategies.append(strategy_IS_6)
    return player2_strategies

def level_k_strategies_player1(k,lamda):
    if k == 0:
        return [(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5)]
    else:
        opp_strategies = level_k_strategies_player2(k-1, lamda)
        information_set = information_set_prob1(opp_strategies)
        level_k_strategies = strategies_player1(lamda, opp_strategies, information_set)
        return level_k_strategies

def level_k_strategies_player2(k, lamda):
    if k == 0:
        return [(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5),(0.5,0.5)]
    else:
        opp_strategies = level_k_strategies_player1(k-1, lamda)
        information_set = information_set_prob2(opp_strategies)
        level_k_strategies = strategies_player2(lamda, opp_strategies, information_set)
        return level_k_strategies




def game_play(player1_level, player2_level, rational_parameter):
    strategy_player1 = level_k_strategies_player1(player1_level, 20)
    nash_strategy = [(0,1),(1/3,2/3),(1,0),(1,0),(1/3,2/3),(0,1)]
    strategy_player2 = level_k_strategies_player2(player2_level, 20)
    card_hands = ['JK','JQ','QJ','QK','KJ','KQ']
    expected_payoff = 0
    for hand in card_hands:
        player1_card = hand[0]
        player2_card = hand[1]
        '''Player 1 Bets and Player 2 Bets'''
        payoff = player1_strategy(player1_card, 1, strategy_player1)[0] * player2_strategy(player2_card,'Bet',strategy_player2)[0] * game_tree[hand]['Bet1']['Bet2']
        expected_payoff = expected_payoff + payoff
        '''Player 1 Bets and Player 2 Folds'''
        payoff = player1_strategy(player1_card, 1, strategy_player1)[0] * player2_strategy(player2_card,'Bet',strategy_player2)[1] * game_tree[hand]['Bet1']['Fold2']
        expected_payoff = expected_payoff + payoff
        '''Player 1 Checks and Player 2 Checks'''
        payoff = player1_strategy(player1_card, 1,strategy_player1)[1] * player2_strategy(player2_card,'Check',strategy_player2)[1] * game_tree[hand]['Check1']['Check2']
        expected_payoff = expected_payoff + payoff
        '''Player 1 Checks and Player 2 Bets and Player 1 Bets'''
        payoff = player1_strategy(player1_card, 1, strategy_player1)[1] * player2_strategy(player2_card, 'Check',strategy_player2)[0] * player1_strategy(player1_card, 2,strategy_player1)[0] * game_tree[hand]['Check1']['Bet2']['Bet1']
        expected_payoff = expected_payoff + payoff
        '''Player 1 Checks and Player Bets and Player 1 Folds'''
        payoff = player1_strategy(player1_card, 1, strategy_player1)[1] * \
                 player2_strategy(player2_card, 'Check', strategy_player2)[0] * \
                 player1_strategy(player1_card, 2, strategy_player1)[1] * game_tree[hand]['Check1']['Bet2']['Fold1']
        expected_payoff = expected_payoff + payoff
    expected_payoff = expected_payoff/6
    return expected_payoff
    #strategies_1 = [(0.6, 0.4),(0.5, 0.5),(0.7,0.3),(0.34,0.66),(0.87,0.13),(0.27,0.73)]
    #strategies_2 = [(0.12,0.88),(0.45,0.55),(0.28,0.72),(0.39,0.61),(0.67,0.33),(0.9,0.1)]
    #print(information_set_prob1(strategies_2))
    #print(information_set_prob2(strategies_1))
    #card_shuffle = np.random.choice(cards)
    #print(card_shuffle)
    #actions = []
    #player1_card = card_shuffle[0]
    #player2_card = card_shuffle[1]
    #player1_reward = 0
    #player2_reward = 0
    #print('Action 1(P1)...')
    #strategy_prob = player1_strategy(player1_card, 1, strategies_1)
    #num = np.random.randn()
    #if num < strategy_prob[0]:
    #    print('Player 1: Bets')
    #    actions.append('Bet1')
    #else:
    #    print('Player 1: Checks')
    #    actions.append('Check1')
    #print('Action 2(P2)...')
    #opp_action = actions[0][:-1]
    #strategy_prob = player2_strategy(player2_card, opp_action, strategies_2)
    #num = np.random.randn()
    #if num < strategy_prob[0]:
    #    print('Player 2: Bets')
    #    actions.append('Bet2')
    #    if actions[0] == 'Bet1':
    #        return game_tree[card_shuffle][actions[0]][actions[1]]
    #else:
    #    if actions[0] == 'Check1':
    #        print('Player 2: Checks')
    #        actions.append('Check2')
    #    else:
    #        print('Player 2: Folds')
    #        actions.append('Fold2')
    #    return game_tree[card_shuffle][actions[0]][actions[1]]
    #print('Action 3(P1)...')
    #strategy_prob = player1_strategy(player1_card,2,strategies_1)
    #num = np.random.randn()
    #if num < strategy_prob[0]:
    #    print('Player 1: Bets again')
    #    actions.append('Bet1')
    #    return game_tree[card_shuffle][actions[0]][actions[1]][actions[2]]
    #else:
    #    print('Player 1: Folds')
    #    actions.append('Fold1')
    #    return game_tree[card_shuffle][actions[0]][actions[1]][actions[2]]





if __name__ == '__main__':
    print(level_k_strategies_player1(2, 20))
    print_hi('PyCharm')
    print ("")
    rational_par = [0.1,0.2,0.25,0.3,0.4,0.5,0.75,1,2.5,4,6,10,20]
    player_exp_payoff = []
    level_4_payoff = []
    for rational_parameter in rational_par:
        player_1_payoff = []
        for i in range(10):
            print('Level ', i, end=",")
            for j in range(10):
                payoff = game_play(i, j, rational_parameter) #playing games P1 vs P2 across levels
                print(payoff, end=",")
                player_1_payoff.append(payoff)
                if j == 7:
                    level_4_payoff.append(payoff)

            print(" ")
        player_exp_payoff.append(sum(player_1_payoff)/len(player_1_payoff)) #avg payoff for a particular rational level
    print (player_exp_payoff)
    rational_par_str = ['0.1','0.2','0.25','0.3','0.4','0.5','0.75', '1', '2.5', '4', '6', '10','20']
    plt.plot(rational_par,player_exp_payoff)
    plt.title('Expected Payoff for the game with change in rational parameter')
    plt.xlabel('rational parameter')
    plt.ylabel('expected payoff')
    plt.show()



    print (game_play(3, 2, rational_parameter))
    print(game_play(3, 2, rational_parameter))
    print(information_set_prob1([[1,0],[1,0],[1,0],[1,0],[1,0],[0,1]]))
    print(level_k_strategies_player1(5,20))
    print(level_k_strategies_player1(6, 20))
    print(level_k_strategies_player1(7, 20))
    print(level_k_strategies_player1(8, 20))
    print('\n')
    print(level_k_strategies_player2(7, 20))
    print(level_k_strategies_player2(8, 20))
    print(sum(level_4_payoff)/len(level_4_payoff))
    #print(information_set_prob2([(0.6,0.4), (0.5,0.5), (0.9,0.1), (0.4,0.6),(0.8,0.2),(0.35,0.65)]))
    #print('payoff =', game_tree['JQ']['Check1']['Bet2']['Bet1'])
