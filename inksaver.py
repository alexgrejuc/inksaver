# inksaver - "hollows out" text and removes large chunks of edge artifacts on a scanned page/image

from PIL import ImageColor;
from PIL import Image;

def is_black(img, x, y):
    r,g,b,a = pixel_color = img.getpixel((x,y));
    
    if((r == 0 and g == 0 and b == 0) or a == 0):
        return True; 
    else:
        return False;

#searches around a pixel to determine if it can be changed to white
#a pixel is not removable if it has white space around it 
#for example, text is black, but is usually surrounded by white space 
#so the edges of a latter should not be removed
def is_removeable(img, x, y):
    total = 0;

    #scans around spot and counts surrounding black pixels 
    for i in range(-1, 1):
        for j in range(-1, 1):
            if(is_black(img, x + i, y + j)):
                    total+=1;
    if(total >= 4):
        return True;
    else:
        return False;

def main():
    img = Image.open('page.png');
     
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            if is_black(img, x, y):
                if(is_removeable(img, x, y)):    
                    img.putpixel((x,y), (0,0,0,0)) 
    img.save('new_page.png');

main();
