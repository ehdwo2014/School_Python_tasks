import pyautogui as pg
import os
import time
from threading import Timer
import pydirectinput as pd
import random
import pyscreenshot

from twocaptcha import TwoCaptcha




print("SelectTaskNumber:")
TaskNumber  = int(input())
print(TaskNumber)
Folder = r'C:\Users\DongJae Yoon\Desktop\PYDFO'
DFOFIle = r'C:\Users\DongJae Yoon\Desktop\PYDFO\Dungeon Fighter Online'
IDVector =[]
PasswordVector = []

IDVector.append("ehdwo2014@gmail.com")
PasswordVector.append("ehdwo456")
TimeOut = 300

Charimage1 = Folder + '\Char1.png'
Charimage2 = Folder + '\Char2.png'
Charimage3 = Folder + '\Char3.png'
Charimage4 = Folder + '\Char4.png'
Charimage5 = Folder + '\Char5.png'
Charimage6 = Folder + '\Char6.png'
Charimage7 = Folder + '\Char7.png'
Charimage8 = Folder + '\Char8.png'
Charimage9 = Folder + '\Char9.png'

captNoti = Folder + '\Capt_Noti.png'
captInput = Folder + '\capt_Input.png'
capt_OK = Folder + '\capt_OK.png'

vec =[]
vec.append(Charimage1)
vec.append(Charimage2)
vec.append(Charimage3)
vec.append(Charimage4)
vec.append(Charimage5)
vec.append(Charimage6)
vec.append(Charimage7)
vec.append(Charimage8)
vec.append(Charimage9)

VecSkill = []
VecSkill.append("q")
VecSkill.append("w")
VecSkill.append("e")
VecSkill.append("r")
VecSkill.append("t")
VecSkill.append("y")
VecSkill.append("a")
VecSkill.append("s")
VecSkill.append("d")
VecSkill.append("f")
VecSkill.append("g")
VecSkill.append("h")



def Entering():
    pg.keyDown("enter")
#Turning on
def Typing(s):
    for i in range(0, len(s)):
        pg.typewrite(s[i])
        Hold_On(0.05)


def IsThere(Path):
    if pg.locateOnScreen(Path, confidence=0.95) is not None:
        print(pg.locateOnScreen(Path, confidence=0.95))
        return True
    else:
        return False

def IsThereMild(Path):
    if pg.locateOnScreen(Path, confidence=0.80) is not None:
        print(pg.locateOnScreen(Path, confidence=0.80))
        return True
    else:
        return False


def IsThereVeryMild(Path):
    if pg.locateOnScreen(Path, confidence=0.8) is not None:
        print(pg.locateOnScreen(Path, confidence=0.8))
        return True
    else:
        return False




def Turn_On():
    CheckingImage = Folder+'\DFO_Turn_On.png'
    os.startfile(DFOFIle)
    tic = time.perf_counter()
    while True:
        toc = time.perf_counter()
        if IsThere(CheckingImage):
            Hold_On(10)
            return True
        elif toc-tic > TimeOut:
            return False

def Hold_On(s):
    time.sleep(s)

def TypeCapt(txt):
    MoveTo(captInput, 0.2)
    Hold_On(0.5)
    Click()
    Hold_On(0.3)
    Typing(txt)

def TypeID(ID):
    image = Folder+'\DFO_ID.png'
    MoveTo(image, 0.1)
    Hold_On(0.2)
    Click()
    Hold_On(0.2)
    Typing(ID)

def TypePassword(Password):
    image = Folder + '\DFO_Password.png'
    MoveTo(image, 0.1)
    Hold_On(0.2)
    Click()
    Hold_On(0.2)
    Typing(Password)

def MoveTo(Image, t):
    if pg.locateCenterOnScreen(Image, confidence = 0.90) is not None:
        y = pg.locateCenterOnScreen(Image, confidence=0.90).y
        x = pg.locateCenterOnScreen(Image, confidence=0.90).x
        pg.moveTo(x,y, t)
        return True
    else:
        return False

def SpelcialMoveTo(Im, t):
    print("IsIt")
    y = pg.locateCenterOnScreen(Im, confidence=0.6).y
    x = pg.locateCenterOnScreen(Im, confidence=0.6).x
    pd.moveTo(x,y, t)

def SpelcialMildMoveTo(Image, t):

    A = pg.locateCenterOnScreen(Image, confidence = 0.8)

    if A is not None:
        print("IsIt")
        y = A.y
        x = A.x
        pd.moveTo(x,y, t)



def Click():
    pg.mouseDown()
    Hold_On(0.2)
    pg.mouseUp()

def DoubleClick():
    pg.mouseDown()
    Hold_On(0.1)
    pg.mouseUp()
    Hold_On(0.05)
    pg.mouseDown()
    Hold_On(0.1)
    pg.mouseUp()

def IsLoggedIn():
    image = Folder + '\DFO_Play.png'
    tic = time.perf_counter()
    while True:
        toc = time.perf_counter()
        if IsThere(image):
            Hold_On(5)
            return True
        elif toc - tic > TimeOut:
            return False

def Log_In(ID, Password):
    if Turn_On():
        TypeID(ID)
        Hold_On(0.1)
        TypePassword(Password)
        Hold_On(0.1)
        Entering()
        Hold_On(3)
        if IsLoggedIn():
            image = Folder + '\DFO_Play.png'
            MoveTo(image, 0.05)
            Hold_On(0.1)
            Click()
            return True
    return False

def IsCharLoaded():
    image = Folder + '\Checking_Game_Loaded.png'
    tic = time.perf_counter()
    while True:
        toc = time.perf_counter()
        if IsThere(image):
            Hold_On(3)
            return True
        elif toc - tic > TimeOut:
            return False

def IsMapLoaded():
    image = Folder + '\DFO_Seria.png'
    image2 = Folder + '\ESC_Needed.png'
    tic = time.perf_counter()
    while True:
        toc = time.perf_counter()
        if IsThereMild(image):
            Hold_On(3)
            return True
        elif IsThereMild(image2):
            pd.keyDown("esc")
            Hold_On(0.1)
            pd.keyUp("esc")
        elif toc - tic > TimeOut:
            return False

def ClickFightingClub():
    image = Folder + '\DFO_Fighting_Club.PNG'
    image3 = Folder + '\DFO_Fighting_Club_Bigger.png'
    image2 = Folder + '\DFO_Dungeon1.PNG'
    while True:
        if IsThereMild(image) or IsThereMild(image3):
            Hold_On(3)
            pd.move(1,0, 0.1)
            SpelcialMoveTo(image, 1)
            SpelcialMoveTo(image3, 1)
            Hold_On(1)
            Click()
            Hold_On(1)
            DoubleClick()
        if IsThereMild(image2):
            return True

def FirstCharLogIn():
    while True:
        if IsCharLoaded():
            image = Folder + '\DFO_First_Char.png'
            MoveTo(image, 0)
            Hold_On(1)
            pg.move(0, 100, 1)
            Hold_On(1)
            DoubleClick()
            return True
    return False

def ReachToThePlace():
    time.sleep(3)
    pd.keyDown("down")
    time.sleep(15)
    pd.keyUp("down")
    time.sleep(0.3)
    pd.keyDown("right")
    image = Folder + '\DFO_Dungeon.png'
    while True:
        if IsThereMild(image):
            pd.keyUp("right")
            return True

def hold (key, hold_time):
    import time, pyautogui
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.press(key)

def WhereIsCharacter():
    Charimage = ""
    switch = False

    for i in range(0, 9):
        if IsThereVeryMild(vec[i]):
            Charimage = vec[i]
            switch = True
            break;
    if switch == True:
        SpelcialMildMoveTo(Charimage, 0)
    else:
        print("Cannot Find")



if TaskNumber == 1:
    if Log_In(IDVector[0], PasswordVector[0]):
        if FirstCharLogIn():
            if IsMapLoaded():
                if ReachToThePlace():
                    if ClickFightingClub():
                        print("Succed")



if TaskNumber == 2:
    Hold_On(3)
    pg.move(0, 100, 1)

if TaskNumber == 3:
    while True:
        WhereIsCharacter()

if TaskNumber == 4:
    image = Folder + '\TTL.png'
    solver = TwoCaptcha('8251ab8d5d4bb423e149e5718fe0b322')
    result = solver.normal(image)
    print(result)

def SkillUse(Skill_Index):
    pd.keyDown(Skill_Index)
    Hold_On(0.05)
    pd.keyUp(Skill_Index)
    Hold_On(0.05)

def SkillUseQWE():
    SkillUse("q")
    Hold_On(1)
    SkillUse("w")
    Hold_On(1)
    SkillUse("e")

def SkillUseAny():
    rn = random.randint(0, len(VecSkill) -1)
    SkillUse(VecSkill[rn])

def CharIndi():
    image = Folder + '\Char_Indicator.PNG'
    if (IsThereMild(image)):
        return True
    else:
        return False
    Hold_On(5)




def Dungeon_1():
    image = Folder + '\Dungeon-1.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_2_Before():
    image = Folder + '\Dungeon-2-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False

def Dungeon_3_Before():
    image = Folder + '\Dungeon-3-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_4_Before():
    image = Folder + '\Dungeon-4-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_5_Before():
    image = Folder + '\Dungeon-5-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_6_Before():
    image = Folder + '\Dungeon-6-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False

def Dungeon_7_Before():
    image = Folder + '\Dungeon-6-Before.PNG'
    if IsThere(image):
        return True
    else:
        return False


def Dungeon_2_After():
    image = Folder + '\Dungeon-2-After.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_3_After():
    image = Folder + '\Dungeon-3-After.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_4_After():
    image = Folder + '\Dungeon-4-After.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_5_After():
    image = Folder + '\Dungeon-5-After.PNG'
    if IsThere(image):
        return True
    else:
        return False
def Dungeon_6_After():
    image = Folder + '\Dungeon-6-After.PNG'
    if IsThere(image):
        return True
    else:
        return False

def Dungeon_Index(index, ba):
    image = Folder + '\Dungeon-' + index + '-' + ba + '.PNG'
    if IsThereMild(image):
        return True
    else:
        return False

def Dungeon_Run_1():
    while True:
        if Dungeon_1():
            pd.keyDown("right")
            break;
    while True:
        if Dungeon_2_Before():
            pd.keyUp("right")
            break;
    return True

def Dungeon_Fight_1():
    while True:
        SkillUseAny()
        if Dungeon_2_After() == True:
            return True

def Dungeon_Run_2():
    while True:
        if Dungeon_2_After():
            pd.keyDown("right")
            break;
    while True:
        if Dungeon_3_Before():
            pd.keyUp("right")
            break;
    return True

def Move_Slight_Right(s):
    pd.keyDown("right")
    Hold_On(s)
    pd.keyUp("right")


if TaskNumber == 9:
    while True:
        Move_Slight_Right(3)
        SkillUseAny()

if TaskNumber == 10:
    while True:
        print(Dungeon_3_After())


def ScreenShot():
    im = pyscreenshot.grab(bbox=(559, 490, 838, 567))
    image = Folder + '\capt.PNG'
    im.save(image)
    pyscreenshot.grab

def GetText():

    image = Folder + '\capt.png'
    solver = TwoCaptcha('8251ab8d5d4bb423e149e5718fe0b322')
    result = solver.normal(image)
    dictlist = []
    for key, value in result.items():
        dictlist.append(value)
    return dictlist[1]

def CaptBreak():

    if IsThereMild(captNoti):
        ScreenShot()
        Hold_On(0.3)
        TypeCapt(GetText())
        Hold_On(0.3)
        MoveTo(capt_OK, 0.1)
        Click()
        Hold_On(2)

if TaskNumber == 13:
    Hold_On(2)
    print(CaptBreak())

if TaskNumber == 14:
    Hold_On(2)
    while True:
        IsThereMild(captNoti)
        SpelcialMoveTo(captNoti, 0.1)


if TaskNumber == 6:
    while True:
        CaptBreak()
        Move_Slight_Right(1)
        if Dungeon_2_Before():
            break;
    while True:
        CaptBreak()
        SkillUseAny()
        if Dungeon_2_After():
            break;
    tic = time.perf_counter()
    while True:
        CaptBreak()
        toc = time.perf_counter()
        Move_Slight_Right(1)
        if Dungeon_3_Before():
            break;
        if toc-tic > 15:
            CaptBreak()
            pd.keyDown("up")
            pd.keyDown("left")
            Hold_On(0.4)
            pd.keyUp("up")
            pd.keyUp("left")
    while True:
        CaptBreak()
        SkillUseAny()
        if Dungeon_3_After():
            break;
    SwitchUp = False
    tic = time.perf_counter()
    while True:
        CaptBreak()
        toc = time.perf_counter()
        Move_Slight_Right(1)
        if Dungeon_4_Before():
            break;
        if toc-tic > 15:
            CaptBreak()
            pd.keyDown("up")
            pd.keyDown("left")
            Hold_On(0.2)
            pd.keyUp("up")
            pd.keyUp("left")
    while True:
        CaptBreak()
        SkillUseAny()
        if Dungeon_4_After():
            break;
    while True:
        CaptBreak()
        tic = time.perf_counter()
        Move_Slight_Right(1)
        if Dungeon_5_Before():
            break;
        if toc-tic > 15:
            CaptBreak()
            pd.keyDown("up")
            pd.keyDown("left")
            Hold_On(0.2)
            pd.keyUp("up")
            pd.keyUp("left")
    while True:
        CaptBreak()
        SkillUseAny()
        if Dungeon_5_After():
            break;
    while True:
        CaptBreak()
        tic = time.perf_counter()
        Move_Slight_Right(1)
        if Dungeon_6_Before():
            break;
        if toc-tic > 15:
            CaptBreak()
            pd.keyDown("down")
            pd.keyDown("right")
            Hold_On(0.2)
            pd.keyUp("down")
            pd.keyUp("right")
    while True:
        CaptBreak()
        SkillUseAny()
        if Dungeon_6_After():
            break;
    while True:
        CaptBreak()
        Move_Slight_Right(1)
        if Dungeon_7_Before():
            break;

if TaskNumber == 7:
    while True:
        print(Dungeon_2_Before())

if TaskNumber == 8:
    while True:
        print(Dungeon_1())


if TaskNumber == 5:
    Hold_On(3)
    while True:
        SkillUseAny()






if TaskNumber == 11:
    Hold_On(2)
    ScreenShot()

if TaskNumber == 12:
    while True:
        print(pg.position())

