import sys
from cx_Freeze import setup, Executable  


setup(
    name='2048Game',
    version='0.1',
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["2048alpha.png","2048.png","2048Image.png","Menu2048.png","Volume.png","VolumeOff.png","SFX.mp3","NoSFX.mp3","Music.mp3"],
                          "excludes": ["OpenGL.GL", "Numeric", "copyreg", "itertools.imap", "numpy", "pkg_resources", "queue", "winreg", "pygame.SRCALPHA", "pygame.sdlmain_osx"]}},
    executables=[Executable("2048Gameplay.py")]
     )
    
