import folium
import pandas

def colors_func(elv):
    if el>0 and el<=2000:
        return "green"
    elif el>2000 and el<=3000:
        return "orange"
    else:
        return "red"
      
data = pandas.read_csv("C:/Users/Ashish/Desktop/Python_3/App2_Web_Map/Data/coordinates.txt")
lt = list(data["LAT"])
ln = list(data["LON"])
elevation = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
""" # Additional styling

map = folium.Map(location=[38.58,-99.09],zoom_start=7,tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lat,lon,el in zip(lt,ln,elevation): #Zip function used to iterate multiple lists
    #styled version
    iframe = folium.IFrame(html=html % str(el),width=200,height=100)
    #for circle markers
    fgv.add_child(folium.CircleMarker(location=[lat,lon],radius=6,popup=folium.Popup(iframe),
    fill_color=colors_func(el),color="black",fill=True,fill_opacity=0.7))
    #fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(iframe),icon=folium.Icon(color=colors_func(el))))
    #basic version
    #In this case popup value elevation doesn't have "" so only str(el) can also be used instead of folium.Popup
    #fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(str(el)+ " m",parse_html=True),icon=folium.Icon(color="red")))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("C:/Users/Ashish/Desktop/Python_3/App2_Web_Map/Data/world.json","r",encoding="utf-8-sig").read()
,style_function= lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 1000000
else "orange" if 1000000<= x["properties"]["POP2005"] < 2000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("C:/Users/Ashish/Desktop/Python_3/App2_Web_Map/Map1.html")