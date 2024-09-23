import numpy as np
import matplotlib.pyplot as plt
time_series = np.array([22.267092,22.988886,23.493668,22.776726,22.673071,22.718583,23.173136,24.021908,23.210611,23.116261,23.559649,24.352009,24.729418,23.927555,22.52656,22.828421,25.32357,21.215067])
q = int(input("Enter value of q: "))
n = len(time_series)
Tline = np.zeros(n)
if len(time_series) % 2 == 1:
    for i in range(q, n - q):
        Tline[i] = np.mean(time_series[i - q:i + q + 1])
else:
    d = 2 * q
    for i in range(q, n - q):
        Tline[i] = (0.5 * time_series[i - q] + np.sum(time_series[i - q + 1:i + q]) + 0.5 * time_series[i + q]) / d
seasonal_effect = np.zeros(n)
for i in range(n):
    sum_diff = 0
    count = 0
    for j in range(-(n // q), n // q):
        if 0 <= i + j * q < n:
            sum_diff += time_series[i + j * q] - Tline[i + j * q]
            count += 1
    if count > 0:
        seasonal_effect[i] = sum_diff / count
avg_seasonality = np.mean(seasonal_effect)
adjusted_seasonal = seasonal_effect - avg_seasonality
print("Calculated Trend:", Tline)
print("Extracted Seasonality:", adjusted_seasonal)
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(time_series, label="Original Data")
plt.legend(loc='upper left')
plt.subplot(312)
plt.plot(Tline, label="Trend", color='orange')
plt.legend(loc='upper left')
plt.subplot(313)
plt.plot(adjusted_seasonal, label="Seasonality", color='green')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()