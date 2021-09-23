import pandas as pd
import matplotlib.pyplot as plt

from common import *


plt.style.use('seaborn-colorblind')

for_spread = pd.read_csv(f"{DATA_DIR}/2021-09-23_FoR_data.csv", 
                            index_col=0)

# Strip FoR ID number
for_spread.index = for_spread.index.str[3:]

ax = (for_spread.sort_values('Fields of Research', ascending=True)
           .plot.barh(legend=False, 
                      grid=True, 
                      xlim=(0.5,100), 
                      logx=True, 
                      figsize=(12,6)))  # 

ax.set_title("Fields of Research")
ax.set_xlabel("Number of Publications")

# ax.yaxis.label.set_size(10)
ax.tick_params(axis='y', labelsize=12)

plt.tight_layout()
plt.savefig(f"{FIG_DIR}/SALib_FoR_spread.png", dpi=300)