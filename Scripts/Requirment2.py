import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

# Set the (countries,airports).shp paths
countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"
airports = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_airports.shp"

arcpy.env.overwriteOutput = True

#### 222
## print airports name

# set output shapefile path
outputPath_2 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Airports'

# Create a feature layer from the countries shapefile
arcpy.MakeFeatureLayer_management(countries, "countries_layer")
#
#
# # Create a feature layer from the airports shapefile with "military" type
arcpy.MakeFeatureLayer_management(airports, 'airports_layer', """ "type" = 'military' """)
#
# # Use Select Layer By Location to select countries that are completely within military airports
arcpy.SelectLayerByLocation_management("airports_layer", "WITHIN", "countries_layer")
#
# # Create a new feature class of the selected countries using FeatureClassToFeatureClass_conversion
arcpy.FeatureClassToFeatureClass_conversion('airports_layer', outputPath_2, 'airports_in_countries')
# # Get the list of countries that have "military" airports
with arcpy.da.SearchCursor(r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Airports\airports_in_countries.shp", ['NAME'])as Countries_cursor:
    for i in Countries_cursor:
        print(i[0])
#                           <----------------------------------------------------------------------------->
print('<----------------------------------------------------------------------------->')
## print countries
# set output shapefile path
outputPath_2_2 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Airports\Countries with Airports'


# Create a feature layer from the countries shapefile
arcpy.MakeFeatureLayer_management(countries, "countries_layer")

# # Create a feature layer from the airports shapefile with "military" type
arcpy.MakeFeatureLayer_management(airports, 'airports_layer', """ "type" = 'military' """)

# when country layer intersects with airport = countries that have military airports
arcpy.SelectLayerByLocation_management("countries_layer", "INTERSECT", 'airports_layer')
# # Create a new feature class of the selected countries using FeatureClassToFeatureClass_conversion
arcpy.FeatureClassToFeatureClass_conversion("countries_layer" , outputPath_2_2 , "military_countries" )
# # Get the list of countries that have "military" airports
with arcpy.da.SearchCursor(r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Airports\Countries with Airports\military_countries.shp", ['NAME'])as Countries_cursor:
    for i in Countries_cursor:
        print(i[0])






