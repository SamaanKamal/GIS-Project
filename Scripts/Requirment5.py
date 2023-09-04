import arcpy
import re

# Set the workspace path
arcpy.env.workspace = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data"

# Set the (places,countries).shp paths
points = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_populated_places.shp"
countries = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Data\ne_10m_admin_0_countries.shp"

arcpy.env.overwriteOutput = True

#### 55555 (Two Methods , 3 types of solutions )
countries_files = ['Egypt', 'Saudi Arabia', 'Tunisia', 'Somalia', 'Algeria', 'Morocco',
                   'Iraq', 'Syria', 'Yemen', 'Libya', 'Jordan', 'United Arab Emirates',
                   'Lebanon','Mauritania', 'Kuwait', 'Oman', 'Qatar',
                   'Djibouti', 'Bahrain', 'Comoros', 'Palestine', 'Sudan', 'South Sudan']

countries_files_dic = {'Egypt': 'Egypt', 'Saudi Arabia': 'Saudi_Arabia', 'Tunisia': 'Tunisia', 'Somalia': 'Somalia', 'Algeria': 'Algeria', 'Morocco': 'Morocco',
                   'Iraq': 'Iraq', 'Syria': 'Syria', 'Yemen': 'Yemen', 'Libya': 'Libya', 'Jordan': 'Jordan', 'United Arab Emirates': 'United_Arab_Emirates',
                   'Lebanon': 'Lebanon','Mauritania': 'Mauritania', 'Kuwait': 'Kuwait', 'Oman': 'Oman', 'Qatar': 'Qatar',
                   'Djibouti': 'Djibouti', 'Bahrain': 'Bahrain', 'Comoros': 'Comoros', 'Palestine': 'Palestine', 'Sudan': 'Sudan', 'South Sudan': 'South_Sudan'}

# set output shapefile path
outputPath_5 = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Arabic Cities' # for normal solutions
outpathNormal = r'D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Arabic Cities Search' # for another solutions

#Method 1 first solution using if condition and countries_files list

### Normal solutions
# using Multiple selection
# Create a feature layer of the city based on the current city name
arcpy.MakeFeatureLayer_management(points, 'points_layer')
# Iterate over country names in 'countries_files'
for x in countries_files:
    # Create a feature layer of the country based on the current country name
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
    # Select the city features that are within the country boundary
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    # Create the output name for the new feature class
    output_name = 'Arabic_cities_in_{0}'.format(x.encode('utf-8'))
    # Replace special characters with underscores to ensure a valid output name
    output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
    # Export the selected city features to a new feature class
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpathNormal, output_name)
#
# #                           <----------------------------------------------------------------------------->
# # using IF condition
# # Create a feature layer of the city based on the current city name
# arcpy.MakeFeatureLayer_management(points, 'points_layer')
# # Iterate over country names in 'countries_files'
# with arcpy.da.SearchCursor(countries,['Name'])as countries_cursor:
#     for x in countries_cursor:
#         if x[0] in countries_files:
#             # Create a feature layer of the country based on the current country name
#             arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
#             # Select the city features that are within the country boundary
#             arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
#             # Create the output name for the new feature class
#             output_name = 'Arabic_cities_in_{0}'.format(x.encode('utf-8'))
#             # Replace special characters with underscores to ensure a valid output name
#             output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
#             # Export the selected city features to a new feature class
#             arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpathNormal, output_name)

#                           <----------------------------------------------------------------------------->

##Using Multiple Selection
arcpy.env.overwriteOutput = True
# Method 2 second solution using Multiple Selection and countries_files list
# 10 minute run O(N)

cities_dict = {}  # Dictionary to store city names per country

# for k in countries_files:
#     cities_dict[k.encode('utf-8')] = []
# # Iterate over country names in 'countries_files'
# for x in countries_files:
#     with arcpy.da.SearchCursor(points,['SOV0NAME','NAME']) as points_cursor:
#         for i in points_cursor:
#             # Check if the country name in the current record matches the current country name in 'countries_files'
#             if i[0] == x:
#                 # Add city names to the dictionary with country name as the key
#                 name = i[1].encode('utf-8')
#                 name = re.sub('[^0-9a-zA-Z_]+', '_', name)
#                 cities_dict[i[0].encode('utf-8')].append(name)
#
#
# # Create an empty list to store the paths of the individual shapefiles
# individual_shapefiles = []
#
# # Iterate over items in the cities dictionary
# for j in cities_dict.keys():
#     for k in cities_dict[j]:
#         point_name = k.encode('utf-8') # City name
#         sovereignt = j.encode('utf-8') # Country name
#         # Create a feature layer of the country based on the current country name
#         arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(sovereignt))
#         # Create a feature layer of the city based on the current city name
#         arcpy.MakeFeatureLayer_management(points, 'points_layer',""" 'NAME' ='{}'""".format(point_name))
#         # Select the city features that are within the country boundary
#         arcpy.SelectLayerByLocation_management('points_layer','WITHIN','countries_layer')
#         # Create the output name for the new feature class
#         output_name = '{0}_in_{1}'.format(point_name, j.encode('utf-8'))
#         # Replace special characters with underscores to ensure a valid output name
#         output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
#         # Export the selected city features to a new feature class
#         arcpy.FeatureClassToFeatureClass_conversion('points_layer', outputPath_5, output_name)
#
#         individual_shapefiles.append(outputPath_5 + '\\' + output_name+".shp")
#
# merged_shapefile = arcpy.CreateUniqueName("Arabic_cities_in_Arabic_countris.shp", r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\Output\Arabic Cities\Arabic cities in one shape file")
# # Merge the individual shapefiles into a single shapefile
# arcpy.Merge_management(individual_shapefiles, merged_shapefile)

#                           <----------------------------------------------------------------------------->

# Method 1 second solution using if condition and countries_files dictionary
# 8-9 minutes run O(N)
# with arcpy.da.SearchCursor(points,['SOV0NAME','NAME']) as points_cursor:
#     for x in points_cursor:
#         # Check if the country name in the current record matches a name in the 'countries_files' dictionary
#         if x[0] in countries_files_dic:
#             # Create a feature layer from the 'countries' feature class using SOVEREIGNT
#             arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(countries_files_dic[x[0].encode('utf-8')]))
#             point_name = x[1].encode('utf-8')
#             # Create a feature layer based on a condition using the 'NAME' field
#             arcpy.MakeFeatureLayer_management(points, 'points_layer',""" 'NAME' ='{}'""".format(point_name))
#             # Select features from 'points_layer' that are within 'countries_layer'
#             arcpy.SelectLayerByLocation_management('points_layer','WITHIN','countries_layer')
#             # Create the output name for the new feature class
#             output_name = '{0}_in_{1}'.format(point_name, x[0].encode('utf-8'))
#             # Replace special characters with underscores to ensure a valid output name
#             output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
#             # Export the selected features from 'points_layer' to a new feature class
#             arcpy.FeatureClassToFeatureClass_conversion('points_layer', outputPath_5, output_name)

#                           <----------------------------------------------------------------------------->

### 50 minutes run O(N^2)
# # Create a feature layer from the 'countries' feature class
# arcpy.MakeFeatureLayer_management(countries,'countries_layer')
# # Iterate over records in the 'points' feature class
# with arcpy.da.SearchCursor(points,['SOV0NAME','NAME']) as points_cursor:
#     for x in points_cursor:
#         i=0
#         while i < 23:
#             # Check if the country name in the current record matches a name in the 'countries_files' list
#             if x[0] == countries_files[i]:
#                 # Create a feature layer based on a condition using the 'NAME' field
#                 arcpy.MakeFeatureLayer_management(points, 'points_layer',""" 'NAME' ='{}'""".format(x[1].encode('utf-8')))
#                 # Select features from 'points_layer' that are within 'countries_layer'
#                 arcpy.SelectLayerByLocation_management('points_layer','WITHIN','countries_layer')
#                 # Create the output name for the new feature class
#                 output_name = '{0}_in_{1}'.format(x[1].encode('utf-8'),x[0].encode('utf-8'))
#                 # Replace special characters with underscores to ensure a valid output name
#                 output_name = re.sub('[^0-9a-zA-Z_]+', '_', output_name)
#                 # Export the selected features from 'points_layer' to a new feature class
#                 arcpy.FeatureClassToFeatureClass_conversion('points_layer',outputPath_5,output_name)
#             i = i + 1

