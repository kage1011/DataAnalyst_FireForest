import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("forestfires1.csv")
#độ tập trung và độ phân tán
print(df["area"].describe())
print(df["area"].mode())
print((df["area"].max())-(df["area"].min()))
print((df["area"].quantile(0.75))-(df["area"].quantile(0.25)))



