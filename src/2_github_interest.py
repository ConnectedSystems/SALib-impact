import pandas as pd
import matplotlib.pyplot as plt

from common import *


plt.style.use('seaborn-colorblind')

star_increase = pd.read_csv(f"{DATA_DIR}/2022-04-02_SALib_star_history.csv", 
                            index_col=1, 
                            names=["Repo", "Starred", "Count"],
                            parse_dates=True)

# Extract just year
star_increase.index = star_increase.index.str[11:15]
star_increase.index = map(int, star_increase.index)

# Data is cumulative sum, so we get the max for each year
yearly_count = star_increase.groupby(by=star_increase.index).max()
yearly_count.drop("Repo", inplace=True, axis=1)

yearly_count.loc[2010, "Count"] = 0.0
yearly_count.loc[2011, "Count"] = 0.0
yearly_count.sort_index(inplace=True)

ax = yearly_count.loc[:2013].plot(legend=False, alpha=0.0, figsize=(8,6))
yearly_count.loc[2013:2021].plot(legend=False, color='C0', ax=ax, marker='o')
yearly_count.loc[2021:].plot(ax=ax, color="C0", ls="--", legend=False, rot=45, grid=True)

ax.set_ylabel("GitHub Stars")
ax.set_xlabel("Year")
ax.set_title("Cumulative Stars of Repository")

ax.annotate("Repository created", xy=(2013, 1), xytext=(2010.1, 110),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate("Release of v1.0", xy=(2016, 80), xytext=(2010.8, 200),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate("Herman & Usher (2017)", xy=(2017, 120), xytext=(2012.1, 305),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.savefig(f"{FIG_DIR}/SALib_star_trend.png", dpi=300)
