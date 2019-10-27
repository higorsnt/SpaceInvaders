import sys
from cx_Freeze import setup, Executable
import pygame


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("spaceinvaders.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame", "math", "random", "os"],
        include_files = ["images/back.png", "images/boss1.png", "images/boss3.png",
        "images/explosion.png", "images/heart.png", "images/invader0.png", "images/invader1.png",
        "images/logo.png", "images/ship.png", "sounds/invaderkilled.wav", "sounds/menu.wav",
        "sounds/shipexplosion.wav", "sounds/shoot.wav", "fonts/space_invaders.ttf"],
        excludes = []
)




setup(
    name = "SpaceInvaders",
    version = "1.0",
    description = "Jogo simulando o Space Invaders",
    options = dict(build_exe = buildOptions),
    executables = executables
)