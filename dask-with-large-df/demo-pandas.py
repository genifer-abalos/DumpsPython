import pandas as pd
import time

start = time.perf_counter()

df = pd.read_csv('recipes.csv')

end = time.perf_counter()
print(f"Runtime: {end-start}s")