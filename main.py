import pygame

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png') # фото иконки
pygame.display.set_icon(icon) # иконка
bg = pygame.image.load('images/background.jpg')
bg_x = 0
player_left = [
	pygame.image.load('images/player/left/player_1.png').convert_alpha(),
	pygame.image.load('images/player/left/player_2.png').convert_alpha(),
	pygame.image.load('images/player/left/player_3.png').convert_alpha(),
	pygame.image.load('images/player/left/player_4.png').convert_alpha(),
	pygame.image.load('images/player/left/player_5.png').convert_alpha(),
	pygame.image.load('images/player/left/player_6.png').convert_alpha() ]
player_right = [
	pygame.image.load('images/player/right/player_1.png').convert_alpha(),
	pygame.image.load('images/player/right/player_2.png').convert_alpha(),
	pygame.image.load('images/player/right/player_3.png').convert_alpha(),
	pygame.image.load('images/player/right/player_4.png').convert_alpha(),
	pygame.image.load('images/player/right/player_5.png').convert_alpha(),
	pygame.image.load('images/player/right/player_6.png').convert_alpha() ]
player_x = 200
player_y = 450
player_speed = 10
player_anim_count = 0
is_jump = False
jump_count = 10
player_main = pygame.image.load('images/player/main/main_1.png').convert_alpha()
running = True
while running:
	screen.blit(bg, (bg_x,0))
	screen.blit(bg, (bg_x + 800,0))
	screen.blit(bg, (bg_x - 800,0))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a] and player_x > 20:
		screen.blit(player_left[player_anim_count], (player_x, player_y))
		player_x -= player_speed
		bg_x += player_speed - 2
		if bg_x == -800:
			bg_x = 0
	elif keys[pygame.K_d] and player_x < 700:
		screen.blit(player_right[player_anim_count], (player_x, player_y))
		player_x += player_speed
		bg_x -= player_speed - 2
		if bg_x == 800:
			bg_x = 0
	else:
		screen.blit(player_main, (player_x, player_y))

	if not  is_jump:
		if keys[pygame.K_SPACE]:
			is_jump = True
	else:
		if jump_count >= -10:
			if jump_count > 0:
				player_y -= (jump_count ** 2) / 2
			else:
				player_y += (jump_count ** 2) / 2
			jump_count -= 2
		else:
			is_jump = False
			jump_count = 10

	if player_anim_count == 5:
		player_anim_count = 0
	else:
		player_anim_count += 1

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	time.tick(15)