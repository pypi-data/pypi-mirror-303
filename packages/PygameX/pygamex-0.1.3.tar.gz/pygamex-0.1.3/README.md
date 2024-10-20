
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
import PygameX

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
            if mouse[2]:
                player = self.objects["player"]
                if PygameX.math.is_point_inside_circle(mouse[0], player):
                    player.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        player = self.objects["player"]
        keys = PygameX.key.get_pressed() # List of pressed keys
        if keys[PygameX.key.LEFT]:
            player.position = (player.position[0] - 3, player.position[1])
        if keys[PygameX.key.RIGHT]:
            player.position = (player.position[0] + 3, player.position[1])
        if keys[PygameX.key.UP]:
            player.position = (player.position[0], player.position[1] - 3)
        if keys[PygameX.key.DOWN]:
            player.position = (player.position[0], player.position[1] + 3)


MainGame(width=500, height=300, max_fps=60)
```
## API Reference

### Game class init

```python
class MainGame(Game):
    pass

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

| Parameter | Type    | Description                                                                                          |
|:----------|:--------|:-----------------------------------------------------------------------------------------------------|
| `mouse`   | `tuple` | An immutable list containing the `position: tuple`, `pressed key: pygame key`, `is pressed: boolean` |

#### Object render mode
PygameX adds the ability to use objects instead of manually drawing shapes.

To enable this mode, just set `object_render_mode` to `True` in your game class.
```python
object_render_mode = True
```

All that remains to be done is to add objects to the `objects` dictionary.

#### Object
`Object` is the main class of all objects in PygameX, it is usually not used in games because it is a dummy that exists to create other objects such as `line`, `circle`, `rect`.

It has a `render` function for displaying an object on the game screen.

#### Rect
The object inheriting the `Object` having 3 settings: `position` `size` `color`.

Initializing template:
```python
Rect(
    position=(50,50),
    size=(25,25),
    color=(0,255,0)
)
```

#### Circle
The object inheriting the `Object` having 3 settings: `position` `radius` `color`.

Initializing template:
```python
Circle(
    position=(50,50),
    radius=25,
    color=(0,255,0)
)
```

#### Line
The object inheriting the `Object` having 3 settings: `point1` `point2` `color`.

Initializing template:
```python
Line(
    point1=(50,50),
    point2=(25,25),
    color=(0,255,0)
)
```

### Creating your own object
Any objects should inherit `Object` because it contains the `render` function and is simply more convenient than creating a new class manually. As a result, the dummy of the new class will look like this:
```python
import pygame
from .Object import Object

class MyCustomObject(Object):

    def __init__(self):
        pass
    
    def render(self, screen):
        pass
```

Let's add the variables `position` and `color` inside.
```python
import pygame
from .Object import Object

class MyCustomObject(Object):

    position = (0,0)
    color = (0,0,0)
    
    def __init__(self, position: tuple = (0,0), color: tuple = (0,0,0)):
        self.position = position
        self.color = color
    
    def render(self, screen):
        pass
```

Now in the `render` method we will draw our object. In the example, a 50x50 square is simply drawn using our values.
```python
import pygame
from .Object import Object

class MyCustomObject(Object):

    position = (0,0)
    color = (0,0,0)
    
    def __init__(self, position: tuple = (0,0), color: tuple = (0,0,0)):
        self.position = position
        self.color = color
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, (50, 50)))
```

Now let's try out our object in the game. Let's replace the circle from the example above with our object
First, let's save our script in `MyCustomObject`, and then import it into the game.
```python
import PygameX

from PygameX.game import *
from PygameX.all_objects import *
from .MyCustomObject import MyCustomObject # I immediately import the object

from random import randint


class MainGame(Game):
    background_color = color.BLUE
    object_render_mode = True

    def ready(self):
        player = MyCustomObject(
            position=(50, 50),
            radius=25,
            color=(0, 255, 0)
        )
        self.objects["player"] = player

    def on_event(self, event):
        super().on_event(event)

    def on_mouse_pressed(self, mouse):
        if mouse[1] == 1:
            if mouse[2]:
                player = self.objects["player"]
                if PygameX.math.is_point_inside_circle(mouse[0], player):
                    player.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        player = self.objects["player"]
        keys = PygameX.key.get_pressed()
        if keys[PygameX.key.LEFT]:
            player.position = (player.position[0] - 3, player.position[1])
        if keys[PygameX.key.RIGHT]:
            player.position = (player.position[0] + 3, player.position[1])
        if keys[PygameX.key.UP]:
            player.position = (player.position[0], player.position[1] - 3)
        if keys[PygameX.key.DOWN]:
            player.position = (player.position[0], player.position[1] + 3)


MainGame(width=500, height=300, max_fps=60)
```

### Scripts
The library provides a quick import of all objects from the library.
```python
from PygameX.all_objects import *
```
If you don't need to import all the objects, you can import them individually.
```python
from .objects.Rect import Rect # Rect
from .objects.Circle import Circle # Circle
from .objects.Line import Line # Line
from .objects.TextDisplay import TextDisplay # Text
```

### Convenient functions
PygameX provides functions for working with objects quickly.

#### List of additional functions:

is_point_inside_circle(point: tuple, circle: Circle)
```python
PygameX.math.is_point_inside_circle(mouse_position, my_circle)
```

is_point_inside_rect(point: tuple, rect: Rect)
```python
PygameX.math.is_point_inside_rect(mouse_position, my_rect)
```

## Installation

Install my library using `pip` in CMD or PyCharm Console:

```bash
pip install PygameX
```
    
## Authors

- [@k0cteJl Github](https://www.github.com/k0cteJl)