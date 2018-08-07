import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot

# 1. Prepare data
labels = ["web","Android","ios","react native"]
values = [400, 250, 200, 150]
color = ["green","blue","orange","gold"]
explode = [0,0,0,0.2]

# 2. plot
pyplot.pie(
    values,
    labels=labels,
    colors=color,
    explode=explode
    )
pyplot.axis('equal')

# 3. show
pyplot.show()