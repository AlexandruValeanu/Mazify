# Mazify

Mazify is a tool that can be used to generate and solve mazes.
There is also a game module written using Pygame if you'd like to see how fast can you solve a maze.

### Creating a maze
```python
python3 main.py create rows=10 columns=20 file-path='mazes/small'
```

### Solving a maze
```python
python3 main.py solve 'start=(1,1)' 'end=(7,6)' file-path='mazes/small.txt'
```

### Playing a game
```python
python3 main.py play file-path='mazes/small.txt'
```

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