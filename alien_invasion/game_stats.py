# coding=gbk

class GameStats():
	def __init__(self,ai_settings):
		'''������Ϸ��ͳ����Ϣ'''
		self.ai_settings = ai_settings
		self.reset_stats()
		# ��Ϸ������ʱ���ڷǻ״̬
		self.game_active = False
	def reset_stats(self):
		'''��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ'''
		self.ships_left = self.ai_settings.ship_limit
