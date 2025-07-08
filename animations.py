import pygame
import os

GIRL_FRAME_WIDTH = 60
GIRL_FRAME_HEIGHT = 120
FPS = 60

class Animation:
    def __init__(self,name,n):
        self.frame_name = name
        self.no_of_frames = n
        self.frame_index = 0

    def animate(self,timer):
        if(timer%(FPS/self.no_of_frames)==0):
            self.frame_index = (self.frame_index+1)%self.no_of_frames
        return self.frame_name[self.frame_index]

def load_frames(sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

#Idle frames creation
IDLE_FRAMES_N = 2

LILY_IDLE_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Idle.png')
)

LILY_IDLEF_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Idlef.png')
)

LILY_IDLEB_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Idleb.png')
)

idle_frames = [load_frames(LILY_IDLE_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,IDLE_FRAMES_N),
               [1,2],
               load_frames(LILY_IDLEF_IMAGE,GIRL_FRAME_WIDTH,GIRL_FRAME_HEIGHT,IDLE_FRAMES_N),
               load_frames(LILY_IDLEB_IMAGE,GIRL_FRAME_WIDTH,GIRL_FRAME_HEIGHT,IDLE_FRAMES_N)
               ]

for i in range(IDLE_FRAMES_N):
    idle_frames[1][i] = pygame.transform.flip(idle_frames[0][i], True, False) 
    
idle = [Animation(idle_frames[0],IDLE_FRAMES_N),
        Animation(idle_frames[1],IDLE_FRAMES_N),
        Animation(idle_frames[2],IDLE_FRAMES_N),
        Animation(idle_frames[3],IDLE_FRAMES_N)
        ]

#Walk frames creation
WALK_FRAMES_N = 6

LILY_WALK_RIGHT_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Walk.png')
)

LILY_WALK_FRONT_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Walkf.png')
)

LILY_WALK_BACK_IMAGE = pygame.image.load(
    os.path.join('img','Girl','Walkb.png')
)

walk_frames = [load_frames(LILY_WALK_RIGHT_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,WALK_FRAMES_N),
               [1,2,3,4,5,6],
               load_frames(LILY_WALK_FRONT_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,WALK_FRAMES_N),
               load_frames(LILY_WALK_BACK_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT, WALK_FRAMES_N)
               ]

for i in range(WALK_FRAMES_N):
    walk_frames[1][i] = pygame.transform.flip(walk_frames[0][i], True, False) 

walk = [Animation(walk_frames[0],WALK_FRAMES_N),                #walk directions 0 = right, 1 = left, 2 = up, 3 = down
        Animation(walk_frames[1],WALK_FRAMES_N),
        Animation(walk_frames[2],WALK_FRAMES_N),
        Animation(walk_frames[3],WALK_FRAMES_N)
        ]