import RPi.GPIO as GPIO
from gpiozero import LED
import time
from tkinter import*
import tkinter.font

Morse = {' ': ' ',"'": '.----.','(': '-.--.-',')': '-.--.-',',': '--..--',
        '-': '-....-','.': '.-.-.-','/': '-..-.','0': '-----','1': '.----',
        '2': '..---','3': '...--','4': '....-','5': '.....','6': '-....',
        '7': '--...','8': '---..','9': '----.',':': '---...',';': '-.-.-.',
        '?': '..--..','A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.',
        'F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-',
        'L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-',
        'R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--',
        'X': '-..-','Y': '-.--','Z': '--..','_': '..--.-'}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED = 18
GPIO.setup(LED,GPIO.OUT)

win = Tk()
win.title("Morse Code Blinker")
myFont = tkinter.font.Font(family = 'Times', size = 14, weight = "bold")

def dot():
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(0.5)

def dash():
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(0.5)
    
def Convert_Morse():
    input = INPUT.get()
    for letter in input:
        for symbol in Morse[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(2)
        time.sleep(2)

INPUT = Entry(win, font = myFont, width = 50, bg = 'white')
INPUT.grid(row = 0, column = 0)

LEDButton = Button(win, text = "Start", font = myFont, command= Convert_Morse, bg = 'white', height = 2, width = 50)
LEDButton.grid(row = 1, column = 0)