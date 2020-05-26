from bokeh.plotting import figure,output_file,show
import pandas

df = pandas.read_excel("weatherdata.xlsx")

x=df["Temperature"]/10
y=df["Pressure"]/10

f=figure(width=500,height=400,tools='pan')

f.title.text="Temperature and Air Presure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature(°C)"
f.yaxis.axis_label="Pressure(hPa)"

output_file("weather.html")
f.circle(x,y,size=0.5,alpha=0.5) #alpha is for transparency
show(f)