import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600)) # размер окна 
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png') # фото иконки
pygame.display.set_icon(icon) # иконка



running = True
while running:

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()