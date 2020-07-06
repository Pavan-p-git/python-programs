from pygame import mixer
file='G:\english music\careless whisper.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
