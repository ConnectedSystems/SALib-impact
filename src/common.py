import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

# fivethirtyeight uses a slightly off-white background
# which does not look pleasant on paper.
plt.rcParams["figure.facecolor"] = 'white'
plt.rcParams["axes.facecolor"] = 'white'
plt.rcParams["savefig.facecolor"] = 'white'

DATA_DIR = "../data"
FIG_DIR = "../figures"