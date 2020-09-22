import pygame
pygame.init()

pygame.display.set_mode(size=(300, 500))

    # for event in pygame.event.get():
key = pygame.key.get_pressed()
        # print(key)
if key[pygame.K_RIGHT]:
    print("向右……")
    print(key)
