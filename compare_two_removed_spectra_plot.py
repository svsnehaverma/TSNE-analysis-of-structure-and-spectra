import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
########################################### Sorted SDMEAN ######################################################
with open('/data2/sneha/sneha-large-set/xanes-short/ABECIT1_4_swap_0_1.txt') as f:
    lines = f.readlines()[2:]
    energy = [float(line.split()[0]) for line in lines]
    Intensity = [float(line.split()[1]) for line in lines]
    #sd = [float(line.split()[2]) for line in lines]
    
with open('/data2/sneha/sneha-large-set/xanes-short/OSODEH1_18.txt') as f:
    lines = f.readlines()[2:]
    energy = [float(line.split()[0]) for line in lines]
    Intensity_or = [float(line.split()[1]) for line in lines]
    
with open('/data2/sneha/sneha-large-set/xanes-short/OSODEH1_15.txt') as f:
    lines = f.readlines()[2:]
    energy = [float(line.split()[0]) for line in lines]
    Intensity_or1 = [float(line.split()[1]) for line in lines]  
    
with open('/data2/sneha/sneha-large-set/xanes-short/VADPEV1_4.txt') as f:
    lines = f.readlines()[2:]
    energy = [float(line.split()[0]) for line in lines]
    Intensity_or2 = [float(line.split()[1]) for line in lines]  
          
      
#print(type(Intensity))i
plt.plot(energy, Intensity, color = 'blue', label = "ABECIT1_4_swap_0_1.txt")
plt.plot(energy, Intensity_or, color = 'black', label = "OSODEH1_18.txt")
plt.plot(energy, Intensity_or1, color = 'red', label = "OSODEH1_15.txt")
plt.plot(energy, Intensity_or2, color = 'green', label = "VADPEV1_4.txt")
#plt.text(7100, color='red', fontsize=12)
plt.ylabel('Intensity', fontsize = 14, weight = 'bold' )
plt.xlabel('Energy', fontsize = 14, weight = 'bold'  )
plt.title('Spectra Performance',  fontsize = 14, weight= 'bold')
leg = plt.legend(loc='best')
plt.show()
