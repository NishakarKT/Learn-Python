import pygame

game_window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("Key press handling")

exit_game = False
game_over  = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        # keys handling
        if event.type == pygame.KEYDOWN: # when keys are "Presseed"
            if(event.key == pygame.K_RIGHT):
                print("You have pressed the right arrow key ...")

        if event.type == pygame.KEYUP:
            pass
