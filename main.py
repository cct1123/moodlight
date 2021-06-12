
# from https://stackoverflow.com/questions/50310613/how-to-capture-screen-using-python-with-better-frame-rate
import numpy as np
import cv2
import glob
from moviepy.editor import VideoFileClip
from mss import mss
from PIL import Image
import time

color = (0, 255, 0) # bounding box color.

# This defines the area on the screen.
mon = {'top' : 0, 'left' : 0, 'width' : 1920, 'height' : 1080}
sct = mss()
previous_time = 0
while True :
    sct.get_pixels(mon)
    frame = Image.frombytes( 'RGB', (sct.width, sct.height), sct.image )
    frame = np.array(frame)
    # image = image[ ::2, ::2, : ] # can be used to downgrade the input
    frame = cv2.resize(frame, dsize=(int(sct.width/4), int(sct.height/4)), interpolation=cv2.INTER_NEAREST)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow ('frame', frame)
    if cv2.waitKey ( 1 ) & 0xff == ord( 'q' ) :
        cv2.destroyAllWindows()
        break
    txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
    previous_time = time.time()
    print(txt1)

