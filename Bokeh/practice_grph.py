from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df=pandas.read_csv("bachelors.csv")
x=df["Year"]
y=df["Engineering"]



f=figure()

f.title.text="Bachelors Passing Trend"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Year"
f.yaxis.axis_label="Percentage of Women"

f.line(x,y)
output_file("Engineering.html")
show(f)