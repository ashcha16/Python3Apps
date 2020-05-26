from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file
from bokeh.embed import components
from bokeh.resources import CDN #content delivery network

start_time=datetime.datetime(2016,1,1)
end_time=datetime.datetime(2016,5,31)
df=data.DataReader(name="GOOG",data_source="yahoo",start=start_time,end=end_time)#name= stock symbol and time must be datetime format
print(df)

f=figure(x_axis_type="datetime",width=1000,height=300,sizing_mode="scale_width")
f.title.text="Candlestick Chart"
f.grid.grid_line_alpha=0.5

#we need to get values where close is greater than open for gray  quad and close less than open for red quad
#green_x=df.index[df.Close>df.Open] #this will those dates where close > open
#red_x=df.index[df.Close<df.Open] #this will those dates where close < open
def inc_dec(clse,opn):
    if clse>opn:
        value="Increase"
    elif clse<opn:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]#list compehension for adding new column
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)
print(df)

width_hours_12=12*60*60*1000 #this is because graph expects milisecond value for width
#for y axis we take the centre point of rectangle by getting mean of open and close
#y=(df.Open+df.Close)/2
#for height of rectangle we take absolute diff between open and close price
#h=abs(df.Open-df.Close)
#f.quad(left=,right=,top=df,bottom=df,)
#f.quad(left=,right=,top=df,bottom=df,)
#using rectangles here

f.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],width_hours_12,df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")
f.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],width_hours_12,df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")
#for line inside the rectangle to show high and low values
#segment takes 4 arguments x high point,y highpoint,x low point, y low point
#x value remains same
f.segment(df.index,df.High,df.index,df.Low,line_color="black")
output_file("candle.html")
#show(f)

script,div=components(f)#this return a tuple of two value script and div of type string

cdn_javascript=CDN.js_files[0] #this give list of links
cdn_css=CDN.css_files[0]#this also gives list of links and we take first value



