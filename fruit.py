import pygame

class Fruit:
    def __init__(self, image, x, y, speed, size, points, half1, half2, scale):
        self.image = pygame.transform.scale(image, scale)
        half_width = scale[0] // 2
        self.half1_image = pygame.transform.scale(half1, (half_width, scale[1]))
        self.half2_image = pygame.transform.scale(half2, (half_width, scale[1]))
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.points = points
        self.sliced = False
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        self.y -= self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        if self.sliced:
            surface.blit(self.half1_image, (self.x - self.half1_image.get_width(), self.y))
            surface.blit(self.half2_image, (self.x, self.y))
        else:
            surface.blit(self.image, (self.x, self.y))

    def slice(self):
        self.sliced = True

def load_fruit_images():
    def load(name): return pygame.image.load(f"assets/{name}.png").convert_alpha()
    return [
        {
            'whole': load("apple"),
            'half1': load("apple_half1"),
            'half2': load("apple_half2"),
            'scale': (50, 50)
        },
        {
            'whole': load("banana"),
            'half1': load("banana_half1"),
            'half2': load("banana_half2"),
            'scale': (70, 40)
        },
        {
            'whole': load("watermelon"),
            'half1': load("watermelon_half1"),
            'half2': load("watermelon_half2"),
            'scale': (120, 80)
        },
        {
            'whole': load("pineapple"),
            'half1': load("pineapple_half1"),
            'half2': load("pineapple_half2"),
            'scale': (60, 80)
        }
    ]
