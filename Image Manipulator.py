from tkinter.filedialog import Open
from PIL import Image, ImageFilter
import os, sys
import subprocess
im_list = """
 Please type the name of the image: 
 [1] Anteater 
 [2] Bear 
 [3] Bunny 
 [4] Chimp 
 [5] Gorilla 
 [6] Lamb 
 [7] Monkey 
 [8] Orangutan 
 [9] Quokka 
 [10] Spider
"""
#rotates images based off user input
def rotate():
    print(im_list)
    while True:
        #tests if the inputs will work
        try:
            #user input to determine what image to rotate and how many degrees
            image = input("Which image do you want to rotate: " ).lower()
            num = int(input("How many degrees: "))
            im = Image.open(image + ".jpg")
            im.rotate(num).show()
            #saves the rotated image into the rotation folder
            fn,fext = os.path.splitext(image)
            im.rotate(num).save('ROTATE/{}.png'.format(fn))
            print("Saved into ROTATE folder")          
            break
        #executes if user inputs an invalid value to rotate
        except ValueError:
            print("That number does not work.")
        #executes if user inputs a picture that does not exist
        except FileNotFoundError:
            print("That picture does not exist.")
#turns images black and white
def black_white():
    print(im_list)
    while True:
        #tests if input will work
        try:
            #user determines what image to turn black and white
            image = input("Which image do you want to make black and white: ").lower()
            im = Image.open(image + ".jpg")
            im.convert("L").show()
            #saves image to blacks folder
            fn,fext = os.path.splitext(image)
            im.convert("L").save('BLACKS/{}.png'.format(fn))   
            print("Saved into BLACKS folder") 
            break
        #executes if the user input a picture that does not exist
        except FileNotFoundError:
            print("That picture does not exist.")
#blurs images based of user input
def blur():
    print(im_list)
    while True:
        #tests if inputs will work
        try:
            #blurs images based off user input
            image = input("Which image do you want to blur: ").lower()
            num = int(input("How much do you want to blur it: "))
            im = Image.open(image + ".jpg")
            im.filter(ImageFilter.GaussianBlur(num)).show()
            #saves blurred images into blurs folder
            fn,fext = os.path.splitext(image)
            im.filter(ImageFilter.GaussianBlur(num)).save('BLURS/{}.png'.format(fn))
            print("Saved into BLURS folder")
            break
        #executes if user inputs an invalid blur input
        except ValueError:
            print("Invalid Number.")
        #executes if user inputs a picture that does not exist
        except FileNotFoundError:
            print("That picture does not exist.")
#turns images into thumbnails based off user input
def thumbnail():
    print(im_list)
    #preset image dimensions
    size1 = (200,200)
    size2 = (400,400)
    size3 = (600,600)
    while True:
        #tests input to see if it would work
        try: 
            #user inputs for size and image
            image = input("Which image do you want to make into a thumbnail: ").lower()
            size = input("Select the size: [1] (300,300), [2] (400,400), [3] (600,600): ")
            #executes if user selects size 1
            if size == "1":
                im = Image.open(image + ".jpg")
                im.thumbnail(size1)
                im.show()
                fn,fext = os.path.splitext(image)
                im.save('THUMBNAIL(200,200)/{}.jpg'.format(fn))
                print("Saved into THUMBNAIL(200,200) folder")
                break
            #executes if user selects size 2
            elif size == "2":
                im = Image.open(image + ".jpg")
                im.thumbnail(size2)
                im.show()
                fn,fext = os.path.splitext(image)
                im.save('THUMBNAIL(400,400)/{}.jpg'.format(fn))
                print("Saved into THUMBNAIL(400,400) folder")
                break
            #executes if user selects size 3
            elif size == "3":
                im = Image.open(image + ".jpg")
                im.thumbnail(size3)
                im.show()
                fn,fext = os.path.splitext(image)
                im.save('THUMBNAIL(600,600)/{}.jpg'.format(fn))
                print("Saved into THUMBNAIL(600,600) folder")
                break
            else:
                print("Invalid number.")
        #executes if the user inputs a picture that does not exist
        except FileNotFoundError:
            print("That picture does not exist.")
#applies a median filter to images based off user input
def Mfilter():
    print(im_list)
    while True:
        #tests if user input will be invalid 
        try:
            #user inputs for image and size of filter 
            image = input("Which image do you want apply a mode filter to: ").lower()
            size = int(input("Size: "))
            im = Image.open(image + ".jpg")
            im.filter(ImageFilter.ModeFilter(size)).show()
            #saves image into filters folder
            fn,fext = os.path.splitext(image)
            im.filter(ImageFilter.ModeFilter(size)).save('FILTERS/{}.png'.format(fn))
            print("Saved into FILTERS folder")
            break
        #executes if user inputs an invalid blur number
        except ValueError:
            print("Invlaid number.")
        #executes if user inputs a picture that does not exist
        except FileNotFoundError:
            print("That picture does not exist.")
#converts jpg images into pngs
def png():
    print(im_list)
    while True:
        #tests if user input will work
        try:
            #user inputs what image he wants to convert
            image = input("Which image do you want to save as a png: ").lower()
            image = image + ".jpg"
            i = Image.open(image)
            fn,fext = os.path.splitext(image)
            i.save('PNGS/{}.png'.format(fn))
            print("Saved into PNGS folder")
            break
        #executes if user inputs a picture that does not exist
        except FileNotFoundError:
            print("That file does not exist.")         
#opens default images to view them
def open_im():
    print(im_list)
    while True:
        try:
            image = input("Which image do you want to view: ")
            im = Image.open(image + ".jpg")
            im.show()
            break
        except FileNotFoundError:
            print("That picture does not exist.")
#utilizes the subprocess module to open the specific file location for based off user input
def open_edited():
    while True:
        choice = input("""
        Which file do you want to open 
        [1] Blacks 
        [2] Blurs 
        [3] Filters 
        [4] PNGS 
        [5] Rotate 
        [6] Thumbanail(200,200) 
        [7] Thumbnail(400,400) 
        [8] Thumbnail(600,600)
        """)
        #each instance and file location for the different kinds of edited images
        if choice == "1":
            process = subprocess.Popen(r'explorer /select,"BLACKS\BLACKS.txt"')
            break
        elif choice == "2":
            process = subprocess.Popen(r'explorer /select,"BLURS\BLURS.txt"')
            break
        elif choice == "3":
            process = subprocess.Popen(r'explorer /select,"FILTERS\FILTERS.txt"')
            break
        elif choice == "4":
            process = subprocess.Popen(r'explorer /select,"PNGS\PNGS.txt"')
            break
        elif choice == "5":
            process = subprocess.Popen(r'explorer /select,"ROTATE\ROTATE.txt"')
            break
        elif choice == "6":
            process = subprocess.Popen(r'explorer /select,"THUMBNAIL(200,200)\THUMBNAIL(200,200).txt"')
            break
        elif choice == "7":
            process = subprocess.Popen(r'explorer /select,"THUMBNAIL(400,400)\THUMBNAIL(400,400).txt"')
            break
        elif choice == "8":
            process = subprocess.Popen(r'explorer /select,"THUMBNAIL(600,600)\THUMBNAIL(600,600).txt"')
            break
        #executes if user inputs an invalid input and loops back
        else:
            print("Invalid input.")
    
#constantly loops back here after user completes editing an image
#takes input from user to select the editing mode
while True:
    mode = input("Please select a mode: rotate [1], black and white [2], blur [3], thumbnail [4], mode filter [5], PNG converter [6], Image view [7], Edited image view [8] or Q to quit: ")
    if mode == "1":
        rotate()
    elif mode == "2":
        black_white()
    elif mode == "3":
        blur()
    elif mode == "4":
        thumbnail()
    elif mode == "5":
        Mfilter()
    elif mode == "6":
        png()
    elif mode == "7":
        open_im()
    elif mode == "8":
        open_edited()
    elif mode == "Q" or mode == "q":
        exit()
    else:
        print("Invalid Input.")