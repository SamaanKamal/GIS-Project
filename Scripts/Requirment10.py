import arcpy

arcpy.env.overwriteOutput = True
###10101010
countries = arcpy.GetParameterAsText(0)
newPopulation = arcpy.GetParameterAsText(1)
#countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"

# Create a search cursor for the ports dataset and iterate through the rows
with arcpy.da.UpdateCursor(countries, ['POP_YEAR', 'POP_EST','Name']) as port_cursor:
    for x in port_cursor:
        # Check if the website field is empty
        if x[0] < 2019:
            # Update the website field with the new website value
            x[1] = newPopulation
            port_cursor.updateRow(x)
            # Print the name of the country that was updated
            arcpy.AddMessage("Population Est updated for: " + x[2].encode('utf-8'))
            print("Population Est updated for: " + x[2].encode('utf-8'))
        else:
            arcpy.AddMessage("Population year for {} country is not less than 2019 and was not updated".format(x[2].encode('utf-8')))

# Add a log message to indicate completion of script
arcpy.AddMessage("Population data update completed.")