import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600)) # размер окна 
pygame.display.set_caption("Название игры") # Название программы
icon = pygame.image.load('images/icon.png').convert_alpha() # фото иконки
pygame.display.set_icon(icon) # иконка

background = pygame.image.load('images/background.jpg').convert()
cat_right = [
	pygame.image.load('images/player/right/player_1.png').convert_alpha(),
	pygame.image.load('images/player/right/player_2.png').convert_alpha(),
	pygame.image.load('images/player/right/player_3.png').convert_alpha(),
	pygame.image.load('images/player/right/player_4.png').convert_alpha(),
	pygame.image.load('images/player/right/player_5.png').convert_alpha(),
	pygame.image.load('images/player/right/player_6.png').convert_alpha(),]
cat_left = [
	pygame.image.load('images/player/left/player_1.png').convert_alpha(),
	pygame.image.load('images/player/left/player_2.png').convert_alpha(),
	pygame.image.load('images/player/left/player_3.png').convert_alpha(),
	pygame.image.load('images/player/left/player_4.png').convert_alpha(),
	pygame.image.load('images/player/left/player_5.png').convert_alpha(),
	pygame.image.load('images/player/left/player_6.png').convert_alpha(),]

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []
player_anim_count = 0
bg_count = 0

player_y = 400

is_jump = False
jump_count = 12

player_speed = 30
player_speed_count = 0
#sound = pygame.mixer.Sound('')     ---------- Звук
#sound.play()                    ------------ При запуске программы проигрывается звук

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1000)

running = True
while running:

	screen.blit(background, (bg_count, 0))
	screen.blit(background, (bg_count + 800, 0))

	player_rect = cat_left[0].get_rect(topleft=(player_speed_count, player_y))
	
	if ghost_list_in_game:
		for el in ghost_list_in_game:
			screen.blit(ghost, el)
			el.x -= 10

		if player_rect.colliderect(el):
			print("You lose")

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		screen.blit(cat_left[player_anim_count], (player_speed_count, player_y))
	else:
		screen.blit(cat_right[player_anim_count], (player_speed_count, player_y))

	if keys[pygame.K_LEFT] and player_speed_count > 10:
		player_speed_count -= player_speed
	elif keys[pygame.K_RIGHT] and player_speed_count < 500:
		player_speed_count += player_speed

	if not is_jump:
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

	bg_count -= 4
	if bg_count == -800:
		bg_count = 0


	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		if event.type == ghost_timer:
			ghost_list_in_game.append(ghost.get_rect(topleft=(820, 350)))

	clock.tick(12)