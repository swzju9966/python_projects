# coding=gbk
'''import sys'''

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from pygame.sprite import Group

import pygame
import game_functions as gf

def run_game():
	# ��ʼ��һ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
	ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	# ������ť
	play_button = Button(ai_settings,screen,'Play')
	# ���ñ���ɫ
	''' bg_color = (230,230,230)'''
	# ����һ�ҷɴ���һ���ӵ������һ�������˱���
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	# ����������Ⱥ
	gf.create_fleet(ai_settings,screen,aliens,ship) 
	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	stats = GameStats(ai_settings)

	
	# ��ʼ��Ϸ����ѭ��
	while True:
		 # ���Ӽ��̺�����¼�
		#for event in pygame.event.get():
			 #if event.type == pygame.QUIT:
				 #sys.exit()
		
		gf.check_events(ai_settings,screen,ship,bullets,stats,
			play_button,aliens)
		
		if stats.game_active:
			
			ship.update()
			gf.update_bullets(aliens,bullets,ai_settings,screen,ship)
			gf.update_aliens(ai_settings,aliens,ship,bullets,stats,screen)
			'''bullets.update()'''
		
		# ɾ������ʧ���ӵ�
		   #for bullet in bullets.copy():
			#if bullet.rect.bottom <= 0:
				#bullets.remove(bullet)
		
		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,
		play_button)
				 
		 #ÿ��ѭ��ʱ���ػ���Ļ
		''' screen.fill(ai_settings.bg_color)
			ship.blitme()
		'''
		 #��������Ƶ���Ļ�ɼ�
		''' pygame.display.flip()'''
run_game()

