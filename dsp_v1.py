from io import BytesIO
import tempfile
import requests
import numpy as np
import scipy.signal as sg
import pydub
import matplotlib.pyplot as plt
from IPython.display import Audio, display

def speak(data):
	# We convert the mp3 bytes to wav.
	audio = pydub.AudioSegment.from_mp3((data))
	with tempfile.TemporaryFile() as fn:
		wavef = audio.export(fn, format='wav')
		wavef.seek(0)
		wave = wavef.read()
	# We get the raw data by removing the 24 first
	# bytes of the header.
	x = np.frombuffer(wave, np.int16)[24:]
	return x, audio.frame_rate

def play(x, fr, autoplay=False):
	display(Audio(x, rate=fr, autoplay=autoplay))	


url = ('https://github.com/ipython-books/cookbook-2nd-data/blob/master/voice.mp3?raw=true')
# voice = requests.get(url).content
voice = "music.mp3"

x, fr = speak(voice)

ten_seconds = 10 * 1000 
first_10_seconds = voice[:ten_seconds]

beginning = first_10_seconds + 6

beginning.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})


fig, ax = plt.subplots(1, 1, figsize=(8, 4))
t = np.linspace(0., len(x) / fr, len(x))
print(len(t))
ax.plot(t, x, lw=1)
plt.show()

