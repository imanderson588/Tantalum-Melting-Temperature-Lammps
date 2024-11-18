import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
This python script can be used to read in the paarsed
data from the Parsed Data directory and scatter plot
of the average BCC fraction over the final 1500 time steps
at each temperature. Tempearature below are hard coded for 
Tantlum but can be adopted to other simulations
'''

# List of temperatures

temps = [2400, 2500, 2600, 2700, 2800, 2900, 2910, 2920, 2930, 2940, 2950, 2960, 2970, 2980, 2990, 3000, 3100, 3200, 3300, 3400]

# Loop through each temperature and calculate the average BCC fraction then plot point
for temp in temps:
    data = pd.read_csv(f'../Parsed Data/parsed_cna_{temp}.csv', header=None, sep=' ', index_col=0)
    average_bcc = np.mean(data[1].values)
    plt.plot(temp, average_bcc, 'bo')

plt.title('Average BCC Fraction Last 1500 Time Steps')
plt.xlabel('Temperature (K)')
plt.ylabel('BCC Fraction')

plt.savefig('bcc_fraction_scatter.png', dpi=400)
