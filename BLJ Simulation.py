import random

basic_strategy_hard = {5: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       6: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       7: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       8: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       9: {2: 'hit', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       10: {2: 'dd', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'dd', 8: 'dd', 9: 'dd', 10: 'hit', 11: 'hit'},
                       11: {2: 'dd', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'dd', 8: 'dd', 9: 'dd', 10: 'dd', 11: 'hit'},
                       12: {2: 'hit', 3: 'hit', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       13: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       14: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       15: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       16: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       17: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       18: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       21: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'}}

basic_strategy_soft = {13: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       14: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       15: {2: 'hit', 3: 'hit', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       16: {2: 'hit', 3: 'hit', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       17: {2: 'hit', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                       18: {2: 'stand', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'stand', 8: 'stand', 9: 'hit', 10: 'hit', 11: 'hit'},
                       19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                       21: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'}}

basic_strategy_pairs = {2: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                        3: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                        4: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'dd', 6: 'dd', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                        5: {2: 'dd', 3: 'dd', 4: 'dd', 5: 'dd', 6: 'dd', 7: 'dd', 8: 'dd', 9: 'dd', 10: 'hit', 11: 'hit'},
                        6: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                        7: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
                        8: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 11: 'split'},
                        9: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'stand', 8: 'split', 9: 'split', 10: 'stand', 11: 'stand'},
                        10: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
                        11: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 11: 'split'}}


class Deck:
    def __init__(self):

        # 4 deck game
        self.unused_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.used_deck = []

    def shuffle(self):
        random.shuffle(self.unused_deck)

    def take_card(self):  # removes first item in unused deck and puts it in used deck
        card = self.unused_deck.pop(0)
        self.used_deck.append(card)
        return card


class Player:
    _NextID = 1

    def __init__(self):
        self.player_ID = Player._NextID
        self.balance = random.randint(100, 1000)
        self.original_balance = self.balance  # to keep track of profits
        self.profits = 0
        self.profits_per_round = 0
        Player._NextID += 1

        self.hands = []

    def end_of_round(self):  # To be used in Round after wins and losses are declared
        self.profits += self.profits_per_round

        cards_list = ''
        for g in self.hands:
            cards_list += str(g.cards)
        details = '\nPlayer: ' + str(self.player_ID) + '\nCards/Hands: ' + cards_list + \
                  '\nProfit p Round: ' + str(self.profits_per_round) + '\nProfits Total: ' + str(self.profits)
        self.hands = []
        self.profits_per_round = 0
        return details


class Hand:
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.bust = False
        self.BJ = False

    def set_card(self, card):
        self.cards.append(card)

    def set_bet(self, bet):
        self.bet = bet

    def play(self,  dealers_upcard):
        if self.cards[0] + self.cards[1] == 21:  # if blackjack
            action = 'BJ'

        elif sum(self.cards) > 21 and 11 not in self.cards:  # only a hard value will bust
            action = 'bust'

        elif self.cards[0] == self.cards[1]:  # if pairs
            action = basic_strategy_pairs[self.cards[0]][dealers_upcard]

        elif 11 in self.cards and sum(self.cards) > 21:  # if another card is taken and bust, change ace to 1
            for n, i in enumerate(self.cards):
                if i == 11:
                    self.cards[n] = 1
            total = sum(self.cards)
            action = basic_strategy_hard[total][dealers_upcard]

        elif 11 in self.cards:  # if there's an 11, then soft (11s turn to 1s when needed)
            total = sum(self.cards)
            action = basic_strategy_soft[total][dealers_upcard]

        else:  # every other hand is hard
            total = sum(self.cards)
            action = basic_strategy_hard[total][dealers_upcard]

        return action

    def hit(self):
        new_card = game.deck.take_card()
        self.cards.append(new_card)
        print(self.cards)

    def double_down(self):
        self.bet = self.bet * 2
        new_card = game.deck.take_card()
        self.cards.append(new_card)
        print(self.cards)

    def split(self, player):
        self.cards.pop(-1)

        hand = Hand()
        hand.set_card(self.cards[0])
        hand.set_bet(self.bet)
        player.hands.append(hand)


        self.hit()
        hand.hit()

        print(self.cards, hand.cards)

    def winBJ(self, player):
        player.balance += 1.5*int(self.bet)
        player.profits_per_round += 1.5*int(self.bet)

    def win(self, player):
        player.balance += int(self.bet)
        player.profits_per_round += int(self.bet)

    def lose(self, player):
        player.balance -= int(self.bet)
        player.profits_per_round += -int(self.bet)


class Dealer:
    def __init__(self):
        self.cards = []
        self.upcard = 0

    def set_card(self, card):
        self.cards.append(card)

    def end_of_round_dealer(self):
        self.cards = []

    def play_dealer(self):
        bust = False
        BJ = False

        if self.cards == 21:
            BJ = True

        while sum(self.cards) < 17:
            self.hit()

        if sum(self.cards) > 21:
            bust = True

        return bust, BJ, sum(self.cards)

    def hit(self):
        new_card = game.deck.take_card()
        self.cards.append(new_card)


class Round:

    def deal_cards(self):

        for g in game.players:
            hand = Hand()
            g.hands.append(hand)
            for i in range(2):
                card = game.deck.take_card()
                g.hands[0].set_card(card)

        for f in game.players:
            f.hands[0].set_bet(5)  # FIND HOW TO PICK BET SIZE

        card = game.deck.take_card()  # setting dealers upcard and cards
        game.dealer.upcard = card
        game.dealer.cards.append(card)
        card = game.deck.take_card()
        game.dealer.cards.append(card)

        for x in game.players:
            for y in x.hands:
                print('Player ' + str(x.player_ID) + "'s cards:", y.cards)

        print("\nDealer's card:", game.dealer.upcard)

        self.play_round()

    def play_round(self):
        for j in game.players:
            for k in j.hands:
                print('\nnew hand:', k.cards)
                action = None
                while action != 'stand' and action != 'bust' and action != 'dd':
                    action = k.play(game.dealer.upcard)
                    print(action)

                    if action == 'BJ':
                        k.BJ = True
                        action = 'stand'

                    elif action == 'hit':
                        k.hit()

                    elif action == 'dd':
                        k.double_down()

                    elif action == 'split':
                        k.split(j)

                    if sum(k.cards) > 21:
                        k.bust = True
                        action = 'bust'
                print(sum(k.cards))

        bust, BJ, dealer_total = game.dealer.play_dealer()

        print('\nDealer: ', game.dealer.cards, '\n', sum(game.dealer.cards))

        for p in game.players:

            win = False
            lose = False

            for h in p.hands:
                if h.bust:  # if player busts automatic loss
                    h.lose(p)
                    lose = True

                elif BJ and h.BJ:  # both player and dealer have blackjacks
                    continue

                elif h.BJ:  # only player has blackjack
                    h.winBJ(p)
                    win = True

                elif BJ:  # only dealer has blackjack
                    h.lose(p)
                    lose = True

                elif bust:  # if dealer busts and player doesn't. If player busts, automatic loss
                    h.win(p)
                    win = True

                elif dealer_total > sum(h.cards):  # if dealer had greater total
                    h.lose(p)
                    lose = True

                elif dealer_total < sum(h.cards):  # win if total greater than dealer's
                    h.win(p)
                    win = True

                elif dealer_total == sum(h.cards):  # tie if same total
                    continue

            var = p.end_of_round()
            print(var)
            if win:
                print('Win')
            elif lose:
                if h.bust:
                    print('Bust')
                print('Lose')
            else:
                print('Tie')

        print('\n')
        game.dealer.cards = []


class Game:
    players = []
    deck = Deck()
    dealer = Dealer()
    deck.shuffle()

    def start_game(self):

        # rand_val = random.randint(2, 6)
        for r in range(3):
            player = Player()
            self.players.append(player)

        for x in range(5):
            self.roundd = Round()
            self.roundd.deal_cards()


game = Game()
game.start_game()






