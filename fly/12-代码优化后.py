#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pygame
import time
from pygame.locals import *
import random


class Base(object):
    """子弹飞机基类"""

    def __init__(self, screen_temp, x, y, image_name):

        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)


class BasePlane(Base):
    """飞机基类"""

    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []  # 存储发射的子弹引用

# 显示飞机
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 调用子弹并显示
        for bullet in self.bullet_list:
            bullet.display()
            # 子弹自己移动
            bullet.move()
            if bullet.judge():  # 判断子弹越界并删除
                self.bullet_list.remove(bullet)


class HeroPlane(BasePlane):
    """飞机类"""

    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 180, 600, "./feiji/hero1.png")

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
# 显示敌机类


class EnemyPlane(BasePlane):
    """敌机类"""

    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direnction = "right"  # 用来存储飞机默认的显示方向

    def move(self):
        if self.direnction == "right":
            self.x += 5
        elif self.direnction == "left":
            self.x -= 5

        if self.x > 430:
            self.direnction = "left"
        elif self.x < 0:
            self.direnction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 20 or random_num == 60:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(Base):
    """子弹基类"""
    # 显示子弹

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):

    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40,
                            y - 20, "./feiji/bullet.png")

    # 子弹自己动
    def move(self):
        self.y -= 5

     # 判断子弹越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):

    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 25,
                            y + 40, "./feiji/bullet1.png")

    # 子弹自己动
    def move(self):
        self.y += 10
    # 判断子弹越界

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


def Key_control(hero_temp):
            # 判断是否是点击了退出按
    for event in pygame.event.get():
        # print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
            # 判断就否按了键
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # 控制飞机让其向左移
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # 控制飞机让其向右移动
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():

    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    # 3.创建一个飞机对象

    hero = HeroPlane(screen)
    # 4.创建一个敌机
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        # 调用飞机显示方法
        hero.display()
        # 显示敌机方法
        enemy.display()
        # 调用敌机移动
        enemy.move()
        # 敌机发射子弹
        enemy.fire()
        pygame.display.update()
        Key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
