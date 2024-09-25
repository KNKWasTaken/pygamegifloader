import os
import pygame
from PIL import Image

pygame.init()

size = (800,600)

class GIFClass(pygame.sprite.Sprite):
    def __init__(self, name, output):
        super().__init__()
        self.images = self.extractImages(name, action, output)
        self.currentImage = 0
        self.image = self.images[self.currentImage]
        self.rect = self.image.get_rect()
        self.rect.center = (size[0]//2, size[1]//2)
        self.speed = 5
        self.animationSpeed = 0.2

    def update(self, dt):
        self.currentImage += self.animationSpeed
        if self.currentImage >= len(self.images):
            self.currentImage = 0
        self.image = self.images[int(self.currentImage)]

    def extractImages(self, name, output):
        frameList = []
        with Image.open(f'{name}.gif') as img:
            for frame in range(img.n_frames):
                img.seek(frame)
                frameImage = img.convert('RGBA')
                framePath = os.path.join(output, f'{name}{frame}.png')
                frameImage.save(framePath)
                frameList.append(pygame.image.load(framePath).convert_alpha())
            
        return frameList
    
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

gif = GIFClass('Your File', 'Your Output')
#Replace it with your file and output folder
allGIF = pygame.sprite.Group(gif)

run = True
while run:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    allGIF.update(dt)

    display.fill((0, 0, 0))
    allGIF.draw(display)
    pygame.display.flip()

pygame.quit()
