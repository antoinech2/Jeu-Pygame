import pygame

class Player(pygame.sprite.Sprite):

	DIR_NORTH = 0
	DIR_NORTH_EAST = 1
	DIR_EAST = 2
	DIR_SOUTH_EAST = 3
	DIR_SOUTH = 4
	DIR_SOUTH_WEST = 5
	DIR_WEST = 6
	DIR_NORTH_WEST = 7

	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("../../res/textures/player/player.png"), (50, 50))
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 100
		self.vitesse = 10

	def Move(self, direction):
		if direction == Player.DIR_EAST:
			self.rect.x += self.vitesse
		elif direction == Player.DIR_WEST:
			self.rect.x -= self.vitesse
		elif direction == Player.DIR_NORTH:
			self.rect.y -= self.vitesse
		elif direction == Player.DIR_SOUTH:
			self.rect.y += self.vitesse

	def GetImage(self):
		return self.image
	def GetRect(self):
		return self.rect
