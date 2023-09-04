import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

airports = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_airports.shp"

arcpy.env.overwriteOutput = True


with arcpy.da.SearchCursor(airports,['name','location','wikipedia','type']) as airports_cusror:
    for x in airports_cusror:
        if x[3] == 'major':
            print("Airport Name: {}".format(x[0].encode('utf-8')))
            print("Location: {}".format(x[1]))
            print("Wikipedia Link: {}".format(x[2]))
            print('\n')