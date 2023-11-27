from collections import namedtuple


Card = namedtuple("Card",['rank','suit'])


class Frenchdeck:
	ranks = [str(n) for n in range(2,11)] + list("JQKA")
	suits = "spades diamonds clubs hearts".split()

	def __init__(self):
		self._card = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):
		return len(self._card)

	def __getitem__(self,position):
		return self._card[position]




if __name__ == '__main__':
    bendeck = Frenchdeck()
    print(bendeck[12::13])
    print(Card("Q","diamonds") in  bendeck)
    from random import choice
    print(choice(bendeck)._asdict())
    print(bendeck[0]._make(["1","2"]))
    print(bendeck._card)