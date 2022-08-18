import pyautogui as pg
import time

time.sleep(1)
txt=open('animals.txt' ,'r')
text=input("enter name hear : ")
print("open text area and tap there after execution of code...")
print("To stope pause the running in your text editor or close the editor...")
for i in txt:
        pg.write(text+ ' is a' +' ' +i)
        pg.press('Enter')
        
    

    

