import customtkinter
from threading import *
import pyautogui
import keyboard
import pydirectinput
import PIL
from licensing.models import *
from licensing.methods import Key, Helpers
#Import needed libraries

# Disable print commands for optimization
# sys.stdout = open(os.devnull, 'w')

def setglobals():
    global gutcounter
    global programclose
    global totalCatches
    global processStatus
    global failsafe
    global timesincelastaction

    global fishstop
    global traderstop
    global recyclerstop
    global softsidestop
    global antiafkstop

def resetGlobals():
    global gutcounter
    global programclose
    global totalCatches
    global processStatus
    global failsafe
    global timesincelastaction

    global fishstop
    global traderstop
    global recyclerstop
    global softsidestop
    global antiafkstop

    fishstop = False
    gutcounter = 0
    failsafe = 0
    totalCatches = 0
    processStatus = "Waiting to start"
    programclose = False

def foodcheck():
    global processStatus
    image = PIL.ImageGrab.grab()  # Define an area to capture.
    rgbwater = image.getpixel((1770,990))  # What pixel do we want?
    rgbfood = image.getpixel((1770,1032))  # What pixel do we want?
    processStatus = "Hungry, looking for pumpkins..."

    print(rgbwater[2])
    print(rgbfood[0])

    keyboard.press("tab")
    time.sleep(0.3)
    keyboard.release("tab")
    time.sleep(0.3)
    pumpkin = pyautogui.locateCenterOnScreen("Images/pumpkin.png", confidence=0.7, grayscale=True)
    rgbwater = image.getpixel((1770, 990))  # What pixel do we want?
    rgbfood = image.getpixel((1770, 1032))  # What pixel do we want?

    print(pumpkin)

    if str(pumpkin) != "None":
        processStatus = "Pumpkins found, eating..."
        pyautogui.leftClick(pumpkin)
        time.sleep(0.5)
        while rgbwater[2] < 180 or rgbfood[0] < 180:
            image = PIL.ImageGrab.grab()  # Define an area to capture.
            rgbwater = image.getpixel((1770, 990))  # What pixel do we want?
            rgbfood = image.getpixel((1770, 1032))  # What pixel do we want?
            print(rgbwater[2])
            print(rgbfood[0])

            eat = pyautogui.locateCenterOnScreen("Images/eat.png", confidence=0.7, grayscale=True)
            pyautogui.leftClick(eat)
            time.sleep(0.7)
            print("eat")
        print("Satisfactory food bar")
    else:
        print("No pumpkins found in inventory, skipping.")



    keyboard.press("esc")
    time.sleep(0.3)
    keyboard.release("esc")

    time.sleep(2)

def deathcheck():
    respawn = pyautogui.locateCenterOnScreen("Images/respawn.png", confidence=0.7, grayscale=True)
    if str(respawn) != "None":
        print("You died")
        time.sleep(1)
        respawn = pyautogui.locateCenterOnScreen("Images/respawn.png", confidence=0.7, grayscale=True)
        pydirectinput.keyDown("alt")
        time.sleep(0.1)
        pydirectinput.keyDown("f4")
        time.sleep(0.5)
        pydirectinput.keyUp("alt")
        time.sleep(0.1)
        pydirectinput.keyUp("f4")

    print("It appears you are alive")
    time.sleep(1)

def respawn():
    respawn = pyautogui.locateCenterOnScreen("Images/respawn.png", confidence=0.7, grayscale=True)
    if str(respawn) != "None":
        print("You died")
        time.sleep(1)
        respawn = pyautogui.locateCenterOnScreen("Images/respawn.png", confidence=0.7, grayscale=True)
        time.sleep(0.5)
        pyautogui.leftClick(respawn)

    print("It appears you are alive")
    time.sleep(1)

setglobals()
resetGlobals()

#Code block for threading

# use threading for fishing activation
def threadingfish():
    # Call work function
    t1 = Thread(target=fishing)
    t1.start()
    print(t1.name)

# use threading for trader activation
def threadingtrader():
    # Call work function
    t1 = Thread(target=trading)
    t1.start()
    print(t1.name)

# use threading for recycler activation
def threadingrecycler():
    # Call work function
    t1 = Thread(target=recycling)
    t1.start()
    print(t1.name)

# use threading for soft side activation
def threadingsoftside():
    # Call work function
    t1 = Thread(target=softsiding)
    t1.start()
    print(t1.name)

# use threading for antiafk activation
def threadingantiafk():
    # Call work function
    t1 = Thread(target=antiafker)
    t1.start()
    print(t1.name)

#threading for updating gui constantly
def guithreader():
    #Constant update gui
    t2 = Thread(target=updater)
    t2.start()
    print(t2.name)

#Active component to update labels and check for user input to regain control
def updater():
    while True:
        #Call globals that will later be used to display session statistics.
        global gutcounter
        global programclose
        global totalCatches
        global processStatus
        global failsafe
        global timesincelastaction

        #Call the current state of Global stop commands.
        global fishstop
        global traderstop
        global recyclerstop
        global softsidestop
        global antiafkstop

        #If the user hold down the "P" key all global stops will be set to True to allow the user to regain access to their keyboard and mouse.
        if keyboard.is_pressed("p") == True:
            print("Stopping all programs")
            fishstop = True
            traderstop = True
            recyclerstop = True
            antiafkstop = True
            softsidestop = True

        #Small sleep timer to not overload resources.
        time.sleep(0.3)

        #if the main GUI loop is closed, end this thread to stop the application being open past close.
        if programclose == True:
            break

        #Old code that updates labels with current stats, to be brought back in future updates.

        '''
        failsafeLabel.configure(text=f"Failsafe is: {failsafe}")
        baitLabel.configure(text=f"gutcounter is: {gutcounter}")
        failsafeLabel.configure(text=f"Failsafe is: {failsafe}")
        totalCatchesLabel.configure(text=f"Total Catches is: {totalCatches}")
        processStatusLabel.configure(text=f"Currently doing: {processStatus}")
        print(f"There are currently {threading.active_count()} open threads")
        '''

#Define code blocks for functions
def fishing():
    if True:
        global processStatus

        processStatus = "loading fishing bot"
        print('Program is running')
        time.sleep(3)
        print('program loaded')
        # Temp delay to load into game screen

        global failsafe
        global gutcounter
        global totalCatches
        # Variables set to 0 that we will need to call upon later

        # Define fishing functions
        if True: #Define fishing functions
            def rodcheck():
                global processStatus
                brokenrod = pyautogui.locateCenterOnScreen("Images/brokenrod2.png", confidence=0.65, grayscale=True,
                                                           region=(1138, 961, 1231, 1051))

                print(brokenrod)

                if str(brokenrod) != "None":
                    print("Rod broken, need new rod")
                    keyboard.press("tab")
                    time.sleep(0.3)
                    keyboard.release("tab")
                    time.sleep(0.3)
                    newrod = pyautogui.locateCenterOnScreen("Images/rod.png", confidence=0.8, grayscale=True)
                    pyautogui.leftClick(newrod)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")

            def cast():
                pydirectinput.mouseDown(button='right')
                time.sleep(1)
                pydirectinput.mouseDown(button='left')
                time.sleep(0.3)
                pydirectinput.mouseUp(button='left')
                pydirectinput.mouseUp(button='right')
                # The above code when called holds the right click for one second, before clicking left mouse to "Shoot" the bobber

            def reel():
                time.sleep(3.5)
                keyboard.press('s')
                keyboard.press('d')
                time.sleep(2.5)
                keyboard.release('s')
                keyboard.release('d')
                # The current reeling code works based off the above time frames which I have identified as suitable to avoid line snaps
                # This could be further optimized with further research.

            def baitcheck():
                global processStatus
                image = PIL.ImageGrab.grab()  # Define an area to capture.
                rodbait = image.getpixel((1153, 971))  # What pixel do we want?

                print(rodbait)

                if rodbait[0] < 200 and rodbait[1] < 200 and rodbait[2] < 200:
                    print("Rod empty, need more bait")
                    keyboard.press("tab")
                    time.sleep(0.3)
                    keyboard.release("tab")
                    time.sleep(0.3)
                    trout = pyautogui.locateCenterOnScreen("Images/smalltrout.png", confidence=0.8, grayscale=True)
                    rawfish = pyautogui.locateCenterOnScreen("Images/rawfish.png", confidence=0.8, grayscale=True)
                    if str(trout) != "None" and app.fish_frame_checkbox_1.get() == 1:
                        pyautogui.leftClick(trout)
                        pyautogui.dragTo(1181, 1003, duration=0.7)
                        time.sleep(0.5)
                        keyboard.press("esc")
                        time.sleep(0.3)
                        keyboard.release("esc")
                    else:
                        pyautogui.leftClick(rawfish)
                        pyautogui.dragTo(1181, 1003, duration=0.7)
                        time.sleep(0.5)
                        keyboard.press("esc")
                        time.sleep(0.3)
                        keyboard.release("esc")

            def gutter():
                global processStatus
                processStatus = "Checking inventory to gut..."

                print(processStatus)

                keyboard.press("tab")
                time.sleep(0.3)
                keyboard.release("tab")
                time.sleep(0.3)
                herring = pyautogui.locateCenterOnScreen("Images/herring.png", confidence=0.7, grayscale=True)
                sardine = pyautogui.locateCenterOnScreen("Images/sardine.png", confidence=0.7, grayscale=True)
                anchovy = pyautogui.locateCenterOnScreen("Images/anchovy.png", confidence=0.7, grayscale=True)
                gut = pyautogui.locateCenterOnScreen("Images/gut.png", confidence=0.7, grayscale=True)

                print(herring)
                print(sardine)
                print(anchovy)
                print(gut)

                while str(herring) != "None" or str(sardine) != "None" or str(anchovy) != "None":
                    processStatus = "Gutting low tier fish..."
                    while str(herring) != "None":
                        herring = pyautogui.locateCenterOnScreen("Images/herring.png", confidence=0.7, grayscale=True)
                        pyautogui.leftClick(herring)
                        time.sleep(0.7)
                        gut = pyautogui.locateCenterOnScreen("Images/gut.png", confidence=0.7, grayscale=True)
                        while str(gut) != "None":
                            pyautogui.leftClick(gut)
                            time.sleep(0.5)
                            print("Gutted")
                            gut = pyautogui.locateCenterOnScreen("Images/gut.png", confidence=0.7, grayscale=True)
                        herring = pyautogui.locateCenterOnScreen("Images/herring.png", confidence=0.7, grayscale=True)
                    print("All Herring gutted")
                    while str(sardine) != "None":
                        sardine = pyautogui.locateCenterOnScreen("Images/sardine.png", confidence=0.7, grayscale=True)
                        pyautogui.leftClick(sardine)
                        time.sleep(0.7)
                        gut = pyautogui.locateCenterOnScreen("Images/gut.png", confidence=0.7, grayscale=True)
                        pyautogui.leftClick(gut)
                        time.sleep(0.7)
                        print("Gutted")
                        sardine = pyautogui.locateCenterOnScreen("Images/sardine.png", confidence=0.7, grayscale=True)
                    print("All Sardine gutted")
                    while str(anchovy) != "None":
                        anchovy = pyautogui.locateCenterOnScreen("Images/anchovy.png", confidence=0.7, grayscale=True)
                        pyautogui.leftClick(anchovy)
                        time.sleep(0.7)
                        gut = pyautogui.locateCenterOnScreen("Images/gut.png", confidence=0.7, grayscale=True)
                        pyautogui.leftClick(gut)
                        time.sleep(0.7)
                        print("Gutted")
                        anchovy = pyautogui.locateCenterOnScreen("Images/anchovy.png", confidence=0.7, grayscale=True)
                    print("All Anchovy gutted")
                else:
                    print("Finished")

                if app.fish_frame_checkbox_2.get() == 1:
                    bones = pyautogui.locateCenterOnScreen("Images/bones.png", confidence=0.7, grayscale=True)
                    while str(bones) != "None":
                        pyautogui.leftClick(bones)
                        pyautogui.dragTo(1500, 1000, duration=0.7)
                        time.sleep(0.5)
                        bones = pyautogui.locateCenterOnScreen("Images/bones.png", confidence=0.7, grayscale=True)
                    time.sleep(1)

                keyboard.press("esc")
                time.sleep(0.3)
                keyboard.release("esc")

                time.sleep(2)

        failsafe = 0

        #Main loop
        while True:
            global fishstop
            if fishstop == True:
                processStatus = "Fishing bot shutting down"
                print("Stopping program")
                time.sleep(2)
                processStatus = "Waiting to start"

                app.fishToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'],
                                                 hover_color=['#36719F', '#144870'])
                app.fishToggleButton.update()
                break
            # if the button is clicked again after starting, break the thread.

            # Main code block
            if gutcounter == 10:
                processStatus = "Gutting fish"
                gutter()
                gutcounter = 0
            # After catching 10 fish, the program will gut all low tier fish in inventory.

            image = PIL.ImageGrab.grab()  # Define an area to capture.
            rgb = image.getpixel((1850, 790))  # What pixel do we want?

            if rgb == (88, 101, 66) or failsafe > 15:
                processStatus = "Fish caught"
                print("Fish caught")
                time.sleep(7)

                failsafe = 0
                gutcounter += 1
                print("Bait used: ", gutcounter)
                totalCatches += 1

                rodcheck()
                baitcheck()


                if app.fish_frame_checkbox_4.get() == 1:
                    image = PIL.ImageGrab.grab()  # Define an area to capture.
                    rgbwater = image.getpixel((1770, 990))  # What pixel do we want?
                    rgbfood = image.getpixel((1770, 1032))  # What pixel do we want?

                    if rgbwater[2] < 180 or rgbfood[0] < 180:
                        print("Hungry or thirsty, eating")
                        foodcheck()
                    else:
                        print("Not hungry or thirsty")

                cast()

            else:
                processStatus = "Fishing"
                print("No fish caught")
                failsafe += 1
                reel()

# work function
def trading():
    if True:
        global processStatus

        '''
        1692,502 115,141,69 #738D45 - Green buy
        1689,392 86,50,42 #56322A - Red buy
        
        
            image = PIL.ImageGrab.grab()  # Define an area to capture.
            rgb = image.getpixel((1850, 790))  # What pixel do we want?

            if rgb == (88, 101, 66) or failsafe > 18:
                processStatus = "Fish caught"
                print("Fish caught")
                time.sleep(7)
                
                
        '''
        time.sleep(2)

        def tradeinput(x,y):
            global tradeskip
            pydirectinput.leftClick(x,y)
            time.sleep(0.1)
            pydirectinput.keyDown("9")
            time.sleep(0.2)
            pydirectinput.keyDown("0")
            time.sleep(0.2)
            pydirectinput.keyUp("9")
            pydirectinput.keyUp("0")
            tradeskip = True

        while True:
            global tradeskip
            tradeskip = False
            #Check if user has input a request to stop the app.
            global traderstop
            if traderstop == True:
                processStatus = "trader bot shutting down"
                print("Stopping program")
                time.sleep(2)
                processStatus = "Waiting to start"

                app.traderToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'],
                                             hover_color=['#36719F', '#144870'])
                app.traderToggleButton.update()
                break
            # if the button is clicked again after starting, break the thread.
            pydirectinput.moveTo(1000,500)
            time.sleep(1)

            image = PIL.ImageGrab.grab()  # Define an area to capture.
            rgbtrout = image.getpixel((1691, 280))  # What pixel do we want? 110 135 66
            rgbshark = image.getpixel((1692,502))  # What pixel do we want?
            rgbsalmon = image.getpixel((1689, 614))  # What pixel do we want?
            rgbsmoke = image.getpixel((1694, 834))  # What pixel do we want?
            rgbgrenade = image.getpixel((1691,504))  # What pixel do we want?
            rgbcloth = image.getpixel((1691,611))  # What pixel do we want?
            rgbfertilizer = image.getpixel((1687,827))  # What pixel do we want?

            if app.trader_cloth.get() == 1 and tradeskip == False:
                if rgbcloth == (115,141,69) or rgbcloth == (115, 141, 69) or rgbcloth == (110, 135, 66):
                    tradeinput(1731,670)
                    pydirectinput.leftClick(1731,620)
                    time.sleep(1)
            if app.trader_fertilizer.get() == 1 and tradeskip == False:
                if rgbfertilizer == (115,141,69) or rgbfertilizer == (115, 141, 69) or rgbfertilizer == (110, 135, 66):
                    tradeinput(1732,893)
                    pydirectinput.leftClick(1732,841)
            if app.trader_smoke.get() == 1 and tradeskip == False:
                if rgbsmoke == (115,141,69) or rgbsmoke == (115, 141, 69) or rgbsmoke == (110, 135, 66):
                    tradeinput(1729,891)
                    pydirectinput.leftClick(1729,841)
            if app.trader_grenade.get() == 1 and tradeskip == False:
                if rgbgrenade == (115,141,69) or rgbgrenade == (115, 141, 69) or rgbgrenade == (110, 135, 66):
                    tradeinput(1734,560)
                    pydirectinput.leftClick(1734,510)
            if app.trader_shark.get() == 1 and tradeskip == False:
                if rgbshark == (115, 141, 69) or rgbshark == (115, 141, 69) or rgbshark == (110, 135, 66):
                    tradeinput(1733,555)
                    pydirectinput.leftClick(1689,492)
            if app.trader_salmon.get() == 1 and tradeskip == False:
                if rgbsalmon == (115,141,69) or rgbsalmon == (115, 141, 69) or rgbsalmon == (110, 135, 66):
                    tradeinput(1738,663)
                    pydirectinput.leftClick(1687,601)
            if app.trader_trout.get() == 1 and tradeskip == False:
                if rgbtrout == (115,141,69) or rgbtrout == (115, 141, 69) or rgbtrout == (110, 135, 66):
                    tradeinput(1732,332)
                    pydirectinput.leftClick(1687,271)

# work function
def recycling():
    time.sleep(2)

    if True:
        # #Crouch if checkbox ticked
        # if app.recycler_crouch.get() == 1:
        #     pydirectinput.keyDown("ctrl")

        # List of components / items we wish to search for
        complist = (
            "fuse", "gear", "cctv", "grenade", "blade", "laptop", "pipe", "propane", "rifle", "semi", "rope", "sewing",
            "sheet", "sign", "smg", "smoke", "tarp", "techtrash", "spring")

        # Give time to tab into game
        time.sleep(2)

        while True:

            pyautogui.rightClick(1299, 715)
            pyautogui.rightClick(1390, 719)
            pyautogui.rightClick(1484, 714)
            pyautogui.rightClick(1600, 714)
            pyautogui.rightClick(1700, 714)
            pyautogui.rightClick(1800, 714)

            recycleron = pyautogui.locateCenterOnScreen("Images/Turn on.png", confidence=0.85)
            recycleroff = pyautogui.locateCenterOnScreen("Images/turnoff.png", confidence=0.85)

            global recyclerstop
            global processStatus

            '''
            #Check if we have lost the recycler, if we have stop the program.
            if str(recycleron) == "None" and str(recycleroff) == "None":
                print("We lost the recycler window")
                recyclerstop = True
            '''

            x = 6

            for i in complist:
                if x == 0:
                    print("Recycler full, waiting for finish.")
                    break

                png = f"Images/{i}.png"
                print(png)

                test = pyautogui.locateCenterOnScreen(png, confidence=0.7, region=(657, 569, 1232, 1058))
                recycleron = pyautogui.locateCenterOnScreen("Images/Turn on.png", confidence=0.85)

                print(test)
                time.sleep(0.15)

                if str(test) != "None":
                    test = pyautogui.locateCenterOnScreen(png, confidence=0.7, region=(657, 569, 1232, 1058))
                    pyautogui.leftClick(test)
                    pyautogui.rightClick(test)
                    time.sleep(0.5)
                    # Checks if recycler needs to be activated after placing item in
                    if str(recycleron) != "None":
                        pyautogui.leftClick(recycleron)
                        time.sleep(0.1)
                    x -= 1

            pyautogui.rightClick(1299, 715)
            pyautogui.rightClick(1390, 719)
            pyautogui.rightClick(1484, 714)
            pyautogui.rightClick(1600, 714)
            pyautogui.rightClick(1700, 714)
            pyautogui.rightClick(1800, 714)

            sleep = 300

            while sleep != 0:
                sleep -= 1
                print(sleep, " Remaining before next run")
                recycleron = pyautogui.locateCenterOnScreen("Images/Turn on.png", confidence=0.85)
                if str(recycleron) != "None":
                    print("Current queue finished, refill.")
                    break

                time.sleep(1)

# work function
def softsiding():
    if True:
        time.sleep(3)
        global softsidestop
        global processStatus

        pydirectinput.mouseDown()

        while True:
            global softsidestop

            if softsidestop == True:
                processStatus = "softside bot shutting down"
                print("Stopping program")
                time.sleep(2)
                processStatus = "Waiting to start"

                app.softsideToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'],
                                                   hover_color=['#36719F', '#144870'])
                app.softsideToggleButton.update()
                break
            # if the button is clicked again after starting, break the thread.

            time.sleep(1)
            brokentool = pyautogui.locateCenterOnScreen("Images/brokentool.png", confidence=0.7, grayscale=True,
                                                        region=(1138, 961, 1231, 1051))

            print(brokentool)

            if str(brokentool) != "None":
                pydirectinput.mouseUp()
                print("Rod broken, need new rod")
                keyboard.press("tab")
                time.sleep(0.3)
                keyboard.release("tab")
                time.sleep(0.6)
                newspear = pyautogui.locateCenterOnScreen("Images/spear.png", confidence=0.9, grayscale=True)
                newpick = pyautogui.locateCenterOnScreen("Images/pickaxe.png", confidence=0.9, grayscale=True)
                newsword = pyautogui.locateCenterOnScreen("Images/sword.png", confidence=0.9, grayscale=True)
                newhammer = pyautogui.locateCenterOnScreen("Images/hammer.png", confidence=0.9, grayscale=True)
                newstonespear = pyautogui.locateCenterOnScreen("Images/stonespear.png", confidence=0.9, grayscale=True)

                print("spear found at: ", newspear)
                print(newpick)
                print(newsword)
                print(newhammer)
                print(newstonespear)

                if str(newspear) != "None":
                    print("Found spear, moving")
                    pyautogui.leftClick(newspear)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")
                elif str(newpick) != "None":
                    print("Found pickaxe, moving")
                    pyautogui.leftClick(newpick)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")
                elif str(newsword) != "None":
                    print("Found sword, moving")
                    pyautogui.leftClick(newsword)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")
                elif str(newhammer) != "None":
                    print("Found hammer, moving")
                    pyautogui.leftClick(newhammer)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")
                elif str(newstonespear) != "None":
                    print("Found stone spear, moving")
                    pyautogui.leftClick(newstonespear)
                    pyautogui.dragTo(1181, 1003, duration=0.7)
                    time.sleep(0.5)
                    keyboard.press("esc")
                    time.sleep(0.3)
                    keyboard.release("esc")
                pydirectinput.keyDown("6")
                time.sleep(3)
                pydirectinput.keyUp("6")
                pydirectinput.mouseDown()

# work function
def antiafker():
    if True:
        global processStatus


        processStatus = "loading"
        print('Program is running')
        time.sleep(1)
        print('program loaded')
        # Temp delay to load into game screen

        global timesincelastaction
        timesincelastaction = 0
        # Variables set to 0 that we will need to call upon later

        while True:
            global antiafkstop

            if antiafkstop == True:
                processStatus = "stopping program"
                print("Stopping program")
                time.sleep(2)
                processStatus = "Waiting to start"

                app.antiafkToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'],
                                                   hover_color=['#36719F', '#144870'])
                app.antiafkToggleButton.update()
                break

            timesincelastaction += 1

            if app.antiafk_jump.get() == 1 and timesincelastaction > 10:
                print("Jumping ", app.antiafk_jump.get())
                keyboard.press("space")
                time.sleep(0.5)
                keyboard.release("space")
                timesincelastaction = 0

            if app.antiafk_left.get() == 1 and timesincelastaction > 10:
                print("Clicking Mouse 1 ", app.antiafk_jump.get())
                pydirectinput.mouseDown(button='left')
                time.sleep(0.5)
                pydirectinput.mouseUp(button='left')
                timesincelastaction = 0

            if app.antiafk_jiggle.get() == 1 and timesincelastaction > 10:
                print("jiggle ", app.antiafk_jump.get())
                keyboard.press("a")
                time.sleep(0.2)
                keyboard.release("a")
                keyboard.press("d")
                time.sleep(0.2)
                keyboard.release("d")
                timesincelastaction = 0

            if app.antiafk_eat.get() == 1 and timesincelastaction > 10:
                print("Jumping ", app.antiafk_jump.get())
                keyboard.press("space")
                time.sleep(0.5)
                keyboard.release("space")
                timesincelastaction = 0

            # if app.antiafk_death.get() == 1 and timesincelastaction > 10:
            #     print("logging out ", app.antiafk_jump.get())
            #     keyboard.press("space")
            #     time.sleep(0.5)
            #     keyboard.release("space")
            #     timesincelastaction = 0

            print("Anti afk")
            print(f"time since last action {timesincelastaction}")
            time.sleep(1)

#Open License file and copy contained license
with open('license.txt') as f:
    key = f.readlines()
    f.close()
    print(len(str(key)))
    try:
        print(key[0])
    except:
        key = ("Please enter a new key")

#Start checking for user input to cancel scripts.
guithreader()

class mainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Auto Rust")
        self.geometry("700x450")
        self.resizable(width=False, height=False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        #Create Menu header
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Auto Rust",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        #Auto fish menu button
        self.fish_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="AUTO FISH",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.fish_button_event)
        self.fish_button.grid(row=1, column=0, sticky="ew")

        # Auto trade menu button
        self.trader_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="AUTO TRADE",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.trader_button_event)
        self.trader_button.grid(row=2, column=0, sticky="ew")

        # Auto recycle menu button
        self.recycler_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="AUTO RECYCLE",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.recycler_button_event)
        self.recycler_button.grid(row=3, column=0, sticky="ew")

        # Auto softside menu button
        self.softside_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="AUTO SOFT SIDE",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.softside_button_event)
        self.softside_button.grid(row=4, column=0, sticky="ew")

        # Auto anti afk menu button
        self.antiafk_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ANTI AFK",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.antiafk_button_event)
        self.antiafk_button.grid(row=5, column=0, sticky="ew")

        # Theme drop-down selection
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create fishing menu frame
        self.fish_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fish_frame.grid_columnconfigure(1, weight=1)

        self.fish_frame_large_image_label = customtkinter.CTkLabel(self.fish_frame, text="")
        self.fish_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.fish_frame_checkbox_1 = customtkinter.CTkCheckBox(self.fish_frame, text="Use small trout as bait")
        self.fish_frame_checkbox_1.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.fish_frame_checkbox_2 = customtkinter.CTkCheckBox(self.fish_frame, text="Discard bones")
        self.fish_frame_checkbox_2.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.fish_frame_checkbox_3 = customtkinter.CTkCheckBox(self.fish_frame, text="Log out on full inventory")
        self.fish_frame_checkbox_3.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.fish_frame_checkbox_4 = customtkinter.CTkCheckBox(self.fish_frame, text="Eat pumpkins below half hunger / water")
        self.fish_frame_checkbox_4.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        self.fish_frame_checkbox_5 = customtkinter.CTkCheckBox(self.fish_frame, text="Log out on death / teleport")
        self.fish_frame_checkbox_5.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.fishToggleButton = self.fish_frame_button_4 = customtkinter.CTkButton(self.fish_frame, text="Start", compound="top",
                                                                          command=self.fishToggle)
        self.fishToggleButton.grid(row=6, column=0, padx=20, pady=10, sticky='w')


        # create trader frame
        self.trader_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.trader_frame.grid_columnconfigure(1, weight=1)

        self.trader_frame_large_image_label = customtkinter.CTkLabel(self.trader_frame, text="")
        self.trader_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.trader_cloth = customtkinter.CTkCheckBox(self.trader_frame, text="Sell Cloth")
        self.trader_cloth.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.trader_fertilizer = customtkinter.CTkCheckBox(self.trader_frame, text="Sell Fertilizer")
        self.trader_fertilizer.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.trader_smoke = customtkinter.CTkCheckBox(self.trader_frame, text="Buy Smoke Grenades")
        self.trader_smoke.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.trader_grenade = customtkinter.CTkCheckBox(self.trader_frame, text="Buy Grenades")
        self.trader_grenade.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        # self.trader_fullinv = customtkinter.CTkCheckBox(self.trader_frame, text="Stop on full inventory")
        # self.trader_fullinv.grid(row=5, column=0, padx=20, pady=10, sticky='w')

        self.trader_shark = customtkinter.CTkCheckBox(self.trader_frame, text="Sell Sharks")
        self.trader_shark.grid(row=1, column=1, padx=20, pady=10, sticky='w')
        self.trader_salmon = customtkinter.CTkCheckBox(self.trader_frame, text="Sell Salmon")
        self.trader_salmon.grid(row=2, column=1, padx=20, pady=10, sticky='w')
        self.trader_trout = customtkinter.CTkCheckBox(self.trader_frame, text="Sell Small Trout")
        self.trader_trout.grid(row=3, column=1, padx=20, pady=10, sticky='w')

        self.traderToggleButton = customtkinter.CTkButton(self.trader_frame, text="Start", compound="top", command=self.traderToggle)
        self.traderToggleButton.grid(row=6, column=0, padx=20, pady=10, sticky='w')

        # create recycler frame
        self.recycler_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.recycler_frame.grid_columnconfigure(1, weight=1)

        self.recycler_frame_large_image_label = customtkinter.CTkLabel(self.recycler_frame, text="")
        self.recycler_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.recycler_grenade = customtkinter.CTkCheckBox(self.recycler_frame, text="Grenades")
        self.recycler_grenade.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.recycler_grenade.select()
        self.recycler_smoke = customtkinter.CTkCheckBox(self.recycler_frame, text="Smoke Grenades")
        self.recycler_smoke.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.recycler_smoke.select()
        self.recycler_pipe = customtkinter.CTkCheckBox(self.recycler_frame, text="Pipes")
        self.recycler_pipe.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.recycler_pipe.select()
        self.recycler_techtrash = customtkinter.CTkCheckBox(self.recycler_frame,text="Tech trash")
        self.recycler_techtrash.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        self.recycler_techtrash.select()
        self.recycler_rope = customtkinter.CTkCheckBox(self.recycler_frame, text="Rope")
        self.recycler_rope.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.recycler_rope.select()
        self.recycler_blade = customtkinter.CTkCheckBox(self.recycler_frame, text="Metal blade")
        self.recycler_blade.grid(row=6, column=0, padx=20, pady=10, sticky='w')
        self.recycler_blade.select()

        self.recycler_gear = customtkinter.CTkCheckBox(self.recycler_frame, text="Gears")
        self.recycler_gear.grid(row=1, column=1, padx=20, pady=10, sticky='w')
        self.recycler_gear.select()
        self.recycler_propane = customtkinter.CTkCheckBox(self.recycler_frame, text="Propane tank")
        self.recycler_propane.grid(row=2, column=1, padx=20, pady=10, sticky='w')
        self.recycler_propane.select()
        self.recycler_smg = customtkinter.CTkCheckBox(self.recycler_frame, text="SMG body")
        self.recycler_smg.grid(row=3, column=1, padx=20, pady=10, sticky='w')
        self.recycler_smg.select()
        self.recycler_rifle = customtkinter.CTkCheckBox(self.recycler_frame, text="Rifle body")
        self.recycler_rifle.grid(row=4, column=1, padx=20, pady=10, sticky='w')
        self.recycler_rifle.select()
        self.recycler_cctv = customtkinter.CTkCheckBox(self.recycler_frame, text="CCTV camera")
        self.recycler_cctv.grid(row=5, column=1, padx=20, pady=10, sticky='w')
        self.recycler_cctv.select()
        self.recycler_sign = customtkinter.CTkCheckBox(self.recycler_frame, text="Road signs")
        self.recycler_sign.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.recycler_sign.select()

        self.recycler_laptop = customtkinter.CTkCheckBox(self.recycler_frame, text="Laptops")
        self.recycler_laptop.grid(row=1, column=2, padx=20, pady=10, sticky='w')
        self.recycler_laptop.select()
        self.recycler_sewing = customtkinter.CTkCheckBox(self.recycler_frame, text="Sewing kits")
        self.recycler_sewing.grid(row=2, column=2, padx=20, pady=10, sticky='w')
        self.recycler_sewing.select()
        self.recycler_tarp = customtkinter.CTkCheckBox(self.recycler_frame, text="Tarp")
        self.recycler_tarp.grid(row=3, column=2, padx=20, pady=10, sticky='w')
        self.recycler_tarp.select()
        self.recycler_sheet = customtkinter.CTkCheckBox(self.recycler_frame, text="Sheet metal")
        self.recycler_sheet.grid(row=4, column=2, padx=20, pady=10, sticky='w')
        self.recycler_sheet.select()
        self.recycler_semi = customtkinter.CTkCheckBox(self.recycler_frame, text="Semi bodies")
        self.recycler_semi.grid(row=5, column=2, padx=20, pady=10, sticky='w')
        self.recycler_semi.select()
        self.recycler_spring = customtkinter.CTkCheckBox(self.recycler_frame, text="Springs")
        self.recycler_spring.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.recycler_spring.select()
        self.recycler_fuse = customtkinter.CTkCheckBox(self.recycler_frame, text="Fuse")
        self.recycler_fuse.grid(row=6, column=2, padx=20, pady=10, sticky='w')
        self.recycler_fuse.select()

        # self.recycler_crouch = customtkinter.CTkCheckBox(self.recycler_frame, text="Hold Crouch (CTRL)")
        # self.recycler_crouch.grid(row=6, column=0, padx=20, pady=10, sticky='w')

        self.recyclerToggleButton = customtkinter.CTkButton(self.recycler_frame, text="Start", compound="top", command=self.recyclerToggle)
        self.recyclerToggleButton.grid(row=8, column=0, padx=20, pady=10, sticky='w')

        # create softside frame
        self.softside_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.softside_frame.grid_columnconfigure(1, weight=1)

        self.softside_frame_large_image_label = customtkinter.CTkLabel(self.softside_frame, text="")
        self.softside_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.softside_frame_checkbox_1 = customtkinter.CTkCheckBox(self.softside_frame, text="Spears")
        self.softside_frame_checkbox_1.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.softside_frame_checkbox_2 = customtkinter.CTkCheckBox(self.softside_frame, text="Pickaxes")
        self.softside_frame_checkbox_2.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.softside_frame_checkbox_3 = customtkinter.CTkCheckBox(self.softside_frame,
                                                                   text="Salvaged hammer")
        self.softside_frame_checkbox_3.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.softside_frame_checkbox_4 = customtkinter.CTkCheckBox(self.softside_frame,
                                                                   text="Craft stone spear on break")
        self.softside_frame_checkbox_4.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        # self.softside_frame_checkbox_5 = customtkinter.CTkCheckBox(self.softside_frame,
        #                                                            text="Log out on death / teleport")
        # self.softside_frame_checkbox_5.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.softsideToggleButton = customtkinter.CTkButton(self.softside_frame, text="Start", compound="top", command=self.softsideToggle)
        self.softsideToggleButton.grid(row=6, column=0, padx=20, pady=10, sticky='w')

        # create antiafk frame
        self.antiafk_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.antiafk_frame.grid_columnconfigure(1, weight=1)

        self.antiafk_frame_large_image_label = customtkinter.CTkLabel(self.antiafk_frame, text="")
        self.antiafk_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.antiafk_jump = customtkinter.CTkCheckBox(self.antiafk_frame, text="Jump")
        self.antiafk_jump.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.antiafk_left = customtkinter.CTkCheckBox(self.antiafk_frame, text="Left click")
        self.antiafk_left.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.antiafk_jiggle = customtkinter.CTkCheckBox(self.antiafk_frame,
                                                                   text="Jiggle move forward / back")
        self.antiafk_jiggle.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.antiafk_eat = customtkinter.CTkCheckBox(self.antiafk_frame,
                                                                   text="Eat pumpkins below half hunger / water")
        self.antiafk_eat.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        self.antiafk_death = customtkinter.CTkCheckBox(self.antiafk_frame,
                                                                   text="Log out on death / teleport")
        self.antiafk_death.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.antiafkToggleButton = customtkinter.CTkButton(self.antiafk_frame, text="Start", compound="top", command=self.antiafkToggle)
        self.antiafkToggleButton.grid(row=6, column=0, padx=20, pady=10, sticky='w')

        # select default frame
        self.select_frame_by_name("fish")

    def fishToggle(self):
        if self.fishToggleButton.cget("text") == "Start":
            print("Fishing starting")
            global fishstop
            fishstop = False
            self.fishToggleButton.configure(text="Stop", fg_color="#B30202", hover_color="dark red")
            self.fishToggleButton.update()
            threadingfish()
        elif self.fishToggleButton.cget("text") == "Stop":
            self.fishToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'], hover_color=['#36719F', '#144870'])
            self.fishToggleButton.update()
            fishstop = True
            print("stop status: ", fishstop)

    def traderToggle(self):
        if self.traderToggleButton.cget("text") == "Start":
            print("Trader starting")
            global traderstop
            traderstop = False
            self.traderToggleButton.configure(text="Stop", fg_color="#B30202", hover_color="dark red")
            self.traderToggleButton.update()
            threadingtrader()
        elif self.traderToggleButton.cget("text") == "Stop":
            self.traderToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'], hover_color=['#36719F', '#144870'])
            self.traderToggleButton.update()
            traderstop = True
            print("stop status: ", traderstop)

    def recyclerToggle(self):
        if self.recyclerToggleButton.cget("text") == "Start":
            print("Recycler starting")
            global recyclerstop
            recyclerstop = False
            self.recyclerToggleButton.configure(text="Stop", fg_color="#B30202", hover_color="dark red")
            self.recyclerToggleButton.update()
            threadingrecycler()
        elif self.recyclerToggleButton.cget("text") == "Stop":
            self.recyclerToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'], hover_color=['#36719F', '#144870'])
            self.recyclerToggleButton.update()
            recyclerstop = True
            print("stop status: ", recyclerstop)

    def softsideToggle(self):
        if self.softsideToggleButton.cget("text") == "Start":
            print("Soft side starting")
            global softsidestop
            softsidestop = False
            self.softsideToggleButton.configure(text="Stop", fg_color="#B30202", hover_color="dark red")
            self.softsideToggleButton.update()
            threadingsoftside()
        elif self.softsideToggleButton.cget("text") == "Stop":
            self.softsideToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'], hover_color=['#36719F', '#144870'])
            self.softsideToggleButton.update()
            softsidestop = True
            print("stop status: ", softsidestop)

    def antiafkToggle(self):
        if self.antiafkToggleButton.cget("text") == "Start":
            print("Anti afk starting")
            global antiafkstop
            antiafkstop = False
            self.antiafkToggleButton.configure(text="Stop", fg_color="#B30202", hover_color="dark red")
            self.antiafkToggleButton.update()
            threadingantiafk()
        elif self.antiafkToggleButton.cget("text") == "Stop":
            self.antiafkToggleButton.configure(text="Start", fg_color=['#3B8ED0', '#1F6AA5'], hover_color=['#36719F', '#144870'])
            self.antiafkToggleButton.update()
            antiafkstop = True
            print("stop status: ", antiafkstop)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.fish_button.configure(fg_color=("gray75", "gray25") if name == "fish" else "transparent")
        self.trader_button.configure(fg_color=("gray75", "gray25") if name == "trader" else "transparent")
        self.recycler_button.configure(fg_color=("gray75", "gray25") if name == "recycler" else "transparent")
        self.softside_button.configure(fg_color=("gray75", "gray25") if name == "softside" else "transparent")
        self.antiafk_button.configure(fg_color=("gray75", "gray25") if name == "antiafk" else "transparent")

        # show selected frame
        if name == "fish":
            self.fish_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fish_frame.grid_forget()
        if name == "trader":
            self.trader_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.trader_frame.grid_forget()
        if name == "recycler":
            self.recycler_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.recycler_frame.grid_forget()
        if name == "softside":
            self.softside_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.softside_frame.grid_forget()
        if name == "antiafk":
            self.antiafk_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.antiafk_frame.grid_forget()

    def fish_button_event(self):
        self.select_frame_by_name("fish")

    def trader_button_event(self):
        self.select_frame_by_name("trader")

    def recycler_button_event(self):
        self.select_frame_by_name("recycler")

    def softside_button_event(self):
        self.select_frame_by_name("softside")

    def antiafk_button_event(self):
        self.select_frame_by_name("antiafk")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

class licenseCheck(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rust Multitool")
        self.geometry("400x250")
        self.resizable(width=False, height=False)

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.frame_1 = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_1, justify=customtkinter.LEFT, text="Rust Multitool",
                                              font=("Arial", 20))
        self.label_1.pack(pady=10, padx=10)

        self.licenseEntry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Copy and paste license", width=250)
        self.licenseEntry.pack(pady=10, padx=10)
        if len(str(key)) > 5:
            self.licenseEntry.insert(0,key)

        self.licenseRemember = customtkinter.CTkCheckBox(master=self.frame_1, text="Remember License Key?")
        self.licenseRemember.pack(pady=10, padx=10)
        self.licenseRemember.select()

        self.registerLicenseButton = customtkinter.CTkButton(master=self.frame_1, command=self.registerLicense, text="Submit")
        self.registerLicenseButton.pack(pady=10, padx=10)


    def registerLicense(self):
        print("Button click")
        key = self.licenseEntry.get()
        print(str(key))

        if self.licenseRemember.get() == 1:
            with open('license.txt', 'w') as f:
                f.write(self.licenseEntry.get())
                f.close()

        RSAPubKey = "<RSAKeyValue><Modulus>q3wp77HGCZEkBwTHrR9+QRCqwTYiSVd2e5BROP8kGTm/5lH3L/16JpQLnpqqqv2WEmkJyhOR5lWj/zV3fh5i0PwuZUbF3wTHuDWvGSiIBmlm3LGpoRuaUkDqcc4xEj3WotcI3JxoZ8EXD0UQldNn7/uBVeFgnkkLS/51ErD/1vZ++mV4bz1FB+gqVhs2huewAbLTgOnqlrMJudMTWOm65HLkRnYVMKRN2joCaBxU5dGmdVCY/rfLg4vNwOX1T5VG5fRhFPgZdPwsIwNPbGc4kvTGktYfh+3zrEnSemF4KQHkpzaGzLDkZ5D2VaRhWq70XVPhnSV6Rdo/ZRCvYYXKeQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
        auth = "WyIzNjc4MjgwNSIsInl1VGxKRXFDVmRDSVRxZHo4UDJnUVEybGZiS1FrcktOSDd3R3hEbSsiXQ=="

        result = Key.activate(token=auth, \
                              rsa_pub_key=RSAPubKey, \
                              product_id=18654, \
                              key=str(key), \
                              machine_code=Helpers.GetMachineCode(v=2))

        if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            print("The license does not work: {0}".format(result[1]))
        else:
            # everything went fine if we are here!
            print("The license is valid!")

            licenseCheck.destroy(self)

            if __name__ == "__main__":
                app = mainApp()
                app.mainloop()

licenseRequired = True

#Check if saved license is valid, if it is, run the main app.
if licenseRequired == True:
    RSAPubKey = "<RSAKeyValue><Modulus>q3wp77HGCZEkBwTHrR9+QRCqwTYiSVd2e5BROP8kGTm/5lH3L/16JpQLnpqqqv2WEmkJyhOR5lWj/zV3fh5i0PwuZUbF3wTHuDWvGSiIBmlm3LGpoRuaUkDqcc4xEj3WotcI3JxoZ8EXD0UQldNn7/uBVeFgnkkLS/51ErD/1vZ++mV4bz1FB+gqVhs2huewAbLTgOnqlrMJudMTWOm65HLkRnYVMKRN2joCaBxU5dGmdVCY/rfLg4vNwOX1T5VG5fRhFPgZdPwsIwNPbGc4kvTGktYfh+3zrEnSemF4KQHkpzaGzLDkZ5D2VaRhWq70XVPhnSV6Rdo/ZRCvYYXKeQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
    auth = "WyIzNjc4MjgwNSIsInl1VGxKRXFDVmRDSVRxZHo4UDJnUVEybGZiS1FrcktOSDd3R3hEbSsiXQ=="

    result = Key.activate(token=auth, \
                          rsa_pub_key=RSAPubKey, \
                          product_id=18654, \
                          key=key[0], \
                          machine_code=Helpers.GetMachineCode(v=2))

    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
        skiplicense = False

        errorapp = customtkinter.CTk()
        errorapp.geometry("400x200")
        errorapp.title("Error: Saved License no longer valid")

        def button_callback():
            print("Button click")
            errorapp.destroy()

        frame_1 = customtkinter.CTkFrame(master=errorapp)
        frame_1.pack(pady=20, padx=20, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="The License that is saved is no longer valid,\n please check internet connection. \n \n Otherwise check discord for updates. \n https://discord.gg/YPeJffHggy")
        label_1.pack(pady=5, padx=5)

        button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Enter License")
        button_1.pack(pady=20, padx=10)

        errorapp.mainloop()

    else:
        # everything went fine if we are here!
        print("The license is valid!")
        skiplicense = True

        if __name__ == "__main__":
            app = mainApp()
            app.mainloop()

#If no active license, open license input window.
if skiplicense != True:
    if __name__ == "__main__":
        app = licenseCheck()
        app.mainloop()

fishstop = True
traderstop= True
recyclerstop= True
softsidestop= True
antiafkstop= True
programclose=True

print("End of program")
