from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df=pandas.read_csv("data.csv")
x=df["x"]
y=df["y"]


output_file("linepanda.html")

f=figure()
f.line(x,y)

show(f)
