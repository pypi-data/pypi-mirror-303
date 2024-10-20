
# PyGameX

### Description

An easy-to-learn library that makes Pygame more structured and user-friendly. The library has many built-in functions that simplify development at times.
## Usage/Examples

#### Empty template
```python
import PygameX as pygamex

class MainGame(Game):
    pass

MainGame(height=300, width=500, max_fps=60)
```

#### Simple game

```python
import PygameX as pygamex

from PygameX.game import *
from PygameX.all_objects import *

from random import randint


class MainGame(Game):
    background_color = color.BLUE
    object_render_mode = True

    def ready(self):
        player = Circle(
            position=(50, 50),
            radius=25,
            color=(0, 255, 0)
        )
        self.objects["player"] = player

    def on_event(self, event):
        super().on_event(event)

    def on_mouse_pressed(self, mouse):
        if mouse[1] == 1:
            if mouse[2] == True:
                player = self.objects["player"]
                if pygamex.math.distance_to(mouse[0], player.position) < player.radius:
                    player.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        player = self.objects["player"]
        keys = pygamex.key.get_pressed()
        if keys[pygamex.key.LEFT]:
            player.position = (player.position[0] - 3, player.position[1])
        if keys[pygamex.key.RIGHT]:
            player.position = (player.position[0] + 3, player.position[1])
        if keys[pygamex.key.UP]:
            player.position = (player.position[0], player.position[1] - 3)
        if keys[pygamex.key.DOWN]:
            player.position = (player.position[0], player.position[1] + 3)


MainGame(width=500, height=300, max_fps=60)
```
## API Reference

### Game class init

```python
MainGame(width=500, height=300, caption="My first PagameX game!", max_fps=60)
```

| Parameters | Type     | Description                                 |
|:-----------|:---------|:--------------------------------------------|
| `width`    | `int`    | Sets the width of the screen                |
| `height`   | `int`    | Sets the height of the screen               |
| `caption`  | `string` | Sets the title of the game                  |
| `max_fps`  | `int`    | Sets the max frame rate of the game process |

### Game class methods

#### Ready
```python
def ready(self):
    pass
```
Called when the game window has been created and started.

#### Init
```python
def init(self):
    pass
```
Called before starting the game and initializing pygame.

#### On quit
```python
def on_quit(self):
    pass
```
Called when the game is closed.

#### Quit
```python
quit()
```
Completes the game cycle.

#### Update
```python
def update(self):
    pass
```
Called every time, before rendering and processing the keys.

#### Render
```python
def render(self):
    pass
```
Called every time to draw objects.

#### On event (event)
```python
def on_event(self, event):
    pass
```
Called every time an interaction event occurs (Includes keystroke events).

| Parameter | Type           | Description                                                      |
|:----------|:---------------|:-----------------------------------------------------------------|
| `event`   | `pygame event` | Pygame event about a pressed key or a set of keys and its status |

#### On mouse pressed (key)
```python
def on_mouse_pressed(self, mouse):
    pass
```
Called every time an interaction event occurs.

| Parameter | Type    | Description                                                              |
|:----------|:--------|:-------------------------------------------------------------------------|
| `mouse`   | `tuple` | An immutable list containing the `position`, `pressed key`, `is pressed` |

#### Object render mode
PygameX adds the ability to use objects instead of manually drawing shapes.

To enable this mode, just set `object_render_mode` to `True` in your game class.
```python
object_render_mode = True
```

All that remains to be done is to add objects to the `objects` dictionary.

#### Object
`object` is the main class of all objects in PygameX, it is usually not used in games because it is a dummy that exists to create other objects such as `line`, `circle`, `rect`.

It has a `render` function for displaying an object on the game screen.

#### Rect
The object inheriting the `object` having 3 settings: `position` `size` `color`.

Initializing template:
```python
rect(
    position=(50,50),
    size=(25,25),
    color=(0,255,0)
)
```

#### Circle
The object inheriting the `object` having 3 settings: `position` `radius` `color`.

Initializing template:
```python
circle(
    position=(50,50),
    radius=25,
    color=(0,255,0)
)
```

#### Line
The object inheriting the `object` having 3 settings: `point1` `point2` `color`.

Initializing template:
```python
line(
    point1=(50,50),
    point2=(25,25),
    color=(0,255,0)
)
```

## Installation

Install my library using `pip` in CMD or PyCharm Console:

```bash
  pip install PygameX
```
    
## Authors

- [@k0cteJl](https://www.github.com/k0cteJl)

