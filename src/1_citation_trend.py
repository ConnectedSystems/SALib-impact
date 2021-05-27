import pandas as pd
import matplotlib.pyplot as plt

from common import *


plt.style.use('seaborn-colorblind')

yearly_citations = pd.read_csv(f"{DATA_DIR}/2021-05-26_SALib_total_citations_year.csv", index_col=0)

ax = yearly_citations.loc[:2020].plot(legend=False)
(yearly_citations.loc[2020:]
                 .plot(ax=ax, color="C0", 
                       ls="-.", legend=False, rot=45, grid=True))

ax.set_ylabel("Citations")
ax.set_xlabel("Year")
ax.set_title("Citations of Herman & Usher (2017)")

ax.annotate("Paper published", xy=(2017, 1), xytext=(2015, 120),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.savefig(f"{FIG_DIR}/SALib_citation_trend.png", dpi=300)
