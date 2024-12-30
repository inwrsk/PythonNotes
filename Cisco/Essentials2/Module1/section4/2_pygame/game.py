import pygame

run = True# the program will run as long as the run variable is True


pygame.init()#initialize environment
width = 400
height = 100
screen = pygame.display.set_mode((width, height))
#window sizes

font = pygame.font.SysFont(None, 48)

text = font.render("Welcome to pygame", True, (255, 255, 255))

screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
#insert the text into the (currently invisible) screen buffer

pygame.display.flip()#flip the screen buffers to make the text visible;

while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False

