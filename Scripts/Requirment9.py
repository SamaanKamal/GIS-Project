import arcpy

arcpy.env.overwriteOutput = True
#### 99999
# Define the input parameters for the tool
ports = arcpy.GetParameterAsText(0)
new_website = arcpy.GetParameterAsText(1)


# Create a search cursor for the ports dataset and iterate through the rows
with arcpy.da.UpdateCursor(ports, ['name', 'website']) as port_cursor:
    for x in port_cursor:
        # Check if the website field is empty
        if not x[1].strip():
            # Update the website field with the new website value
            x[1] = new_website
            port_cursor.updateRow(x)
            arcpy.AddMessage("Website for {} port has been updated to {}".format(x[0], new_website))
        else:
            arcpy.AddMessage("Website for {} port is not empty and was not updated".format(x[0]))

# Print a message to indicate the process has completed successfully
arcpy.AddMessage("All empty port websites have been updated.")
