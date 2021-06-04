"""Plot citation using data sourced from Google Scholar
with the Publish or Perish tool.

https://harzing.com/resources/publish-or-perish/windows

Data file: SALib_PoPCites.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

from common import *


citing_pubs = pd.read_csv(DATA_DIR+"/SALib_PoPCites.csv", usecols=["Year"], dtype={'Year': 'Int64'})

num_citations = len(citing_pubs.index)


# Add citation count column and dummy entries for 2015/16 for space in the plot
citing_pubs['citations'] = 1
dummy = pd.DataFrame({"Year": [2015, 2016], "citations": [0, 0]})
citing_pubs = pd.concat((dummy, citing_pubs))

pubs_per_year = citing_pubs.groupby(["Year"]).count()

ax = pubs_per_year.loc[2017:2020].plot(legend=False, marker='o')
(pubs_per_year.loc[2015:2017]
              .plot(ax=ax, color="C0",
                    ls="-", legend=False, alpha=0.5, figsize=(8,6)))

(pubs_per_year.loc[2020:]
              .plot(ax=ax, color="C0", 
                    ls="-.", legend=False, rot=45, grid=True))


ax.set_ylabel("Citations")
ax.set_xlabel("Year")
ax.set_title(f"Citations of Herman & Usher (2017)\nTotal Citations: {num_citations}")

ax.annotate("Paper published", xy=(2017, 20), xytext=(2015.4, 45),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.savefig(f"{FIG_DIR}/SALib_citation_trend.png", dpi=300)
