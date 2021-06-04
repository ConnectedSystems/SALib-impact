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

ax = prog_pop.loc["2015":, "Python"].plot(title="Python PYPL Index", figsize=(8,6), rot=45)
ax.set_ylabel("Percentage of searches")


plt.tight_layout()
plt.savefig(f"{FIG_DIR}/PYPL_trend.png", dpi=300)


