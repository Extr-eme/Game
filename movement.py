import pygame
from animations import idle, walk  # Ensure these are valid lists of animation frames

class Character_state(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        self.frame_type = idle[direction]

        # Use image and rect for sprite compatibility
        self.image = self.frame_type.animate(0)  # Assume frame_type has .animate(timer)

        # Offset the rect's center downward to appear in front of grass tiles
        offset_y = 20  # Adjust this value if needed
        self.rect = self.image.get_rect(center=(x, y + offset_y))

        self.speed = 5

    def character_movement(self, keys):
        dx = dy = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction = 0
            self.frame_type = walk[self.direction]
            dx = self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction = 1
            self.frame_type = walk[self.direction]
            dx = -self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction = 2
            self.frame_type = walk[self.direction]
            dy = self.speed
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction = 3
            self.frame_type = walk[self.direction]
            dy = -self.speed
        else:
            self.frame_type = idle[self.direction]

        # Update position
        self.rect.x += dx
        self.rect.y += dy

    def update(self, frame_timer):
        # Update current frame from animation
        self.image = self.frame_type.animate(frame_timer)
