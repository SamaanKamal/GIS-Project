import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

# Set the (places).shp paths
points = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_populated_places.shp"

arcpy.env.overwriteOutput = True
# ##### 11
# Iterate over fields in the 'points' feature class
for field in arcpy.ListFields(points):
    # Print the name and type of each field
    print("Field name: {0}, Type: {1}".format(field.name, field.type))