import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

# Set the (countries,roads).shp paths
countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"
roads = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_roads.shp"

arcpy.env.overwriteOutput = True

#### 3333
# set output shapefile path
outputPath_3 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Roads in asia'

# Create a feature layer of Asia continent
#arcpy.MakeFeatureLayer_management(countries, 'countries_layer',)
arcpy.MakeFeatureLayer_management(roads, "roads_layer", """ "continent" = 'Asia' """)

# Select roads that WITHIN with the Asia continent layer
#arcpy.SelectLayerByLocation_management("roads_layer", "WITHIN", "countries_layer")

# Create a new shapefile of selected roads
arcpy.FeatureClassToFeatureClass_conversion("roads_layer",outputPath_3, "Roads_in_Asia")

# Get the number of selected roads
output_roads = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Roads in asia\Roads_in_Asia.shp'

# Count the number of selected roads by opening a SearchCursor
num_roads = 0
with arcpy.da.SearchCursor(output_roads, ['FID']) as cursor:
    for row in cursor:
        num_roads += 1
print("Number of roads in Asia: {}".format(num_roads))


# Count the number of selected roads by function
num_roads = arcpy.GetCount_management(output_roads)

# Print the number of selected roads
print("Number of roads in Asia: {}".format(num_roads))

