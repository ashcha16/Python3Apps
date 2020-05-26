from pandas_datareader import DataReader
from bokeh.plotting import figure,output_file,show
import datetime


def stock_data(stock,start,end):
    #print(start,str(start),end,str(end))
    try:
        if '/' in start :
            start_time=datetime.datetime.strptime(str(start),"%d/%m/%Y").strftime("%Y-%m-%d")

        if '/' in end:
             end_time=datetime.datetime.strptime(str(end),"%d/%m/%Y").strftime("%Y-%m-%d")

    
        df = DataReader(name=stock,data_source="yahoo",start=start_time,end=end_time)

        f=figure(x_axis_type="datetime",width=1000,height=300,sizing_mode="scale_width")
        f.title.text="Stock Analysis of "+ stock
        f.grid.grid_line_alpha=0.3

        width = 12*60*60*1000

        def Inc_dec(o,c):
            if o > c:
                return "Decrease"
            elif c > o:
                return "Increase"
            else:
                return "Equal"

        df["Status"]=[Inc_dec(o,c) for o,c in zip(df["Open"],df["Close"])]
        df["Height"]=abs(df["Open"]-df["Close"])
        df["Y_axis"]=(df["Open"]+df["Close"])/2

        f.rect(df.index[df.Status=="Increase"],df.Y_axis[df.Status=="Increase"],width,df.Height[df.Status=="Increase"],fill_color="green",line_color="black")
        f.rect(df.index[df.Status=="Decrease"],df.Y_axis[df.Status=="Decrease"],width,df.Height[df.Status=="Decrease"],fill_color="red",line_color="black")

        f.segment(df.index,df.High,df.index,df.Low,line_color="black")
        #print(df)
        return f        
    except Exception as e:
        return str(e)
    

#s='1/03/2016'
#e='10/03/2016'
#stock_data("AAPL",s,e)