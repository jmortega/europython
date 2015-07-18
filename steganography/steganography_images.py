import sys
import Image,ImageOps

def extract_image(from_image,s=4):
	data = Image.open(from_image)
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p = data.getpixel((x,y))
			red = (p[0] % s) * 255 /s
			green = (p[0] % s) * 255 /s
			blue = (p[0] % s) * 255 /s
			data.putpixel((x,y),(red,green,blue))
	data.save("extracted.png")
	return data
	
def hide_image(public_image,secret_image,s=4):
	data = Image.open(public_image)
	key = ImageOps.autocontrast(Image.open(secret_image).resize(data.size))
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p = data.getpixel((x,y))
			q = key.getpixel((x,y))
			red = p[0] - (p[0] % s) + (s * q[0] / 255)
			green = p[1] - (p[1] % s) + (s * q[1] / 255)
			blue = p[2] - (p[2] % s) + (s * q[2] / 255)
			data.putpixel((x,y),(red,green,blue))
	data.save("python-secret.png")		
	return data
	
	
	
hide_image("python.png","secret.png");

extract_image("python-secret.png");
