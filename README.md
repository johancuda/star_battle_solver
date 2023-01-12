# Star Battle solver

The code used here is taken from [here](https://www.reddit.com/r/dailyprogrammer/comments/7xyi2w/20180216_challenge_351_hard_star_battle_solver/). This repo's sole purpose is to explain how to use it.

We also corrected a little typo in the script.

## How to test the solver

1. Install [PuLP](https://pypi.org/project/PuLP/).
2. If you run the script and an error about GLPK missing pops, install GLPK. (I had a few problems with this, if you do also refer to [this](https://stackoverflow.com/questions/51873735/how-to-add-glpk-solver-on-pulp-python)).
3. You can now run the solver!

## How to encore your puzzle grid

A test grid should be like this `test_grid = """1\nAABBCC\nAABCCC\nAABCCC\nDDBBEE\nDDBBEF\nDDBBFF"""`

1. The first character is the number of trees per zones/lines/columns followed by a new line.
2. Each zone is defined by a letter.
3. Each line is seperated from the other by a new line.