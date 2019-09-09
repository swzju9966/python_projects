# coding=gbk
class Settings():
	'''存储游戏所有设置的类'''
	
	def __init__(self):
		'''初始化游戏的设置'''
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)
		# 飞船的设置
		self.ship_speed_factor = 3
		self.ship_limit = 3
		
		# 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 60
		self.bullet_height = 60
		self.bullet_color = (250,0,0)	
		self.bullets_allowed = 3	
		
		# 外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction 为1表示向右移,-1向左移
		self.fleet_direction = 1
		
