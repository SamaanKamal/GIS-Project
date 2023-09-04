import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

# Set the (countries,ports).shp paths
ports = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_ports.shp"
countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"

arcpy.env.overwriteOutput = True

#### 4444 using two methods(Multiple selection, Multiple Query in 1 shape file)
# set output shapefile path
outputPath_4 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Ports'
# method 1 Multiple Selection

# set a list of countries to select from
countries_for_ports = ['Italy','Spain' ,'France']

# Create a feature layer of ports
arcpy.MakeFeatureLayer_management(ports,"ports_layer")


for x in countries_for_ports:
#   # Create a feature layer for the three countries
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))

#   Use Select Layer By Location to select countries that are completely within ports
    arcpy.SelectLayerByLocation_management("ports_layer", "WITHIN", "countries_layer")

#   Create a new feature class of the selected countries with ports using FeatureClassToFeatureClass_conversion
    arcpy.FeatureClassToFeatureClass_conversion("ports_layer",outputPath_4, "Ports_in_{}".format(x))


#                           <----------------------------------------------------------------------------->
# method 2 Multiple Query in 1 shape file


# # Create a feature layer of ports
# arcpy.MakeFeatureLayer_management(ports,"ports_layer")

# # Create a feature layer for the three countries
# arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" IN('Italy', 'Spain', 'France') """)

# #   Use Select Layer By Location to select countries that are completely within ports
# arcpy.SelectLayerByLocation_management("ports_layer", "WITHIN", "countries_layer")

# Create a new shapefile of selected ports in the three countries
# arcpy.FeatureClassToFeatureClass_conversion("ports_layer",outputPath_4, "Ports_in_Italy_Spain_France")

