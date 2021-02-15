from scipy.io import savemat
import numpy as np

data = np.loadtxt('data.txt')
savemat("data.mat", {'A': data})