from GPIOArm import Arm
import pygame
arm = Arm()
pygame.init()
pygame.display.set_mode()

def ArmControl(key, part, state):
        if event.key == getattr(pygame,"K_"+key):
                getattr(getattr(arm, part), state)()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			ArmControl("a", "base", "counter")
			ArmControl("d", "base", "clock")
			ArmControl("w", "shoulder", "up")
			ArmControl("s", "shoulder", "down")
			ArmControl("r", "elbow", "up")
			ArmControl("f", "elbow", "down")
			ArmControl("t", "wrist", "up")
			ArmControl("g", "wrist", "down")
			ArmControl("y", "grip", "close")
			ArmControl("h", "grip", "open")
			ArmControl("u", "light", "on")
			ArmControl("j", "light", "off")
		elif event.type == pygame.KEYUP:
			
