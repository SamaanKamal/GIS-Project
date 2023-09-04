import arcpy
import re
# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

roads = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_roads.shp"
countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"
outputPath_7 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Roads in_name_income'

arcpy.env.overwriteOutput = True

# Create a feature layer for the roads dataset
arcpy.MakeFeatureLayer_management(roads, "roads_layer")

with arcpy.da.SearchCursor(countries,['FID','NAME','SOVEREIGNT','POP_EST','CONTINENT','INCOME_GRP']) as countries_cusror:
    for x in countries_cusror:
        if x[3] > 25000000 and x[4] == 'Africa':
            arcpy.MakeFeatureLayer_management(countries, "countries_layer",""" "FID" = {} AND SOVEREIGNT = '{}' """.format(x[0],x[2]))
            arcpy.SelectLayerByLocation_management("roads_layer", "WITHIN", "countries_layer")
            output_name = "Roads_in_{0}_{1}".format(x[1].encode('utf-8'), x[5].encode('utf-8'))
            output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)

            arcpy.FeatureClassToFeatureClass_conversion("roads_layer", outputPath_7,output_name)