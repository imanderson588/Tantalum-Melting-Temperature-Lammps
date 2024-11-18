import pandas as pd

'''
This file can be used to parse the CNA output files from LAMMPS
the temps below must be updated for the simulation data being parsed
'''

# List of temperature output files to be parsed
temps = [2910]

# Loop through each temperature and parse the CNA output file
for temp in temps:
    # Read in path (Specific to this repository)
    file_path = f'../Data/cna_output_{temp}.txt'

    with open (file_path, 'r') as file:
        lines = file.readlines()

    time_steps = []
    structure_index = []

    # Locate lines containing relevant structure information
    # then only parse the final data from final 1500 time steps
    for i , line in enumerate(lines):
        if 'ITEM: TIMESTEP' in line:
            line = lines[i+1]
            step = int(line)
            if step >= 6000:
                time_steps.append(step)
                line = lines[i+9]
                structure_info = lines[(i+9):(i+409)]
                structure_index.append([int(structure_info[i].split()[2]) for i in range(0,399)])

    # Calculate the percentage of BCC atoms at each time step THIS WILL NEED TO BE UPDATEF FOR OTHER SIMULATIONS
    percentage_bcc = [structure_index[i].count(3)/400 for i in range(len(structure_index))]

    # Output parsed data the new files
    # The length of the number will need to be updated 
    # based on temperatures used
    parsed_data = pd.DataFrame(percentage_bcc, index=time_steps)
    parsed_data.to_csv(f'../Parsed Data/parsed_cna_{file_path[19:23]}.csv', sep=' ', index=True, header=False)
