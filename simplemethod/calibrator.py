import numpy as np
import matplotlib.pyplot as plt

# Load raw data (replace with actual data loading code)
raw_data = np.loadtxt('raw_data.txt')

# Calibration: Apply a calibration factor
calibrated_data = raw_data * 2.0

# Data Reduction: Calculate the mean of calibrated data
reduced_data = np.mean(calibrated_data)

# Visualization: Create a histogram
plt.hist(calibrated_data, bins=20)
plt.xlabel('Calibrated Values')
plt.ylabel('Frequency')
plt.title('Calibrated Data Histogram')
plt.show()

# Output: Save reduced and calibrated data (replace with actual saving code)
np.savetxt('calibrated_data.txt', calibrated_data)
