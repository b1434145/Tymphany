import matplotlib.pyplot as plt
import numpy as np
import wave

# bass_low_pass = np.array([0.000016711401632480687583399980855602962,
# 	0.003059767600620552988055500520658824826,
# 	0.028706644937584960969312319889468199108,
# 	0.107556527291491413333979210165125550702,
# 	0.221280810207095418595812930107058491558,
# 	0.278759077123150289523323408502619713545,
# 	0.221280810207095474106964161364885512739,
# 	0.107556527291491441089554825794039061293,
# 	0.028706644937584967908206223796696576755,
# 	0.003059767600620553421736369514860598429,
# 	0.000016711401632480687583399980855602962])

bass_low_pass = np.array([0.000003089055423054337131918327744029007,
0.000015134363724602482265493320900962004,
0.000056916641478903750011458795299290614,
0.000145184575745511295664924578119325815,
0.000307763119613892752526873586305100616,
0.000583411714589119364919589383333686783,
0.001021093088992671565895520302547083702,
0.001678362181079298990835080296335490857,
0.002618625104165958703689165432137997414,
0.003907127645088793836680718385423460859,
0.005605700780897677169833936972054289072,
0.007766495192975994554807073200208833441,
0.010425147642233111369702847071039286675,
0.013594005394436300612759360717518575257,
0.017256157998100381256723068190694903024,
0.021361062416105480038508446227751846891,
0.02582248243508597843054452880551252747 ,
0.030519294844999197979795724222640274093,
0.035299456307097520912918753310805186629,
0.039987102982113317817258746345032704994,
0.044392407234299616214379113898758077994,
0.048323485123715842481928461893403436989,
0.051599377948626942713694631947873858735,
0.054062957813206594104293856162257725373,
0.055592556852051895621702470862146583386,
0.05611120308830462588556287073515704833 ,
0.055592556852051895621702470862146583386,
0.054062957813206614920975567883942858316,
0.051599377948626942713694631947873858735,
0.048323485123715842481928461893403436989,
0.044392407234299637031060825620443210937,
0.039987102982113345572834361973946215585,
0.035299456307097507035130945496348431334,
0.030519294844999184102007916408183518797,
0.025822482435085954144415865130213205703,
0.021361062416105500855190157949436979834,
0.017256157998100384726170020144309091847,
0.013594005394436298878035884740711480845,
0.010425147642233126982214130862303136382,
0.007766495192976005830509667049454947119,
0.005605700780897678904557412948861383484,
0.003907127645088805979745050223073121742,
0.002618625104165955667923082472725582193,
0.001678362181079301809760728758647019276,
0.001021093088992674384821168764858612121,
0.000583411714589119364919589383333686783,
0.000307763119613894595670566811662638429,
0.000145184575745513003283346242788809377,
0.000056916641478904054943319806847412679,
0.000015134363724605019976203294784777853,
0.000003089055423054337131918327744029007])

voice_high_pass = np.array([-0.000000266391372279984297950300919585742,
-0.000001298393877913319472561107584263063,
-0.000004858796683293104637119553396162885,
-0.000012335463186361147707565365239101851,
-0.000026031218856719190798834975830722271,
-0.000049135182207557869069492612057459269,
-0.000085648150175396129736050954139869873,
-0.000140238905414849941146945844216986643,
-0.00021801207997578457955037412041576772 ,
-0.000324177432156347311575927960802800953,
-0.00046362403753004958898223386576376015 ,
-0.000640419105058620151058046410241786361,
-0.00085726748204202542647661688945959213 ,
-0.001114981768029237778686035831299250276,
-0.001412021855628785987901707699165854137,
-0.001744164751337851614054752502624978661,
-0.002104359667308748713804300578544825839,
-0.002482809645044582302214619673463857907,
-0.002867300516184692355664553886640533165,
-0.003243772968172966945921142922770741279,
-0.003597106755461515915223147388246616174,
-0.003912060951739432246299088546948041767,
-0.00417429379662460822014713457406287489 ,
-0.004371372887353586547676265183781652013,
-0.004493683074762639707844247283219374367,
 0.995464587261945532681295389920705929399,
-0.004493683074762640575205985271622921573,
-0.004371372887353587415038003172185199219,
-0.00417429379662460822014713457406287489 ,
-0.003912060951739431378937350558544494561,
-0.003597106755461517649946623365053710586,
-0.003243772968172968680644618899577835691,
-0.002867300516184691488302815898236985959,
-0.002482809645044580567491143696656763495,
-0.002104359667308746979080824601737731427,
-0.001744164751337853131937793982331186271,
-0.00141202185562878642158257669336762774 ,
-0.001114981768029237345005166837097476673,
-0.000857267482042026619099006623514469538,
-0.000640419105058621018419784398645333567,
-0.000463624037530049697402451114314203551,
-0.00032417743215634834156799182203201326 ,
-0.000218012079975784281394776686902048368,
-0.000140238905414850157987380341317873444,
-0.0000856481501753963601290126073095621  ,
-0.000049135182207557869069492612057459269,
-0.00002603121885671934665289727062198466 ,
-0.000012335463186361293397232292978760171,
-0.000004858796683293130895140918279473397,
-0.000001298393877913537160028551939450203,
-0.000000266391372279984297950300919585742])





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
print(type(deinterleaved[0]))

#Get time from indices
fs = wav_file.getframerate()
Time = np.linspace(0, len(signal)/wav_file.getnchannels()/fs, num=len(signal)/wav_file.getnchannels())

# for test stereo
# fake = np.linspace(0, 0, num=len(signal)/wav_file.getnchannels())

#Plot
# plt.figure(1)
# plt.title('Signal Wave...')
# for channel in deinterleaved:
#     plt.plot(Time,channel)
# plt.show()

wav_file.close()


################ generate new file ##################
gain = 1.05


############### filter ##############
deinterleaved[0] = np.convolve(deinterleaved[0], bass_low_pass, mode='same')
deinterleaved[1] = np.convolve(deinterleaved[1], bass_low_pass, mode='same')

# Put the channels together with shape (2, 44100).
new_stereo = np.array([deinterleaved[0], deinterleaved[1]]).T

# Convert to (little-endian) 16 bit integers.
new_stereo = (new_stereo*gain).astype("<h")

print(new_stereo)


sample_rate = 44100
new_wav_file = wave.open("sound2.wav", "w")
new_wav_file.setnchannels(2)
new_wav_file.setsampwidth(2)
new_wav_file.setframerate(sample_rate)
new_wav_file.writeframes(new_stereo.tobytes())
