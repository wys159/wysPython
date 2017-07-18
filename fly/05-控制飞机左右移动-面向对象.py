# _*_ coding:utf-8 _*_
import pygame
import time
from pygame.locals import *

class HeroPlane():
	def __init__(self,screen_temp):
		self.x=180
		self.y=600
		self.screen=screen_temp
		self.image=pygame.image.load("./feiji/hero1.png")
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		
	def move_left(self):
		self.x-=10
		
	def move_right(self):
		self.x+=10
		
def Key_control(hero_temp):
   #判断是否是点击了退出按
	for event in pygame.event.get():
	# print(event.type) 
		if event.type == QUIT:
			print("exit")
			exit()
			#判断就否按了键
		elif event.type == KEYDOWN:
			if event.key == K_a or event.key == K_LEFT:
				print('left')
				#控制飞机让其向左移
				hero_temp.move_left()
			elif event.key == K_d or event.key == K_RIGHT:
				print('right')
				#控制飞机让其向右移动
				hero_temp.move_right()
			elif event.key == K_SPACE:
				print('space')


def main():
	
	#1.创建窗口
	screen=pygame.display.set_mode((480,852),0,32)
	
	#2.创建一个背景图片
	background=pygame.image.load("./feiji/background.png")
	#3.创建一个飞机对象

	hero=HeroPlane(screen)
	while True:
		screen.blit(background,(0,0))
		#调用飞机显示方法
		hero.display()
		pygame.display.update()
		Key_control(hero)
		time.sleep(0.01)








if __name__=="__main__":
	main()
