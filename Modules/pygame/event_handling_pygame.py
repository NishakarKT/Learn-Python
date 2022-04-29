import pygame

game_window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("Event Handling")

exit_game = False

while not exit_game:
    for event in pygame.event.get(): # gets me all the events form mouse and keyboard performed by the user.
        print(event) # prints all the ongoing events