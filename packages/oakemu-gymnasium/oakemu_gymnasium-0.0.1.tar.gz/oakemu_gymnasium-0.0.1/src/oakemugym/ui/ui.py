import pygame
from oakemu.machines.zxspectrum import Keys


class Events:
    def __init__(self, quit: bool, keys: Keys):  # noqa
        self.quit = quit
        self.keys = keys


def process_events() -> Events:
    quit = any(event.type == pygame.QUIT for event in pygame.event.get())
    keys = _get_keys_pressed()
    return Events(quit, keys)


def _get_keys_pressed() -> Keys:
    keys = Keys.NONE

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        keys |= Keys.A
    if pressed[pygame.K_b]:
        keys |= Keys.B
    if pressed[pygame.K_c]:
        keys |= Keys.C
    if pressed[pygame.K_d]:
        keys |= Keys.D
    if pressed[pygame.K_e]:
        keys |= Keys.E
    if pressed[pygame.K_f]:
        keys |= Keys.F
    if pressed[pygame.K_g]:
        keys |= Keys.G
    if pressed[pygame.K_h]:
        keys |= Keys.H
    if pressed[pygame.K_i]:
        keys |= Keys.I
    if pressed[pygame.K_j]:
        keys |= Keys.J
    if pressed[pygame.K_k]:
        keys |= Keys.K
    if pressed[pygame.K_l]:
        keys |= Keys.L
    if pressed[pygame.K_m]:
        keys |= Keys.M
    if pressed[pygame.K_n]:
        keys |= Keys.N
    if pressed[pygame.K_o]:
        keys |= Keys.O
    if pressed[pygame.K_p]:
        keys |= Keys.P
    if pressed[pygame.K_q]:
        keys |= Keys.Q
    if pressed[pygame.K_r]:
        keys |= Keys.R
    if pressed[pygame.K_s]:
        keys |= Keys.S
    if pressed[pygame.K_t]:
        keys |= Keys.T
    if pressed[pygame.K_u]:
        keys |= Keys.U
    if pressed[pygame.K_v]:
        keys |= Keys.V
    if pressed[pygame.K_w]:
        keys |= Keys.W
    if pressed[pygame.K_x]:
        keys |= Keys.X
    if pressed[pygame.K_y]:
        keys |= Keys.Y
    if pressed[pygame.K_z]:
        keys |= Keys.Z
    if pressed[pygame.K_0] or pressed[pygame.K_KP0]:
        keys |= Keys.D0
    if pressed[pygame.K_1] or pressed[pygame.K_KP1]:
        keys |= Keys.D1
    if pressed[pygame.K_2] or pressed[pygame.K_KP2]:
        keys |= Keys.D2
    if pressed[pygame.K_3] or pressed[pygame.K_KP3]:
        keys |= Keys.D3
    if pressed[pygame.K_4] or pressed[pygame.K_KP4]:
        keys |= Keys.D4
    if pressed[pygame.K_5] or pressed[pygame.K_KP5]:
        keys |= Keys.D5
    if pressed[pygame.K_6] or pressed[pygame.K_KP6]:
        keys |= Keys.D6
    if pressed[pygame.K_7] or pressed[pygame.K_KP7]:
        keys |= Keys.D7
    if pressed[pygame.K_8] or pressed[pygame.K_KP8]:
        keys |= Keys.D8
    if pressed[pygame.K_9] or pressed[pygame.K_KP9]:
        keys |= Keys.D9
    if pressed[pygame.K_RETURN]:
        keys |= Keys.ENTER
    if pressed[pygame.K_SPACE]:
        keys |= Keys.SPACE
    if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
        keys |= Keys.SHIFT
    if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]:
        keys |= Keys.SYMBOL_SHIFT

    return keys
