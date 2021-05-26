import pandas as pd
import matplotlib.pyplot as plt

from common import *


plt.style.use('seaborn-colorblind')

star_increase = pd.read_csv(f"{DATA_DIR}/SALib_star_history.csv", 
                            index_col=1, 
                            names=["Repo", "Starred", "Count"],
                            parse_dates=True)

# Extract just year
star_increase.index = star_increase.index.str[11:15]
star_increase.index = map(int, star_increase.index)

# Data is cumulative sum, so we get the max for each year
yearly_count = star_increase.groupby(by=star_increase.index).max()

ax = yearly_count.loc[:2020].plot(legend=False)
yearly_count.loc[2020:].plot(ax=ax, color="C0", ls="-.", legend=False)

ax.set_ylabel("GitHub Stars")
ax.set_xlabel("Year")
ax.set_title("Cumulative Stars of Repo")

ax.annotate("Repository created", xy=(2013, 1), xytext=(2014, 200),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.savefig(f"{FIG_DIR}/SALib_star_trend.png", dpi=300)