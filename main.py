import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600)) # размер окна 
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png') # фото иконки
pygame.display.set_icon(icon) # иконка

background = pygame.image.load('images/background.jpg')
cat = [
	pygame.image.load('images/player/player_1.png'),
	pygame.image.load('images/player/player_2.png'),
	pygame.image.load('images/player/player_3.png'),
	pygame.image.load('images/player/player_4.png'),
	pygame.image.load('images/player/player_5.png'),
	pygame.image.load('images/player/player_6.png'),
]

player_anim_count = 0
bg_count = 0

#sound = pygame.mixer.Sound('')     ---------- Звук
#sound.play()                    ------------ При запуске программы проигрывается звук
running = True
while running:

	screen.blit(background, (bg_count, 0))
	screen.blit(background, (bg_count + 800, 0))
	screen.blit(cat[player_anim_count], (300, 400))

	if player_anim_count == 5:
		player_anim_count = 0
	else:
		player_anim_count += 1

	bg_count -= 10
	if bg_count == -800:
		bg_count = 0

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	clock.tick(8)