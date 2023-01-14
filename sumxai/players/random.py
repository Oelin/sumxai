from .. import SumXPlayer, SumXAction, SumXState

import random


class RandomSumXPlayer(SumXPlayer):

        def __call__(self, state: SumXState) -> SumXAction:
                return SumXAction(number = random.randint(0, self.options.y))
