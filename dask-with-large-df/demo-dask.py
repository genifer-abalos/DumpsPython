import dask.dataframe as dd
import dask.datasets as ds
import dask.array as da
import time


# Dataframes
start = time.perf_counter()
# reading a large file
ddf = dd.read_csv(r"recipes.csv")

end = time.perf_counter()
print(f"Runtime: {end-start}s")

# how many partitions the whole ddf was divided
print(ddf.npartitions)  # auto <- 20

# we can also set the number of partitions by size
ddf_with_blocksize = dd.read_csv(r"recipes.csv", blocksize="10mb")
print(ddf_with_blocksize.npartitions)   # 70 partitions = ~700mb/10mb
# GOOD RULE of THUMB: keep your partitions under 100mb in size

# print(ddf.partitions[-1])     # the last partition
# print(ddf_with_blocksize.shape)


print("-------------------------------")
# Datasets
# loading time series data
dsf = ds.timeseries(
    start='2000-01-01',
    end='2001-01-01',
)

# print(dsf.npartitions)
# print(dsf.head())

# calculate the mean of the x column
print(f"Mean of column x = {dsf.x.mean().compute()}")
print(f"Mean of column y = {dsf.y.mean().compute()}")

print("-------------------------------")
# array
the_large_array = da.random.random( (10000, 10000) )
print(the_large_array)
the_add = the_large_array[0] + the_large_array[1]
print(the_add.compute())
# slicing
sliced = the_large_array[::2, 5000:].mean(axis=1)
print(sliced.compute())