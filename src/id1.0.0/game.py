import pygame
from player import Player

class Game:
	def __init__(self):
		pygame.init()
		#Initialisation de la fenêtre
		self.screen_size = (1500,1000)
		self.screen = pygame.display.set_mode(self.screen_size)
		pygame.display.set_caption("Jeu de test")

		self.is_running = True

		self.background_color = pygame.Color("white")
		self.player = Player()

	def Start(self):
		while self.is_running:
			self.screen.fill(self.background_color)
			self.screen.blit(self.player.GetImage(), self.player.GetRect())
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.Stop()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.player.Move(Player.DIR_EAST)
					elif event.key == pygame.K_LEFT:
						self.player.Move(Player.DIR_WEST)
					elif event.key == pygame.K_UP:
						self.player.Move(Player.DIR_NORTH)
					elif event.key == pygame.K_DOWN:
						self.player.Move(Player.DIR_SOUTH)

		pygame.quit()

	def Stop(self):
		self.is_running = False
