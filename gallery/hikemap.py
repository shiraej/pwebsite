
import pandas as pd
import gpxpy, folium

def process_gpx(filename):

	gpx = gpxpy.parse(open(filename)) 

	#(1)make DataFrame
	track = gpx.tracks[0]
	segment = track.segments[0]
	# Load the data into a Pandas dataframe (by way of a list)
	data = []
	segment_length = segment.length_3d()
	for point_no, point in enumerate(segment.points):
		data.append([point.longitude, point.latitude,point.elevation,
		point.time, segment.get_speed(point_no)])
	columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
	gpx_df = pd.DataFrame(data, columns=columns)

	#2(make points tuple for line)
	points = []
	for track in gpx.tracks:
		for segment in track.segments: 
			for point in segment.points:
				points.append(tuple([point.latitude, point.longitude]))
	pts_ser = pd.Series(points)
	
	return gpx_df, pts_ser

def generate_map(filename, hikeid):
	df = process_gpx(filename)[0]
	points = process_gpx(filename)[1]

	#generate map
	mymap = folium.Map( location=[ df.Latitude.mean(), df.Longitude.mean() ], zoom_start=12, tiles=None)

	folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', max_zoom=17, name= 'Topo Map - Higher Zoom', attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)').add_to(mymap)
	
	
	#draw route
	folium.PolyLine(points, color='red', weight=4.5, opacity=1).add_to(mymap)

	#start/stop marker
	folium.Marker(
	    location=list(points.iloc[0]),
	    icon=folium.Icon(color="green", prefix="fa", icon="fa-circle" ),
	).add_to(mymap)
	folium.Marker(
	    location=list(points.iloc[-1]),
	    icon=folium.Icon(color="red", prefix="fa", icon="fa-circle" ),
	).add_to(mymap)

	

	mymap.save('./gallery/templates/gallery/maps/{0}.html'.format(hikeid))