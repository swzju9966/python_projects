# coding=gbk
class Settings():
	'''�洢��Ϸ�������õ���'''
	
	def __init__(self):
		'''��ʼ����Ϸ������'''
		# ��Ļ����
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)
		# �ɴ�������
		self.ship_speed_factor = 3
		self.ship_limit = 3
		
		# �ӵ�����
		self.bullet_speed_factor = 3
		self.bullet_width = 60
		self.bullet_height = 60
		self.bullet_color = (250,0,0)	
		self.bullets_allowed = 3	
		
		# ����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction Ϊ1��ʾ������,-1������
		self.fleet_direction = 1
		
