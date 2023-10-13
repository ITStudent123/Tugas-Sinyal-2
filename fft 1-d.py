import math
import matplotlib.pyplot as plt

def fft_real(signal):
    n = len(signal)
    if n <= 1:
        return signal
    
    even_signal = [signal[i] for i in range(0, n, 2)]
    odd_signal = [signal[i] for i in range(1, n, 2)]
    
    even_fft = fft_real(even_signal)
    odd_fft = fft_real(odd_signal)
    
    factor = [math.cos(2 * math.pi * k / n) - 1j * math.sin(2 * math.pi * k / n) for k in range(n // 2)]
    combined_fft = []
    for k in range(n // 2):
        t = factor[k] * odd_fft[k]
        combined_fft.append(even_fft[k] + t)
        combined_fft.append(even_fft[k] - t)
    
    return combined_fft

t = [i for i in range(512)]
signal = [math.sin(2 * math.pi * 50 * i / 512) + 0.5 * math.sin(2 * math.pi * 120 * i / 512) for i in t]

fft_result = fft_real(signal)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Input Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot([abs(x) for x in fft_result])
plt.title('FFT Result')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
