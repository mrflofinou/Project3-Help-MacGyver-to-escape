"""File for the install of macgyver.py"""

from cx_Freeze import setup, Executable

# We call the setup function
setup(
    name = "MacGyver - The game",
    version = "0.1",
    description = "Help MacGyver to escape from labyrinth",
    executables = [Executable("macgyver.py")],
)
