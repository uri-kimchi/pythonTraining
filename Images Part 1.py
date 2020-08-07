from PIL import Image

dir_name = '/home/urik/Python38/Complete-Python-3-Bootcamp-master/14-Working-with-Images/'
file_name = 'example.jpg'

img = Image.open(dir_name+file_name)
#img.show()
img.save('/home/urik/Desktop/original.jpg')
print (type(img), img.filename , img.format_description)
out = img.transpose(Image.ROTATE_90)
out.save('/home/urik/Desktop/transpose.jpg')
crop = img.crop((10,10,20,20))
crop.save('/home/urik/Desktop/crop.jpg')
