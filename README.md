# SumX AI

An AI which solves the game SumX using [minimax](https://en.wikipedia.org/wiki/minimax).


## Overview

SumX is a two player zero-sum game consisting of $X$ rounds. Each round, a player may choose a number between 0 and $Y$ to add to the "running total" which starts at 0. The first player's aim is to ensure that the total reaches exactly $X$ on the final round. If they succeed then they win; otherwise the second player wins. This game can be played optimally using a minimax strategy. For large $X$ and $Y$, heuristics may need be to used; however in this implementation we mainly focus on small games (e.g. $X=5$, $Y=3$). In this case, the non-trivial game can be solved *perfectly* using minimax. 

An alternative variant of SumX allows $X$ to be reached by any player on any round but keeps the number of actions below another constant $K$. This can also be solved with minimax, however often this version uses a large $Y$ (say $Y = 20$) which may require heuristics or alpha-beta pruning to maintain efficiency. 


## Examples

We show several example SumX games with $X = 5$ and $Y = 3$.

Example 1:

```
Player    Action    Sum
AI        1         1
Human     1         2
AI        1         3
Human     0         3
AI        2         5

Winner: AI
```

Example 2:

```
Player    Action    Sum
AI        1         1
Human     2         3
AI        0         3
Human     1         4
AI        1         5

Winner: AI
```

Example 3:

```
Player    Action    Sum
AI        1         1
Human     0         1
AI        1         2
Human     0         2
AI        2         5

Winner: AI
```
