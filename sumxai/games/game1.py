from .. import SumXGame, SumXOptions
from .. players import RandomSumXPlayer, InteractiveSumXPlayer


options = SumXOptions()
player1 = InteractiveSumXPlayer(options)
player2 = RandomSumXPlayer(options)
game = SumXGame(options = options, players = [ player1, player2 ])


for game_step in game.play():
	print('total sum is: ' + str(game_step.state.sum))


end = game_step

if end.state.sum == options.x:
	print('Player 1 WINS!!!')

else:
	print('Player 2 WINS!!!')

