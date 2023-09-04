import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

feature_list = arcpy.ListFeatureClasses()
print (feature_list)