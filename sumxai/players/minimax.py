from .. import SumXPlayer, SumXAction, SumXState

from typing import List
import numpy as np


class MinimaxSumXPlayer(SumXPlayer):

    def __call__(self, state: SumXState) -> SumXAction:

        a = SumXAction(
                number = np.argmax(self.get_action_values(state)),
        )

        print(f'minimax choosing: {a}')
        return a


    def get_action_values(self, state: SumXState, is_max=True) -> List[int]:

        return [
                self.minimax(SumXState(
                        sum = state.sum + number,
                        round = state.round + 1,
                ), not is_max)

                for number in range(self.options.y + 1)
        ]


    def minimax(self, state: SumXState, is_max=True) -> int:

        is_leaf = state.round == self.options.x

        if is_leaf:
            assert not is_max
            return state.sum == self.options.x

        else:
            action_values = self.get_action_values(state, is_max)
            return max(action_values) if is_max else min(action_values)
