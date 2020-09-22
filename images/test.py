import pygame
pygame.init()

def test():
    a = input("shuru:")
    while True:
        eventList = pygame.event.get()
        if len(eventList) > 0:
            print(eventList)

test()