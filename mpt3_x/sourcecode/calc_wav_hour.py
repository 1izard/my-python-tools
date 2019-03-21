wav_byte = 3.3 * (1024 ** 3)
frame = wav_byte / 2
sec = frame / 16000
hour = sec / 3600
print('wav_byte', wav_byte)
print('frame', frame)
print('sec', sec)
print('hour', hour)

'''
Result unless consider ch
    wav_byte 3543348019.2
    frame 1771674009.6
    sec 110729.6256
    hour 30.758229333333333

If consider ch = 2, frame = wav_byte / 2 / 2 -> 30.758 / 2
'''

