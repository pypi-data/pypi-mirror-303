import pandas as pd
from formatter import process_dataframe

df = pd.read_excel("need_2.xlsx")


df_new = df.copy()
df_to_excel = process_dataframe(df_new)

df_to_excel.to_excel("out2.xlsx")
