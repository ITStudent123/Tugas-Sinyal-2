# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:47:40 2023

@author: FAHMI RAMADHAN
"""

def convolv(sinyal1, sinyal2):
    m, n = len(sinyal1), len(sinyal2)
    panjang_output = m + n - 1
    sinyal_output = [0] * panjang_output
    sinyal2_flipped = sinyal2[::-1]
    
    for i in range(panjang_output):
        for j in range(m):
            if i - j >= 0 and i - j < n:
                sinyal_output[i] += sinyal1[j] * sinyal2_flipped[i - j]
    
    return sinyal_output

print("Tugas Konvolusi")
print("Muhammad Fahmi Ramadhan")
print("5009211007")

sinyal1 = [0,2,4,6,8]
sinyal2 = [16,18,20,24,26]

print(convolvA(sinyal1, sinyal2))