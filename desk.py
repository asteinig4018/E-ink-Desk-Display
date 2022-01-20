import os
import time

from datetime import datetime

from waveshare_epd import epd4in2

from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic' #pic directory

#initialize
try:
    # display init and clear
    display = epd4in2.EPD()
    display.init()
    display.Clear() #0: Black, 255: White

    h = display.height
    w = display.width

    print('width: ', w)
    print('height: ', h)
	
    ## Image Code ##
    #print('importing')
    time_font = ImageFont.truetype('RampartOne-Regular.ttf', 120, layout_engine=ImageFont.LAYOUT_BASIC)
    time_font2 = ImageFont.truetype('RampartOne-Regular.ttf', 32)
    #print("imported font")

    old_time = datetime.now().minute

    while(1):
        
        new_time = datetime.now().minute

        if new_time != old_time:
            image = Image.new(mode='1',size=(w,h), color=255)
            draw = ImageDraw.Draw(image)  

            now = datetime.now()

            time_now = now.strftime("%I:%M")

            time_pm = now.strftime("%p")

            draw.text((0,0), time_now, font=time_font, fill = 0, align='left')
        
            draw.text((345,105), time_pm, font=time_font2, fill=0, align='left') 

            #display.DisplayPartial(display.getbuffer(image))

            display.EPD_4IN2_PartialDisplay(0,0,400,150, display.getbuffer(image))

        
        old_time = new_time

        time.sleep(20)


except IOError as e:
    print(e)
