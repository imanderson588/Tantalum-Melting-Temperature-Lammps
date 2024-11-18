import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
This python script can be used to read in the paarsed
data from the Parsed Data directory and create a bar chart
of the average BCC fraction over the final 1500 time steps
at each temperature. Tempearature below are hard coded for 
Tantlum but can be adopted to other simulations
'''


# List of temperatures and empty list to store bcc averages

temps = [2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400]
average = []

# Loop through each temperature and calculate the average BCC fraction
for temp in temps:
    data = pd.read_csv(f'../Parsed Data/parsed_cna_{temp}.csv', header=None, sep=' ', index_col=0)
    average_bcc = np.mean(data[1].values)
    average.append(average_bcc)

# Plot creation

plt.title('Average BCC Fraction Last 1500 Time Steps')
plt.xlabel('BCC Fraction')
plt.ylabel("Temperature (K)")
plt.yticks(temps)

plt.barh(temps, average, color='lightblue', height=80)

plt.savefig('bcc_fraction_bar.png', dpi=400)
