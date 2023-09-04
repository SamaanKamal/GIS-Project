import arcpy
import re

arcpy.env.overwriteOutput = True
# Define the input parameters for the tool
roads = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
outputPath_7 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Roads in_name_income'

# Create a feature layer for the roads dataset
arcpy.MakeFeatureLayer_management(roads, "roads_layer")

with arcpy.da.SearchCursor(countries,['FID','NAME','SOVEREIGNT','POP_EST','REGION_UN','INCOME_GRP']) as countries_cusror:
    for x in countries_cusror:
        # Check if the country is in Africa and has a population greater than 25 million
        if x[3] > 25000000 and x[4] == 'Africa':
            # Create a feature layer for the countries dataset based on the FID and Sovereignty fields
            arcpy.MakeFeatureLayer_management(countries, "countries_layer",""" "FID" = {} AND SOVEREIGNT = '{}' """.format(x[0],x[2]))
            arcpy.SelectLayerByLocation_management("roads_layer", "WITHIN", "countries_layer")
            output_name = "Roads_in_{0}_{1}".format(x[1].encode('utf-8'), x[5].encode('utf-8'))
            output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
            # Copy the selected features to a new shapefile
            arcpy.FeatureClassToFeatureClass_conversion("roads_layer", outputPath_7,output_name)
            # Log the process
            arcpy.AddMessage("Successfully created shapefile for roads in {0}".format(x[1].encode('utf-8')))
        else:
            # Log that the country was skipped
            arcpy.AddMessage("Skipped {0} because it does not meet the population or region criteria".format(x[1].encode('utf-8')))

    # Log that the process is complete
    arcpy.AddMessage("Finished creating shapefiles for roads in Africa with population greater than 25 million")

