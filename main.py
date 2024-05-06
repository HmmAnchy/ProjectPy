import pygame

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png').convert_alpha() # фото иконки
pygame.display.set_icon(icon) # иконка
bg = pygame.image.load('images/background.jpg').convert()
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
attack = pygame.image.load('images/player/attack/1.png')
attack_list = []
attack_speed = 12
player_x = 200
player_y = 450
player_speed = 15
player_anim_count = 0
is_jump = False
jump_count = 10
player_main = pygame.image.load('images/player/main/main_1.png').convert_alpha()
ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)

running = True
while running:
	screen.blit(bg, (bg_x,0))
	screen.blit(bg, (bg_x + 800,0))
	screen.blit(bg, (bg_x - 800,0))

	player_rect = player_main.get_rect(topleft=(player_x, player_y))
	
	if ghost_list_in_game:
		for el in ghost_list_in_game:
			screen.blit(ghost, el)
			el.x -= 10

		if player_rect.colliderect(el):
			print("You lose")

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

			if ghost_list_in_game:
				for (i2, ghost_idx) in enumerate(ghost_list_in_game):
					if attack_idx.colliderect(ghost_idx):
						attack_list.pop(i)
						ghost_list_in_game.pop(i2)

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
		if event.type == ghost_timer:
			ghost_list_in_game.append(ghost.get_rect(topleft=(820, 450)))

	time.tick(15)