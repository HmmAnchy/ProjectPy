import pygame
from random import randint as ri

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png').convert_alpha() # фото иконки
pygame.display.set_icon(icon) # иконка
bg = pygame.image.load('images/bg.png').convert()
bg_x = 0
labal_font = pygame.font.Font('font/Roboto/Roboto-Black.ttf', 35)
heart = pygame.image.load('images/heart.png').convert_alpha()
labal_lose = labal_font.render('Вы проиграли!', False, (193, 196, 199))
bg_lose = pygame.image.load('images/bg_lose.png').convert()

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
attack = pygame.image.load('images/player/attack/1.png')
attack_list = []
attack_speed = 12
player_x = 100
player_y = 450
player_speed = 15
player_anim_count = 0
is_jump = False
jump_count = 12
player_life = 3
player_main = pygame.image.load('images/player/main/main_1.png').convert_alpha()
ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list = []
ghost_rect_x = 820
ghost_speed = 4

running = True
while running:
	labal_life = labal_font.render(str(player_life), False, (193, 196, 199))

	screen.blit(bg, (bg_x, 0))
	screen.blit(bg, (bg_x + 800, 0))
	screen.blit(bg, (bg_x - 800, 0))
	screen.blit(labal_life, (65, 7))
	screen.blit(heart, (10, 10))

	if player_life <= 0:
		screen.blit(bg_lose, (0, 0))
		screen.blit(labal_lose, (280, 250))

	player_rect = player_main.get_rect(topleft=(player_x, player_y))

	player_rect = player_main.get_rect(topleft=(player_x, player_y))

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

	if keys[pygame.K_e]:
		attack_list.append(attack.get_rect(topleft=(player_x + 30, player_y)))

	if attack:
		for(i,attack_idx) in enumerate(attack_list):
			screen.blit(attack, attack_idx)
			attack_idx.x += attack_speed

			if ghost_list:
				for (i2, ghost_idx) in enumerate(ghost_list):
					if attack_idx.colliderect(ghost_idx):
						attack_list.pop(i)
						ghost_list.pop(i2)

	if not  is_jump:
		if keys[pygame.K_SPACE]:
			is_jump = True
	else:
		if jump_count >= -12:
			if jump_count > 0:
				player_y -= (jump_count ** 2) / 2
			else:
				player_y += (jump_count ** 2) / 2
			jump_count -= 2
		else:
			is_jump = False
			jump_count = 12

	if player_anim_count == 5:
		player_anim_count = 0
	else:
		player_anim_count += 1

	check = ri(0, 40)
	if check == 2:
		ghost_list.append(ghost.get_rect(topleft=(ghost_rect_x, 450)))
		ghost_rect_x -= 4

	if ghost_list:
		for i in ghost_list:
			screen.blit(ghost, i)
			i.x -= ghost_speed
			if player_rect.colliderect(i):
				player_life -= 1
				player_x = 100
				ghost_list.pop(0)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	time.tick(15)
