'''
# Minimax SumX

An optimal strategy for SumX using minimax.


SumX is a two player zero-sum game consisting of X rounds. Each round, a player may choose a number between 0 and Y to add to the "running total" which starts at 0. Each player's aim is to ensure the total reaches exactly X on the final round. If they succeed then they win; otherwise the second player wins. 

This game can be played optimally using a minimax strategy. For small X and Y, the game can be played perfectly using a minimax strategy.
:wq
'''


from typing import Tuple, Iterator
from dataclasses import dataclass


@dataclass
class SumXOptions:
	"""
	Stores options/settings for a SumX game.
	"""

	x: int = 5 # Number of rounds.
	y: int = 2 # Number of actions to chose from each round.



@dataclass
class SumXState:
	"""
	Stores the state of a SumX game.
	"""

	sum: int = 0
	round: int = 0


@dataclass
class SumXAction:
	
	number: int = 0


@dataclass
class SumXPlayer:

	options: SumXOptions


	def __call__(self, state: SumXState) -> SumXAction:
		raise NotImplementedError()


class SumXGame:
	pass


@dataclass
class SumXGame:
	
	options: SumXOptions
	players: Tuple[SumXPlayer, SumXPlayer]
	state: SumXState = SumXState()


	def play(self) -> Iterator[SumXGame]:

		if self.state.round == self.options.x:
			return

		player = self.players[self.state.round % 2]
		action = player(self.state)

		game = SumXGame(
			options = self.options,
			players = self.players,
			state = SumXState(
				sum = self.state.sum + action.number,
				round = self.state.round + 1,
			),
		)

		yield game
		yield from game.play()
