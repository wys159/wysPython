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
		self.bullet_list=[]#存储发射的子弹引用
	#显示飞机
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		#调用子弹并显示
		for bullet in self.bullet_list:
			bullet.display()
			#子弹自己移动
			bullet.move()
			if bullet.judge():#判断子弹越界并删除
				self.bullet_list.remove(bullet)

	def move_left(self):
		self.x-=10
	def move_right(self):
		self.x+=10

	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))
#显示敌机类
class EnemyPlane():
	"""敌机类"""
	def __init__(self,screen_temp):
		self.x=0
		self.y=0
		self.screen=screen_temp
		self.image=pygame.image.load("./feiji/enemy0.png")
		#self.bullet_list=[]#存储发射的子弹引用
		self.direnction="right"#用来存储飞机默认的显示方向
	#显示飞机
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		#调用子弹并显示
		#for bullet in self.bullet_list:
		#	bullet.display()
		#	#子弹自己移动
		#	bullet.move()
		
	def move(self):
		if self.direnction=="right":
			self.x+=2
		elif self.direnction=="left":
			self.x-=2

		if self.x>430:
			self.direnction="left"
		elif self.x<0:
			self.direnction="right"
	

	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))
class Bullet():
	def __init__(self,screen_temp,x,y):

		self.x=x+40
		self.y=y-20
		self.screen=screen_temp#窗口对象的引用
		self.image=pygame.image.load("./feiji/bullet.png")
		#显示子弹
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	#子弹自己动
	def move(self):
		self.y-=5
	#判断子弹越界
	def judge(self):
		if self.y<0:
			return True
		else:
			return False

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
				hero_temp.fire()


def main():
	
	#1.创建窗口
	screen=pygame.display.set_mode((480,852),0,32)
	
	#2.创建一个背景图片
	background=pygame.image.load("./feiji/background.png")
	#3.创建一个飞机对象

	hero=HeroPlane(screen)
	#4.创建一个敌机
	enemy=EnemyPlane(screen)
	while True:
		screen.blit(background,(0,0))
		#调用飞机显示方法
		hero.display()
		#显示敌机方法
		enemy.display()
		#调用敌机移动
		enemy.move()
		pygame.display.update()
		Key_control(hero)
		time.sleep(0.01)








if __name__=="__main__":
	main()
