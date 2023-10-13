# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:16:03 2023

@author: FAHMI RAMADHAN
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to generate 2D box signal
def generate_box_signal_2d(t1, t2, width1, width2):
    signal = np.zeros((len(t1), len(t2)))
    for i in range(len(t1)):
        for j in range(len(t2)):
            if abs(t1[i]) <= width1 and abs(t2[j]) <= width2:
                signal[i][j] = 5.0
    return signal

# Function to perform 2D FFT
def fft2(signal):
    # Perform 1D FFT along the rows
    fft_rows = np.fft.fft(signal, axis=0)
    
    # Perform 1D FFT along the columns
    fft_result = np.fft.fft(fft_rows, axis=1)
    
    return fft_result

# Time intervals
t1 = np.linspace(-2, 2, 1000)
t2 = np.linspace(-2, 2, 1000)

# Generate 2D box signals
box_signal1 = generate_box_signal_2d(t1, t2, 1, 1)
box_signal2 = generate_box_signal_2d(t1, t2, 2, 2)
box_signal3 = generate_box_signal_2d(t1, t2, 2.5, 2.5)

# Compute 2D FFT for each box signal
fft_result1 = fft2(box_signal1)
fft_result2 = fft2(box_signal2)
fft_result3 = fft2(box_signal3)

# Plot the signals and their FFT
plt.figure(figsize=(15, 10))

# Plot box signals
plt.subplot(3, 2, 1)
plt.imshow(box_signal1, cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D Box Signal 1')
plt.xlabel('Time 1')
plt.ylabel('Time 2')
plt.colorbar()

plt.subplot(3, 2, 3)
plt.imshow(box_signal2, cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D Box Signal 2')
plt.xlabel('Time 1')
plt.ylabel('Time 2')
plt.colorbar()

plt.subplot(3, 2, 5)
plt.imshow(box_signal3, cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D Box Signal 3')
plt.xlabel('Time 1')
plt.ylabel('Time 2')
plt.colorbar()

# Plot FFT results
plt.subplot(3, 2, 2)
plt.imshow(np.abs(fft_result1), cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D FFT Result - Box Signal 1')
plt.xlabel('Frequency 1')
plt.ylabel('Frequency 2')
plt.colorbar()

plt.subplot(3, 2, 4)
plt.imshow(np.abs(fft_result2), cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D FFT Result - Box Signal 2')
plt.xlabel('Frequency 1')
plt.ylabel('Frequency 2')
plt.colorbar()

plt.subplot(3, 2, 6)
plt.imshow(np.abs(fft_result3), cmap='hot', extent=[t1.min(), t1.max(), t2.min(), t2.max()])
plt.title('2D FFT Result - Box Signal 3')
plt.xlabel('Frequency 1')
plt.ylabel('Frequency 2')
plt.colorbar()

plt.tight_layout()
plt.show()

