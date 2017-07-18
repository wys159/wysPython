# _*_ coding:utf-8 _*_
import pygame
import time
from pygame.locals import *
def main():
	
	#1.创建窗口
	screen=pygame.display.set_mode((480,852),0,32)

	#2.创建一个背景图片
	background=pygame.image.load("./feiji/background.png")
	#3.创建一个飞机

	hero=pygame.image.load("./feiji/hero1.png")
	x=180
	y=600

	while True:
		screen.blit(background,(0,0))
		screen.blit(hero,(x,y))
		#判断是否是点击了退出按钮
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
					x-=10
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')
					#控制飞机让其向右移动
					x+=10
				elif event.key == K_SPACE:
					print('space')
		pygame.display.update()

		time.sleep(0.01)








if __name__=="__main__":
	main()
