"""
please install:
  pip install pillow
  pip install qrcode
"""

import os
import qrcode
from PIL import Image,ImageDraw,ImageFont

def create_id(): 
    try:         
        # data needed for the id
        muni_city = "QUEZON CITY"
        province = "METRO MANILA"
        VIN = "0809-0121B-L3189JTD10000"
        last_name = "DELA CRUZ"
        first_name = "JUAN"
        middle_name = "TAMAD"
        dob = "January 31, 1989"
        civil_stat = "Single"
        citizenship = "Filipino"
        address1 = "SAINT MARY ST., E. RODRIGUEZ,"
        address2 = "QUEZON CITY,"
        address3 = "METRO MANILA"
        precinct_num = '0121B'
        
        # move one level directory
        path = os.path.abspath('..')
        #print(path)
        
        # open id template
        img_id = Image.open(path+'\\default\\template\\id_template.png')
        
        # generate qrs for vin and name
        name = last_name+', '+first_name+', '+middle_name
        gen_qr_vin(VIN)
        gen_qr_name(VIN,name)
        
        # insert qr of vin into the template
        img_qr_vin = Image.open(path+"\\data\\qrs\\vin\\"+VIN+".png")  
        img_qr_vin = img_qr_vin.resize((1100, 1100), Image.ANTIALIAS)
        img_id.paste(img_qr_vin, (3750, 600))
        
        # insert qr of name into the template
        img_qr_name = Image.open(path+"\\data\\qrs\\Name\\"+VIN+".png")  
        img_qr_name = img_qr_name.resize((1100, 1100), Image.ANTIALIAS)
        img_id.paste(img_qr_name, (3750, 1800))
        
        # insert user picture into the template
        img_user = Image.open(path+"\\data\\photos\\"+VIN+".png")  
        img_user = img_user.resize((1200, 1400), Image.ANTIALIAS)
        img_id.paste(img_user, (250, 1200), img_user)
        
        # configure font type - family and size
        font_type_comelec = ImageFont.truetype("ariblk.ttf", 100)
        font_type_name = ImageFont.truetype("ariblk.ttf", 90)
        font_type_label = ImageFont.truetype("arial.ttf", 90)
        font_type_content = ImageFont.truetype("arial.ttf", 80)
        font_type_sign = ImageFont.truetype("arial.ttf", 90)
        font_type = ImageFont.truetype("arial.ttf", 100)
        
        draw_img = ImageDraw.Draw(img_id)
        
        # write id header - comelec and logo
        img_logo = Image.open(path+"\\default\\template\\logo.png")  
        img_logo = img_logo.resize((820, 820), Image.ANTIALIAS)
        img_id.paste(img_logo, (480, 172), img_logo)
        draw_img.text(xy=(1900, 250), text= "Republic of the Philippines", fill =(0,0,0), font = font_type)
        draw_img.text(xy=(1690, 350), text= "COMMISSION ON ELECTIONS", fill =(0,0,0), font = font_type_comelec)
        
        # write id header - region
        field_office = muni_city+', '+province
        draw_img.text(xy=(1900, 500), text= field_office.upper(), fill =(0,0,0), font = font_type_content)
        
        # write id header - vin
        lvin = 'VIN: '+VIN.upper()
        draw_img.text(xy=(1700, 650), text= lvin, fill =(0,0,0), font = font_type)
        
        # write signatory into the template
        draw_img.text(xy=(2060, 2880), text= "SHERIFF M. ABAS", fill =(0,0,0), font = font_type)
        draw_img.text(xy=(2250, 2980), text= "Chairman", fill =(0,0,0), font = font_type_sign)
        
        # insert chairman sign into the template
        img_sign = Image.open(path+"\\default\\template\\chair_sign.png")  
        img_sign = img_sign.resize((1200, 400), Image.ANTIALIAS)
        img_id.paste(img_sign, (1800, 2500), img_sign)
        
        # write id labels into the template
        draw_img.text(xy=(1600, 1300), text= "Date of Birth", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(2150, 1300), text= ":", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(1600, 1450), text= "Civil Status", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(2150, 1450), text= ":", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(1600, 1600), text= "Citizenship", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(2150, 1600), text= ":", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(1600, 1750), text= "Address", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(2150, 1750), text= ":", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(1600, 2350), text= "Precinct No.", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(2150, 2350), text= ":", fill =(0,0,0), font = font_type_label)
        draw_img.text(xy=(455, 2980), text= "Signature of Voter", fill =(0,0,0), font = font_type_sign)
        
        # write user data into the template - name
        draw_img.text(xy=(1600, 900), text= last_name.upper(), fill =(0,0,0), font = font_type_name)
        draw_img.text(xy=(1600, 1000), text= first_name.upper(), fill =(0,0,0), font = font_type_name)
        draw_img.text(xy=(1600, 1100), text= middle_name.upper(), fill =(0,0,0), font = font_type_name)
        
        # write user data into the template - other details
        draw_img.text(xy=(2300, 1300), text= dob, fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(2300, 1450), text= civil_stat, fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(2300, 1600), text= citizenship, fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(1700, 1900), text= address1.upper(), fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(1700, 2050), text= address2.upper(), fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(1700, 2200), text= address3.upper(), fill =(0,0,0), font = font_type_content)
        draw_img.text(xy=(2300, 2350), text= precinct_num, fill =(0,0,0), font = font_type_content)
        
        # insert user signature into the template
        img_user_sign = Image.open(path+"\\data\\signs\\"+VIN+".png")  
        img_user_sign = img_user_sign.resize((1200, 400), Image.ANTIALIAS)
        img_id.paste(img_user_sign, (255, 2650), img_user_sign)
        
        # save new template
        img_id.save(path+'\\data\\ids\\'+VIN+'.png')
        img_id.show()
    except IOError: 
        pass

def gen_qr_vin(VIN):
    path = os.path.abspath('..')
    qr = qrcode.QRCode(
        version = 13,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 20,
        border = 0,
    )
    qr.add_data(VIN)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(path+'\\data\\qrs\\vin\\'+VIN+'.png')

def gen_qr_name(VIN,name):
    path = os.path.abspath('..')
    qr = qrcode.QRCode(
        version = 13,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 20,
        border = 0,
    )
    qr.add_data(name)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(path+'\\data\\qrs\\name\\'+VIN+'.png')
    
if __name__ == "__main__": 
    create_id()

