# https://atcoder.jp/contests/past201912-open/tasks/past201912_h

from typing import List
import math


class CardManager:

    cards = None

    # 毎回最小値を検索するのではなくメモ化
    min_ev = None
    min_z = None

    # セット取引回数もメモ化
    sng = 0
    ev = 0
    z = 0

    def __init__(self, cards: List[int]) -> None:
        CardManager.cards = cards
        CardManager.min_ev = min(cards[::2])
        CardManager.min_z = min(cards)

    @classmethod
    def sold_num(cls) -> int:
        sold_ev = cls.ev * math.ceil(len(cls.cards) / 2)
        sold_z = cls.z * len(cls.cards)
        return cls.sng + sold_ev + sold_z

    @classmethod
    def deal(cls, query: str) -> None:
        q = [int(num) for num in query.split()]

        if q[0] == 1:
            idx = q[1]-1
            if idx % 2 == 0:
                if cls.cards[idx] - cls.ev - cls.z >= q[2]:
                    val = cls.cards[idx] - q[2]
                    cls.cards[idx] = val
                    cls.min_ev = min(cls.min_ev, val)  # 偶数のみ
                    cls.min_z = min(cls.min_z, val)
                    cls.sng += q[2]
            else:
                if cls.cards[idx] - cls.z >= q[2]:
                    val = cls.cards[idx] - q[2]
                    cls.cards[idx] = val
                    cls.min_z = min(cls.min_z, val)
                    cls.sng += q[2]
        elif q[0] == 2:
            if cls.min_ev >= q[1]:
                cls.ev += q[1]  # 取引枚数更新
                cls.min_ev -= q[1]
                cls.min_z = min(cls.min_z, cls.min_ev)
        else:
            if cls.min_z >= q[1]:
                cls.z += q[1]  # 取引枚数更新
                cls.min_z -= q[1]
                cls.min_ev -= q[1]


if __name__ == '__main__':
    n = int(input())
    org_cards = [int(c) for c in input().split()]
    CardManager(org_cards)  # 変数に格納しなくてもよい
    q = int(input())

    for i in range(q):
        # クラスメソッドはインスタンスを経由してもしなくてもよい
        CardManager.deal(input())

    print(CardManager.sold_num())
