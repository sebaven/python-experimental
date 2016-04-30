# coding: utf-8
import csv_loader
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# load towers coordinates form CSV file
loader = csv_loader.CsvLoader("/Users/sebastien/Documents/workspace/bird-towers/samples/towers.csv")
towers = loader.load()

# set map initial size
plt.figure(figsize=(10,8))

# create map renderer and configure it to display Finland
m = Basemap(projection='merc', resolution='l', lat_0=58, lon_0=18, area_thresh=1000, llcrnrlon=18, llcrnrlat=58, urcrnrlon=35, urcrnrlat=75)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

# draw the towers on the map
for tower in towers:
    x, y = m(tower.longitude, tower.latitude)
    m.plot(x, y, 'bo', markersize=2)

# render the map
plt.title("Bird watching towers in Finland")
plt.show()

