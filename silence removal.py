import os
import soundfile as sf

def count_zeros(samples):
    consecutiveZeros=0
    for sample in samples:
        if sample == 0:
            consecutiveZeros+=1
        else:
            break
    return consecutiveZeros


def read_audio(audio,removeZeros,removeZerosFromStart):
    '''Read the audio, remove first consecutive block of zeros from start or end or from both '''
                            
    if not os.path.exists(audio):
        print('%s NOT FOUND !!'%(audio))
        return
        
    samples,fs = sf.read(audio)
    
    zeros_at_start=-99 # -99 indicates zero-removal script was not triggered
    zeros_at_end=-99
        
    if removeZeros:
        zeros_at_end=count_zeros(samples[::-1])
        samples=samples[0:len(samples)-zeros_at_end]            
            
    if removeZerosFromStart:
        zeros_at_start=count_zeros(samples)
        samples=samples[zeros_at_start :len(samples)]
                            
    print('Consecutive zeros in start = %d and at end = %d' %(zeros_at_start,zeros_at_end))
        
    return samples, fs

input_folder = "D:\\School2\\DISSERTATION\\Voice Files\\New folder\\ASVspoof2021_DF_eval\\flac"
output_folder = "D:\\School2\\DISSERTATION\\processed2"

for filename in os.listdir(input_folder):
    audio_path = os.path.join(input_folder, filename)
    processed_samples, fs = read_audio(audio_path, removeZeros=True, removeZerosFromStart=True)
    output_path = os.path.join(output_folder, filename)
    sf.write(output_path, processed_samples, fs)

