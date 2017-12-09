from matplotlib import pyplot as plt
#from scipy.io import wavfile
#from scipy import signal
#import math
#from scipy.fftpack import dct
import os
import numpy as np
#import keras
import time
import random

'''

print(score)
x = np.arange(len(score)) + 1
plt.plot(x, score)
plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('Learning Curve of Policy Gradient: Reward per Episode')
plt.savefig('policy_gradient_curve.png')
'''

x = np.asarray([])
np.save('Q_Score', x)
np.save('PG_Score', x)
A = np.load('Q_Score.npy')
B = np.load('PG_score.npy')
print(A)
print(B)
'''
x = np.load('Q_Score.npy')
print(x)
'''