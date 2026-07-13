import qrcode

# text = input("Enter the text to convert into qrcode: ")

# filename = input("Enter the filename to save the qrcode: ")

def generate_qrcode(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()       
    text = lines[0].strip()
    filename = lines[1].strip()
    
    image_qrcode = qrcode.make(text)
    image_qrcode.save(filename)
    
generate_qrcode("input.txt") 

