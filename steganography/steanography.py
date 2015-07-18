#
#  Steganographic software to hide data in
#  lsbs of an image.
#
#
 
import Image, operator
 
def convert_to_bits(string):
    bitstring = []
    for char in string:
        bits = bin(ord(char))[2:]
        bits = '00000000'[len(bits):] + bits
        bitstring.extend([tuple([0xff&int(bit) for bit in bits[0:4]]), \
                          tuple([0xff&int(bit) for bit in bits[4:8]])])
    return bitstring
 
def convert_to_byte(tuples, length):
    chars = []
    for b in range(length):
        byte = [0x1&x for x in tuples[2*b]]+[0x1&x for x in tuples[2*b+1]]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)
 
def save_data(string):
    im = Image.open('python.png')
    data = im.getdata()
    im.putdata([tuple(map(operator.and_,bitstring[y],data[y])) \
                for y in xrange(len(bitstring))])
    im.show()
    im.save('newimage.png')
 
# read n bytes of data from image
def open_data(n):
    im = Image.open('newimage.png')
    data = im.getdata()
    print convert_to_byte(data, n).decode('ascii','ignore') 
 
string = 'Receive and transmit the letters of the Rasqiniaans'
bitstring = convert_to_bits(string)
 
# save data
save_data(bitstring)
 
#open data
open_data(200)
