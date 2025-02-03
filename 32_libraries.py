import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy Example
arr = np.array([1, 2, 3, 4])
print("NumPy Array:", arr)

# Pandas Example
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
print("\nPandas DataFrame:\n", df)

# Matplotlib Example
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')
plt.title("Simple Plot")
plt.show()
