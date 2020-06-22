# import packagws
import pygame
from pygame.locals import * #consants from Pygame


# initialize pygame
pygame.init()

# setting up screen
screen_info = pygame.display.Info()
size = (width,height) = (screen_info.current_w,screen_info.current_h)
screen = pygame.display.set_mode(size)
color = (50, 104, 168) # background color


# set up the clock
clock = pygame.time.Clock()


# set up the sprite
spriteImage = pygame.image.load("FISH sprite.png")
spriteImage = pygame.transform.scale(spriteImage, (int(spriteImage.get_rect().width * 0.3), int(spriteImage.get_rect().height * 0.3)))
spriteRect = spriteImage.get_rect()
# center sprite
spriteRect.center = (width // 2, height // 2)



def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(spriteImage,spriteRect)
    pygame.display.flip()

if __name__ == "__main__":
  main()