#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : pukepai.py
# @Time      : 2018/6/1 15:06
# @software  : PyCharm

from random import randint, randrange


class Card(object):
    ''' 一张牌 '''

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        all_suites = ('♠', '♥', '♣', '♦')
        if self.face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (all_suites[self._suite], face_str)


class Poker(object):
    ''' 一副牌'''

    def __init__(self):
        self._cards = []
        self._current = 0
        for suite in range(4):
            for face in range(1,14):
                card = Card(suite, face)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        ''' 洗牌机'''
        self._current = 0
        cards_len = len(self._cards)
        for index in range(cards_len):
            pos = randrange(cards_len)
            self._cards[index], self._cards[pos] = self._cards[pos], self._cards[index]

    @property
    def next(self):
        ''' 发牌阶段 '''

        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)


class Player(object):
    ''' 玩家'''

    def __init__(self, name):
        self._name =  name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        ''' 摸牌'''
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        ''' 整理牌面'''
        self._cards_on_hand.sort(key=card_key)


def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        for card in player.cards_on_hand:
            print(card, end=' ')
        print()


if __name__ == '__main__':
    main()
