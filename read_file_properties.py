import pyexiv2


def get_image_properties(path):
    img = pyexiv2.Image('data/Manticore.jpg')
    data = img.read_exif()
    img.close()
    return data['Exif.Image.XPComment']
    
#print(data['Exif.Image.XPComment'])