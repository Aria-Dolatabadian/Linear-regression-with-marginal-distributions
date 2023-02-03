import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv (r'OilPro.csv')
print(df)

sns.set_theme(style="whitegrid")
# sns.set_theme(style="darkgrid")
g = sns.jointplot(x="Oil yiled", y="Protein yield", data=df,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="b", height=7)
plt.show()
