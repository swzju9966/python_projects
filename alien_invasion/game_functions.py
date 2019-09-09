# coding=gbk
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

'''def check_events(ship):
	''''''��Ӧ����������¼�''''''
	for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 sys.exit()
			 elif event.type ==pygame.KEYDOWN:
				 if event.key == pygame.K_RIGHT:
					# �����ƶ��ɴ�
					 ''''''ship.rect.centerx += 1''''''
					 ship.moving_right = True
				 elif event.key == pygame.K_LEFT:
					 ship.moving_left = True
			 elif event.type ==pygame.KEYUP:
				 if event.key == pygame.K_RIGHT:
					 ship.moving_right = False
				 elif event.key == pygame.K_LEFT:
					 ship.moving_left = False
'''
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''��Ӧ����'''	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# �������ӵ���������������
		fire_bullet(ai_settings,screen,ship,bullets)
		    #if len(bullets) < ai_settings.bullets_allowed:
				#new_bullet = Bullet(ai_settings,screen,ship)
				#bullets.add(new_bullet) 
	# ������Ϸ�Ŀ�ݼ�
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event,ship):
	'''��Ӧ�ſ�'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets,stats,play_button,
	aliens):
	'''��Ӧ����������¼�'''
	for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 sys.exit()
			 elif event.type == pygame.KEYDOWN:
				 check_keydown_events(event,ai_settings,screen,ship,bullets)
			 elif event.type == pygame.KEYUP:
				 check_keyup_events(event,ship)
			 elif event.type == pygame.MOUSEBUTTONDOWN:
				 mouse_x,mouse_y = pygame.mouse.get_pos()
				 check_play_button(ai_settings,screen,stats,play_button,
				 ship,aliens,bullets,mouse_x,mouse_y)
				 
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,
	bullets,mouse_x,mouse_y):
	'''����ҵ���play��ťʱ��ʼ��Ϸ'''
	if play_button.rect.collidepoint(mouse_x,mouse_y):
		# ������Ϸ��Ϣ
		stats.reset_stats()
		stats.game_active = True 
		
		# ����������б���ӵ��б�
		aliens.empty()
		bullets.empty()
		
		# ����һȺ�µ������ˣ����÷ɴ�����
		create_fleet(ai_settings,screen,aliens,ship)
		ship.center_ship()
		
				 
				
def update_screen(ai_settings,screen,ship,bullets,aliens,stats,
	play_button):
	'''������Ļ�ϵ�ͼ�񣬲��л�������Ļ'''
	# ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_settings.bg_color)
	# �ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		play_button.draw_button()
	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
	
def update_bullets(aliens,bullets,ai_settings,screen,ship):
	'''�����ӵ���λ�ã���ɾ���Ѿ���ʧ���ӵ�'''
	# �����ӵ���λ��
	bullets.update()
	# ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(aliens,bullets,ai_settings,screen,ship)

def check_bullet_alien_collisions(aliens,bullets,ai_settings,screen,ship):
	'''��Ӧ�ӵ��������˵���ײ'''
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	# ����Ƿ����ӵ�������������
	# �������������ɾ����Ӧ���ӵ��������ˣ�����һ���ֵ�
	#collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if len(aliens) == 0:
		# ɾ�����е��ӵ����½�һȺ������
		bullets.empty()
		create_fleet(ai_settings,screen,aliens,ship)
		
	
			
	
			
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
			
def get_number_aliens_x(ai_settings,alien_width):
	'''����һ�п������ɶ��ٸ�������'''
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	'''������Ļ�����ɶ�����������'''
	available_space_y = (ai_settings.screen_height - ship_height-
	(3 * alien_height))
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	'''����һ�������˲�������뵱ǰ��'''
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,aliens,ship):
	'''����������Ⱥ'''
	# ����һ�������ˣ�������һ�п������ɶ��ٸ�������
	# �����˼��Ϊ�����˿��
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,
	alien.rect.height)
	#alien_width = alien.rect.width
	#available_space_x = ai_settings.screen_width - 2 * alien_width
	#number_aliens_x = int(available_space_x / (2 * alien_width))
	
	# ����һ��������
	#'''for alien_number in range(number_aliens_x):'''
		 #����һ�������˲�������뵱ǰ��
		 #'''create_alien(ai_settings,screen,aliens,alien_number)'''
		#alien = Alien(ai_settings,screen)
		#alien.x = alien_width + 2 * alien_width * alien_number
		#alien.rect.x = alien.x
		#aliens.add(alien)
		
		
	# ����������Ⱥ
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,
			row_number)
			
def change_fleet_direction(ai_settings,aliens):
	'''����Ⱥ���������ƣ����ı����ǵķ���'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1	
	
def check_fleet_edges(ai_settings,aliens):
	'''�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
	
def ship_hit(ai_settings,aliens,ship,bullets,stats,screen):
	'''��Ӧ��������ײ���ķɴ�'''
	if stats.ships_left > 0:
		
	# �� ships_left��1
		stats.ships_left -= 1
	# ����������б���ӵ��б�
		aliens.empty()
		bullets.empty()
	# ����һȺ�µ�������
		create_fleet(ai_settings,screen,aliens,ship)
		ship.center_ship()
	# ��ͣ0.5s
		sleep(0.5)
	else:
		stats.game_active = False			
			
def check_aliens_bottom(ai_settings,aliens,ship,bullets,stats,screen):
	'''����Ƿ��������˵�����Ļ�Ͷ�'''
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# ��ɴ�һ��������
			ship_hit(ai_settings,aliens,ship,bullets,stats,screen)
			break
			
		
def update_aliens(ai_settings,aliens,ship,bullets,stats,screen):
	'''����Ƿ���������λ����Ļ��Ե������������Ⱥ�����������˵�λ��'''
	check_fleet_edges(ai_settings,aliens)
	aliens.update()	
	
	# ��������˺ͷɴ�֮�����ײ
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,aliens,ship,bullets,stats,screen)
	# ����Ƿ��������˵�����Ļ�Ͷ�
	check_aliens_bottom(ai_settings,aliens,ship,bullets,stats,screen)
	
		
		

		


	
		

		
	
		
