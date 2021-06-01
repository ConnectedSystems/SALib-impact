"""Plot citation trend.

Data source:
https://app.dimensions.ai/analytics/publication/overview/timeline?or_subset_publication_citations=pub.1068918762&local:indicator-y1=timeline-source-published

Citations per year:
2021-06-01_SALib_citations.csv

Total citations (publications can cite more than once)
2021-05-26_SALib_total_citations_year.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

from common import *


plt.style.use('seaborn-colorblind')

yearly_citations = pd.read_csv(f"{DATA_DIR}/2021-06-01_SALib_citations.csv", index_col=0)

ax = yearly_citations.loc[2017:2020].plot(legend=False, marker='o')
(yearly_citations.loc[2015:2017]
                 .plot(ax=ax, color="C0",
                       ls="-", legend=False, alpha=0.5))

(yearly_citations.loc[2020:]
                 .plot(ax=ax, color="C0", 
                       ls="-.", legend=False, rot=45, grid=True))


ax.set_ylabel("Citations")
ax.set_xlabel("Year")
ax.set_title("Citations of Herman & Usher (2017)")

ax.annotate("Paper published", xy=(2017, 5), xytext=(2016, 45),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.savefig(f"{FIG_DIR}/SALib_citation_trend.png", dpi=300)
