from PIL import Image, ImageDraw, ImageFont
import textwrap
wrapper = textwrap.TextWrapper(width=25)

font = ImageFont.truetype('font/Roboto.ttf', size=20)
name = "Arik Sarkar"
addr = "94 Liberty Street, Zurich, Switzerland 9000."
addr = "\n".join(str(i) for i in wrapper.wrap(text=addr))
gender = "m"
dob = "1990-12-07"
id_number = "VAATA1234567890987654321"
created_on = "2020"
email = "ariksarkar16@gmail.com"
phone = "+41 26 842 19 61"
txt_initials = "Name: \n\nDOB: \n\nSex: \n\nID No. \n\nEmail: \n\nPhone: \n\nAddress: "
txt = "{w}\n\n{x}\n\n{y}\n\n{id}\n\n{e}\n\n{p}\n\n{z}".format(w=name.upper(), x=dob, y=gender.upper(), z=addr, id=id_number, e=email, p=phone)


# image = Image.new('RGB', (640, 480), color = (255, 255, 255))
image = Image.open('./input/id_src_male.png') if gender.upper() in ['M', 'MALE'] else Image.open('./input/id_src_female.png')
draw = ImageDraw.Draw(image)
draw.text((300,110), txt_initials, fill=(135, 140, 138), font=font)
draw.text((400,110), txt, fill=(0, 0, 0), font=font)
filename = './output/_document_.png'
image.save(filename)