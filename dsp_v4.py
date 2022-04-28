import matplotlib.pyplot as plt
import numpy as np
import wave

# Read bass filter coefficient

bass_filter_co = np.empty((0))
lines = []

with open('65.fcf') as f:
    lines = f.readlines()

for line in lines:
    bass_filter_co = np.append(bass_filter_co, float(line))


# Read Voice filter coefficient

voice_filter_co = np.empty((0))
lines = []

with open('65_2000.fcf') as f:
    lines = f.readlines()

for line in lines:
    voice_filter_co = np.append(voice_filter_co, float(line))


# Read 300~1000Hz filter coefficient

bandpass_filter_co = np.empty((0))
lines = []

with open('2000_5000.fcf') as f:
    lines = f.readlines()

for line in lines:
    bandpass_filter_co = np.append(bandpass_filter_co, float(line))

# Read 1000~20000Hz filter coefficient

highpass_filter_co = np.empty((0))
lines = []

with open('5000.fcf') as f:
    lines = f.readlines()

for line in lines:
    highpass_filter_co = np.append(highpass_filter_co, float(line))

print('load OK')

file = 'bad_guy.wav'

wav_file = wave.open(file,'r')

#Extract Raw Audio from Wav File

signal = wav_file.readframes(-1)

if wav_file.getsampwidth() == 1:
    signal = np.array(np.frombuffer(signal, dtype='UInt8')-128, dtype='Int8')
elif wav_file.getsampwidth() == 2:
    signal = np.frombuffer(signal, dtype='Int16')
else:
    raise RuntimeError("Unsupported sample width")

# http://schlameel.com/2017/06/09/interleaving-and-de-interleaving-data-with-python/
deinterleaved = [signal[idx::wav_file.getnchannels()] for idx in range(wav_file.getnchannels())]

# deinterleaved [0] [1] denotes stereo
# deinterleaved[0] is left, deinterleaved[1] is right
# print(type(deinterleaved[0]))

#Get time from indices
fs = wav_file.getframerate()
Time = np.linspace(0, len(signal)/wav_file.getnchannels()/fs, num=len(signal)/wav_file.getnchannels())

# for test stereo
# fake = np.linspace(0, 0, num=len(signal)/wav_file.getnchannels())

# Plot
# plt.figure(1)
# plt.title('Signal Wave...')
# for channel in deinterleaved:
#     plt.plot(Time,channel)
# plt.show()

wav_file.close()


################ generate new file ##################

# gain of the EQ

gain1 = 0
gain2 = 1
gain3 = 0
gain4 = 0

# initialization
filter1_l = np.empty((0))
filter1_r = np.empty((0))
filter2_l = np.empty((0))
filter2_r = np.empty((0))
filter3_l = np.empty((0))
filter3_r = np.empty((0))
filter4_l = np.empty((0))
filter4_r = np.empty((0))
print('test')


############## filter 1 ##############
filter1_l = np.convolve(deinterleaved[0], bass_filter_co, mode='same')
filter1_r = np.convolve(deinterleaved[1], bass_filter_co, mode='same')

print('OK 1')

############## filter 2 ##############
filter2_l = np.convolve(deinterleaved[0], voice_filter_co, mode='same')
filter2_r = np.convolve(deinterleaved[1], voice_filter_co, mode='same')

print('OK 2')


############### filter 3 ##############
filter3_l = np.convolve(deinterleaved[0], bandpass_filter_co, mode='same')
filter3_r = np.convolve(deinterleaved[1], bandpass_filter_co, mode='same')

print('OK 3')


# # ############### filter 4 ##############
filter4_l = np.convolve(deinterleaved[0], highpass_filter_co, mode='same')
filter4_r = np.convolve(deinterleaved[1], highpass_filter_co, mode='same')

print('OK 4')



# plt.figure(2)
# plt.title('After filtering, remain 5000~20000 Hz')
# plt.plot(Time,filter4_l)
# plt.plot(Time,filter4_r)
# plt.show()

# Put the channels together with shape (2, 44100).

stereo_l = gain1*filter1_l+gain2*filter2_l+gain3*filter3_l+gain4*filter4_l
stereo_r = gain1*filter1_r+gain2*filter2_r+gain3*filter3_r+gain4*filter4_r
new_stereo = np.array([stereo_l, stereo_r]).T


# # Convert to (little-endian) 16 bit integers.
new_stereo = (new_stereo).astype("<h")

# print(new_stereo)


sample_rate = 44100
new_wav_file = wave.open("test.wav", "w")
new_wav_file.setnchannels(2)
new_wav_file.setsampwidth(2)
new_wav_file.setframerate(sample_rate)
new_wav_file.writeframes(new_stereo.tobytes())

# plt.figure(2)
# plt.title('After filtering')
# for channel in deinterleaved:
#     plt.plot(Time,channel)
# plt.show()
