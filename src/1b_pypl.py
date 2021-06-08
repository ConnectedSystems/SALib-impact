"""Create plot of python popularity using
PopularitY of Programming Languages data sourced via Kaggle.com

From the website:
"The PYPL PopularitY of Programming Language Index is created by
analyzing how often language tutorials are searched on Google :
the more a language tutorial is searched, the more popular the language
is assumed to be. It is a leading indicator. The raw data comes from Google Trends."

Data accessible via: https://www.kaggle.com/muhammadkhalid/most-popular-programming-languages-since-2004
(sign-up required)

Data License: CC0 Public Domain
"""

import pandas as pd

from common import *


# Programming language search trends
prog_pop = pd.read_csv(f"{DATA_DIR}/pl_pop.zip",
                       compression='zip',
                       parse_dates=True,
                       index_col=0)

prog_pop.iloc[-1, :].sort_values(ascending=False)

ax = prog_pop.loc["2010":, ["Python", "Java", "R"]].plot(title="PYPL Index", 
                                                         figsize=(8,6), 
                                                         rot=45,
                                                         legend=False)
ax.set_ylabel("Percentage of searches")

py_loc = prog_pop.iloc[-1, :]["Python"]
java_loc = prog_pop.iloc[-1, :]["Java"]
r_loc = prog_pop.iloc[-1, :]["R"]
ax.text("2021", py_loc+1.5, "Python")
ax.text("2021", java_loc+1.5, "Java")
ax.text("2021", r_loc+1.5, "R")

# ax.text("2011-06-01", r_loc-15, "Repository created")

plt.tight_layout()
plt.savefig(f"{FIG_DIR}/PYPL_trend.png", dpi=300)
