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
