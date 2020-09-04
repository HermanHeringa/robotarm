from roboarm import Arm
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
		if event.type == pygame.KEYDOWN:
			ArmControl("a", "base", "rotate_counter")
			ArmControl("d", "base", "rotate_clock")
			ArmControl("w", "shoulder", "up")
			ArmControl("s", "shoulder", "down")
			ArmControl("r", "elbow", "up")
			ArmControl("f", "elbow", "down")
			ArmControl("t", "wrist", "up")
			ArmControl("g", "wrist", "down")
			ArmControl("y", "grips", "close")
			ArmControl("h", "grips", "open")
			ArmControl("u", "led", "on")
			ArmControl("j", "led", "off")
#arm.base.rotate_clock(1)
#arm.shoulder.up(1)
#arm.elbow.down(1)
#arm.wrist.up(1)
#arm.grips.close(1)
#arm.led.on(2)
