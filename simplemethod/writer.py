import numpy as np

# Generate synthetic raw data (replace this with your actual data source)
raw_data = np.random.normal(0, 1, 10000)  # Replace with your data source or generation code

# Calibration: Apply a calibration factor (example: multiply by 2)
calibrated_data = raw_data * 2.0

# Save raw data to a text file
with open('raw_data.txt', 'w') as raw_file:
    for value in raw_data:
        raw_file.write(f'{value}\n')

# Save calibrated data to a text file
with open('calibrated_data.txt', 'w') as calibrated_file:
    for value in calibrated_data:
        calibrated_file.write(f'{value}\n')

print("Raw data and calibrated data have been saved to 'raw_data.txt' and 'calibrated_data.txt'.")
