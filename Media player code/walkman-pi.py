import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
b1=b2=b3=b4=0
m=x=2
p=2
os.system("mocp -S")
os.system("mocp -c")
os.system("mocp -a /media/")
os.system("mocp -p")
os.system("mocp -P")
os.system("aplay /home/pi/Downloads/beep-07.wav")
fs=1000
fs2='4'
while True:
        if(GPIO.input(18) ==1):
                b1=b1+1
                m=1
#		print(b1)
        if(GPIO.input(23) ==1):
                b2=b2+1
                m=1
#		print(b2)
        if(GPIO.input(24) ==1):
                b3=b3+1
                m=1
#		print(b3)
        if(GPIO.input(25) ==1):
                b4=b4+1
                m=1
#		print(b4)
        if(m ==0):
                if(b1>1 and b1<6001):
                        os.system("aplay /home/pi/Downloads/beep-07.wav")
                        os.system("amixer -q sset PCM 500+")
 
                if(b2>1 and b2<6001):
                        os.system("amixer -q sset PCM 500-")
 
                if(b3>1 and b3<6001):
                        os.system("mocp -f")
 
                if(b4>1 and b4<6001):
                        os.system("mocp -G")
                b1=b2=b3=b4=0
		p=0
        if(m==1):
                if(b1>6000):
                        if(x==fs):
                                os.system("mocp -k "+fs2)
                if(b2>6000):
                        if(x==fs):
                                os.system("mocp -k -"+fs2)
                if(b3>6000 and p==0):
			p=1
                        os.system("mocp -r")
                        os.system("aplay /home/pi/Downloads/beep-07.wav")
		if(b4>6000):
			os.system("aplay /home/pi/Downloads/beep-07.wav")
			os.system("mocp -p")
        m=0
        if(x==fs):
                x=0
        x=x+1
os.system("mocp -x")
GPIO.cleanup()