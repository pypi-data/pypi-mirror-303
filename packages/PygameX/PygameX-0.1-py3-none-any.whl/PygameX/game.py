import pygame

import PygameX.color as color
import PygameX.key as key
import PygameX.math as math

class Game:

    """
    Main game class
    """

    background_color = (0,0,0)
    object_render_mode = False
    objects = {}
    
    def __init__(self, width: int = 100, height: int = 100, caption: str = "PygameX Game", max_fps: int = 60):
        self.width = width
        self.height = height
        self.max_fps = max_fps
        
        pygame.init()
        self.init()
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        clock = pygame.time.Clock()

        self.running = True
        self.ready()
        
        while self.running:
            self.update()
            
            # events
            for e in pygame.event.get():
                self.on_event(e)

                if e.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                    if 1 <= e.button <= 3:
                        self.on_mouse_pressed((pygame.mouse.get_pos(), e.button, pygame.mouse.get_pressed()[e.button-1]))
            
            # rendering
            self.render()
            
            # visualization
            pygame.display.flip()
            
            clock.tick(self.max_fps)

        pygame.quit()
        self.on_quit()

    def init(self):
        pass

    def ready(self):
        pass

    def quit(self):
        self.running = False

    def on_quit(self):
        pass

    def on_mouse_pressed(self, mouse):
        pass

    def update(self):
        pass

    def on_event(self, event):
        if event.type == key.QUIT:
            self.running = False
    
    def render(self):
        self.screen.fill(self.background_color)
        if self.object_render_mode:
            for obj in self.objects.keys():
                self.objects[obj].render(self.screen)
