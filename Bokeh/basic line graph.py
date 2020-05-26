#Making a basic bokeh line graph with minimum requirements
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show

#creating the data
# the length should be equal otherwise warning gets generated as below
#BokehUserWarning: ColumnDataSource's columns must be of the same length. Current lengths: ('x', 6), ('y', 5)
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#creating the output file
output_file("line.html")

#creating the figure obect
f=figure()

#creating the line graph
f.line(x,y)
#showing the graph
show(f)
