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
	# 初始化一个游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
	ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	# 创建按钮
	play_button = Button(ai_settings,screen,'Play')
	# 设置背景色
	''' bg_color = (230,230,230)'''
	# 创建一艘飞船，一个子弹编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings,screen,aliens,ship) 
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	
	# 开始游戏的主循环
	while True:
		 # 监视键盘和鼠标事件
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
		
		# 删除已消失的子弹
		   #for bullet in bullets.copy():
			#if bullet.rect.bottom <= 0:
				#bullets.remove(bullet)
		
		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,
		play_button)
				 
		 #每次循环时都重绘屏幕
		''' screen.fill(ai_settings.bg_color)
			ship.blitme()
		'''
		 #让最近绘制的屏幕可见
		''' pygame.display.flip()'''
run_game()

