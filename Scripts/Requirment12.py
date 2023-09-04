import arcpy

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

points = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_populated_places.shp"

arcpy.env.overwriteOutput = True

#### 12
fields = arcpy.ListFields(points)
field_list = []
for i in fields:
    if not i.type == 'String':
        field_list.append(i.name)

for field in field_list:
    with arcpy.da.UpdateCursor(points,[field]) as city_cursor:
        for x in city_cursor:
            if x[0] == ' ' or x[0] is None or x[0] == 0:
                name = field  # Field name
                x[0] = 8
                city_cursor.updateRow(x)
                print 'Value of field {}  is updated to {}'.format(name, x[0])
                print('DONE')

#                           <----------------------------------------------------------------------------->
# # another Solution
# fields = arcpy.ListFields(points) # Get a list of fields in the 'points' feature class
#
# NonStringEmptyFileds = {}  # Dictionary to store non-string field names
# numberOfNonStringFileds = 0  # Counter for non-string field names
#
# # Iterate over the fields
# for field in fields:
#     # Check if the field type is not 'String'
#     if field.type != 'String':
#         # Add the field name to the dictionary with an index as the key
#         NonStringEmptyFileds[numberOfNonStringFileds] = field.name.encode('utf-8')
#         numberOfNonStringFileds += 1
#
# # Iterate over the non-string field names
# for i in range(numberOfNonStringFileds):
#     # Update the values of the field
#     with arcpy.da.UpdateCursor(points,[NonStringEmptyFileds[i]]) as fields_cursor:
#         for x in fields_cursor:
#             # Check if the value is empty or zero
#             if not x[0] or x[0] == 0:
#                 name = NonStringEmptyFileds[i]  # Field name
#                 x[0] = 7  # Update the value to 7
#                 fields_cursor.updateRow(x) # Update the row with the new value
#                 print 'Value of field {}  is updated to {}'.format(name, x[0])

