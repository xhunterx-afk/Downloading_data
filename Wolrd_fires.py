import csv

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
from datetime import datetime

# Making a variable with a number to set a limit

row_number=1000

# Opening file

with open("world_fires_1_day.csv") as W_F:
    reader = csv.reader(W_F)
    header = next(reader)

    # Making a variable with the value of 0 for teh counter

    num_row = 0

    # Looping through the information and storing it in the empty list

    brightness,lons,lats,dates=[], [], [],[]

    for row in reader:

        bright=float(row[2])
        acq_date= datetime.strptime(row[5],"%Y-%m-%d")

        dates.append(acq_date)
        brightness.append(bright)
        lons.append(row[1])
        lats.append(row[0])

        # starting the counter

        num_row+=1

        # Breaking loop if num_row equals to row_number

        if num_row == row_number:
            break

# Using a map as a type. Setting lon and lat as the coordination,
# Making as the point bigger depending on the fire,
# Making a scaling color as for the biggest fires it takes a specific color,
# Naming the color scale

data = [{"type":"scattergeo",
      "lon":lons,
      "lat":lats,
       "text":dates,
      "marker": {
      "size": [bris/20 for bris in brightness],
      "color": brightness,
      "colorscale": "YlOrRd",
      "reversescale": True,
      "colorbar": {"title": "Brightness"}}}]

# Giving the graph a title and putting it in the middle with some modification text type and text size

my_layout=Layout(title={"text": "World Fires",
                        "x":0.5,
                        "y":0.96,
                        "xanchor":"center",
                        "yanchor":"top"},
                        font=dict
                        (family="Courier New, monospace",
                        size=35))

# Saving the graph and running the data and the layout

fig={"data": data, "layout": my_layout}
offline.plot(fig, filename="Worldfires.html")