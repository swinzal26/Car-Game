import pygame
from pygame.locals import *
import random

size = width, height = (500, 620)
road_width = int(width/1.2)
roadmark_width = int(width/60)

right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

speed = 2

pygame.init()
running = True

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Car Game")

screen.fill((87, 163, 207))

pygame.display.update()

car = pygame.image.load("car.png")

car_mov = car.get_rect()
car_mov.center = right_lane, height*0.8

car2 = pygame.image.load("otherCar.png")
car2_mov = car2.get_rect()
car2_mov.center = left_lane, height*0.2

counter = 0

while running:
    counter += 1
    
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    car2_mov[1] += speed
    if car2_mov[1] > height:

        if random.randint(0,1) == 0:
            car2_mov.center = right_lane, -200
        else:
            car2_mov.center = left_lane, -200

    if car_mov[0] == car2_mov[0] and car2_mov[1] > car_mov[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:

            running = False
        if event.type == KEYDOWN:

            if event.key in [K_a, K_LEFT]:
                car_mov = car_mov.move([-int(road_width/2), 0])

            if event.key in [K_d, K_RIGHT]:
                car_mov = car_mov.move([int(road_width/2), 0])

    pygame.draw.rect(
        screen,
        (83, 87, 89),
        (width/2-road_width/2, 0, road_width, height))

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_width/2, 0, roadmark_width, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height))

    screen.blit(car, car_mov)
    screen.blit(car2, car2_mov)

    pygame.display.update()

pygame.quit()