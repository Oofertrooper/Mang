import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png"))),
]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x  # "Starting Position x"
        self.y = y  # "Starting Position y"
        self.tilt = 0  # "How much the image is tilted"
        self.tick_count = 0  # "Physics (if we fall down or move up)"
        self.vel = 0  # "is not moving, that's the reason for 0"
        self.height = self.y
        self.img_count = 0  # which image is shown - animation
        self.img = self.IMGS[0]  # reference to image 0

    def jump(self):  # jump of the bird
        self.vel = -10.5  # random number to be confirmed later, because trainer
        # told this works with other settings. 0,0 - a left top corner y up -, y down +, x left -, x right +)
        self.tick_count = 0  # keeping track where we last jumped, 0 is needed fot the next method to work
        self.height = self.y  # where we start, from which point bird starts to move

    def move(self):
        self.tick_count += 1  # tick happen frame go by, so we moved since the last jump

        d = self.vel * self.tick_count + 0.5 * (3) * (self.tick_count) ** 2
        # displacement, how many pixels we are moving up or down
        # time
        # we are moving tick_count to 0 after each jump,
        # additionally we set velocity to 10.5, and we update our y position
        if d >= 16:
            d = 16  # maxium movements

        if d < 0:
            d -= 2  # jump's size

        self.y = self.y + d

        if (
            d < 0 or self.y < self.height + 50
        ):  # to keep track from where w jump exactly and not to tilt too much
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if (
                self.tilt > -90
            ):  # Bird can go directly down, but not up let see above lines of code
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if (
            self.img_count < self.ANIMATION_TIME
        ):  # is the image count is less than 5 (animation time) then image 0
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            # is the image count is less than 10 (2x animation time) then image 1
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        # all this if and elif function is: in a nutshell an animation of the movement of the bird
        if self.tilt <= -80:
            self.img = self.IMGS[
                1
            ]  # when the bird is going down no movement of the wings
            self.img_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y).center)
        )
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def draw_window(win, bird):
    win.blit(BG_IMG, [0, 0])  # blit ~ draw
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(0, 0) # Default start coordinates of the bird.
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(win, bird)

    pygame.quit()
    quit()


main()