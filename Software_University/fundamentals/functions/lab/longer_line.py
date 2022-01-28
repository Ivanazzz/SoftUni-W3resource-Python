import math

def function():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())
    
    line1_to_center = math.sqrt((x1 ** 2) + (y1 ** 2))
    line2_to_center = math.sqrt((x2 ** 2) + (y2 ** 2))
    line3_to_center = math.sqrt((x3 ** 2) + (y3 ** 2))
    line4_to_center = math.sqrt((x4 ** 2) + (y4 ** 2))
    
    line1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    line2 = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
    
    if line2 > line1:
        if line3_to_center > line4_to_center:
           print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")
        else:
            print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
    else:
        if line1_to_center > line2_to_center:
           print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
        else:
            print(f"({math.floor(x1)},{math.floor(y1)})({math.floor(x2)},{math.floor(y2)})")
        
function()