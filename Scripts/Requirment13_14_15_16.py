import arcpy
from PIL import Image, ExifTags
import os

##### 13 14 15 16
img_folder = r"D:\fcis\8th semster\Geographic Information System-GIS\Labs\Project\PicturesData"
img_content = os.listdir(img_folder)

# Iterate over the images in the folder
for image in img_content:

    full_path = os.path.join(img_folder, image)  # Get the full path of the image
    print("\nFull path: "+full_path)
    img = Image.open(full_path)  # Open the image using PIL 13

    try:
        # Extract the EXIF data from the image
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
        print("Exif Tags =>")
        if(exif['GPSInfo']):
            print(exif)


            gps_all = {}#14

            # Extract GPS information from the EXIF data
            for key in exif['GPSInfo'].keys():
                decoded_value = ExifTags.GPSTAGS.get(key)
                gps_all[decoded_value] = exif['GPSInfo'][key]

            long_ref = gps_all.get('GPSLongitudeRef')  # Get the longitude reference
            lat_ref = gps_all.get('GPSLatitudeRef')  # Get the latitude reference

            longitude = gps_all.get('GPSLongitude')  # Get the longitude value
            latitude = gps_all.get('GPSLatitude')  # Get the latitude value
            print("Latitude and Longitude =>")
            print(long_ref)
            print(lat_ref)

            print(longitude)
            print(latitude)
    except:
        print("This image is not a GeoTagged image")