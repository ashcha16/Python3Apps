from motion_detect_App import df
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
#print(df)
cds=ColumnDataSource(df)
print(cds)

f = figure(x_axis_type="datetime",width=1000,height=300,title="Motion Graph")
f.yaxis.minor_tick_line_color=None
f.ygrid[0].ticker.desired_num_ticks=1
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)
q=f.quad(left="Start_string",right="End_string",top=1,bottom=0,color="green",source=cds)

output_file("Quad_Graph3.html")
show(f)