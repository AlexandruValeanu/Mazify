# Mazify

Mazify is a tool that can be used to generate and solve mazes.
There is also a game module written using Pygame if you'd like to see how fast can you solve a maze.

### Creating a maze
```python
python3 main.py create rows=10 columns=20 file-path='mazes/small'
```
![small maze](https://github.com/AlexandruValeanu/Mazify/blob/master/mazes/small.png)

```python
python3 main.py create rows=100 columns=200 file-path='mazes/big'
```
![big maze](https://github.com/AlexandruValeanu/Mazify/blob/master/mazes/big.png)

### Solving a maze
```python
python3 main.py solve 'start=(1,1)' 'end=(7,6)' file-path='mazes/small.txt'
```
![small maze](https://github.com/AlexandruValeanu/Mazify/blob/master/mazes/small_sol.png)

```python
python3 main.py solve 'start=(34,19)' 'end=(76,163)' file-path='mazes/big.txt'
```
![big maze](https://github.com/AlexandruValeanu/Mazify/blob/master/mazes/big_sol.png)
![big maze dfs](https://github.com/AlexandruValeanu/Mazify/blob/master/mazes/big_sol_dfs.png)

### Playing a game
```python
python3 main.py play file-path='mazes/big.txt'
```
![game](https://github.com/AlexandruValeanu/Mazify/blob/master/Peek%202017-10-02%2012-14.gif)

### Maze solvers
There are 3 maze-solvers implemented:
* ![Depth-first search maze-solver](https://github.com/AlexandruValeanu/Mazify/blob/master/solvers/dfs_solver.py)
* ![Breadth-first search maze-solver](https://github.com/AlexandruValeanu/Mazify/blob/master/solvers/bfs_solver.py)
* ![A* graph-search maze-solver](https://github.com/AlexandruValeanu/Mazify/blob/master/solvers/astar_solver.py)

###  Key controls
* z  -> Highlight current location
* x  -> Highlight destination
* t  -> Show solution from current location
* c  -> Decrease frame rate
* v  -> Increase frame rate
* f  -> Show frame rate
* Arrows or WASD for movement

### Stuff used to make this:
* [pygame](https://www.pygame.org/news) for the game module
* [tkinter](https://wiki.python.org/moin/TkInter) for basic GUI
* [matplotlib](https://matplotlib.org/) for drawing mazes
* [numpy](http://www.numpy.org/) for representing mazes
