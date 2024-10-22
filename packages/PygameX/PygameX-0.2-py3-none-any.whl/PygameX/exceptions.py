class FontInitException(Exception):
    def __init__(self, message="The Pygame font is not initialized!"):
        self.message = message
        super().__init__(self.message)
