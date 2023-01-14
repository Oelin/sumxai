from .. import SumXPlayer, SumXAction, SumXState


class InteractiveSumXPlayer(SumXPlayer):

        def __call__(self, state: SumXState) -> SumXAction:

                number = 0

                while 1:
                        number = input(f'[?] Enter a number between 0 and {self.options.y}: ')

                        if not number.isnumeric():
                                print('[!] Must enter a number')
                                continue

                        number = int(number)

                        if not number in range(self.options.y + 1):
                                print(f'[!] Must enter a numbrer between 0 and {self.options.y}')
                                continue

                        break

                return SumXAction(number = number)
