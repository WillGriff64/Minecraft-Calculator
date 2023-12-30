from tkinter import *
import math

root= Tk()
root.title("The Minecraft Calculator")
root.geometry("300x400")
root.resizable(False, False) 

def mainMenu():
    for i in root.grid_slaves():
        i.destroy()
        
    mainFrame = LabelFrame(root)
    mainFrame.grid(row=0,column=0)
    title = Label(mainFrame, text="Minecraft Calculator",font=("Courier New",15)).grid(row=0,column=0,padx=26)

    NPortalMenu = Button(mainFrame,text="Nether Portal Calculator",font=("Courier New",10),bd=5,command=lambda:portalCalc())
    NPortalMenu.grid(row=2,column=0,sticky=W)

    StronholdFinderButton = Button(mainFrame,text="Stronhold Finder",font=("Courier New",10),bd=5,command=StrongholdFinder)
    StronholdFinderButton.grid(row=3,column=0,sticky=W)

    ItemCounterButton = Button(mainFrame,text="Item Counter",font=("Courier New",10),bd=5,command=ItemCounter)
    ItemCounterButton.grid(row=4,column=0,sticky=W)

    mainFrame.grid_rowconfigure(1, minsize=15)

def portalCalc():

    def calculatePortal():

        try:
            ovx = int(OxInput.get())
            nex = int(ovx/8)
            NxInput.delete(0, END)
            NxInput.insert(INSERT,str(nex))
        except:
            try:
                nex = int(NxInput.get())
                ovx = nex*8
                OxInput.delete(0, END)
                OxInput.insert(INSERT,str(ovx))
            except:
                pass
        try:
            ovy = int(OyInput.get())
            NyInput.delete(0, END)
            NyInput.insert(INSERT,str(ovy))
        except ValueError:
            try:
                ney = int(NyInput.get())
                OyInput.delete(0, END)
                OyInput.insert(INSERT,str(ney))
            except:
                pass
        try:
            ovz = int(OzInput.get())
            nez = int(ovz/8)
            NzInput.delete(0, END)
            NzInput.insert(INSERT,str(nez))
        except ValueError:
            try:
                nez = int(NzInput.get())
                ovz = nez*8
                OzInput.delete(0, END)
                OzInput.insert(INSERT,str(ovz))
            except:
                pass

    def clearall():
        OxInput.delete(0, END)
        OyInput.delete(0, END)
        OzInput.delete(0, END)
        NxInput.delete(0, END)
        NyInput.delete(0, END)
        NzInput.delete(0, END)
    
    for i in root.grid_slaves():
        i.destroy()
        
    Frame = LabelFrame(root)
    Frame.grid(row=0,column=0)

    title = Label(Frame, text="Nether Portal\nCoord Calculator",font=("Courier New",15)).grid(row=0,column=0,padx=50,columnspan=6)

    OverworldTitle = Label(Frame, text="Overworld",font=("Courier New bold",10)).grid(row=2,column=0,sticky=W,columnspan=2)

    NetherTitle = Label(Frame, text="Nether",font=("Courier New bold",10)).grid(row=2,column=2,sticky=W,columnspan=2)
    
    OxLabel = Label(Frame, text="X",font=("Courier New",10)).grid(row=3,column=0,sticky=W)
    OxInput = Entry(Frame)
    OxInput.grid(row=3,column=1,sticky=W)

    OyLabel = Label(Frame, text="Y",font=("Courier New",10)).grid(row=4,column=0,sticky=W)
    OyInput = Entry(Frame, width=20)
    OyInput.grid(row=4,column=1,sticky=W)

    OzLabel = Label(Frame, text="Z",font=("Courier New",10)).grid(row=5,column=0,sticky=W)
    OzInput = Entry(Frame, width=20)
    OzInput.grid(row=5,column=1,sticky=W)

    NxLabel = Label(Frame, text="X",font=("Courier New",10)).grid(row=3,column=2,sticky=W)
    NxInput = Entry(Frame)
    NxInput.grid(row=3,column=3,sticky=W)

    NyLabel = Label(Frame, text="Y",font=("Courier New",10)).grid(row=4,column=2,sticky=W)
    NyInput = Entry(Frame, width=20)
    NyInput.grid(row=4,column=3,sticky=W)

    NzLabel = Label(Frame, text="Z",font=("Courier New",10)).grid(row=5,column=2,sticky=W)
    NzInput = Entry(Frame, width=20)
    NzInput.grid(row=5,column=3,sticky=W)

    Confirm = Button(Frame,text="Calculate Coords",font=("Courier New",10),bd=5,command=calculatePortal)
    Confirm.grid(row=6,column=0,columnspan=2,sticky=W)

    ClearButton = Button(Frame,text="Clear All",font=("Courier New",10),bd=5,command=clearall)
    ClearButton.grid(row=6,column=2,columnspan=2,sticky=E)

    back = Button(root,text="Back",font=("Courier New",8),bd=5,command=lambda:mainMenu())
    back.grid(row=999,column=0,sticky=W,columnspan=2)

    Frame.grid_rowconfigure(1, minsize=15)
    Frame.grid_rowconfigure(6, minsize=15)


def StrongholdFinder():

    def CalculateCoords():

        try:
            X1 = float(X1Input.get())
            Z1 = float(Z1Input.get())
            A1 = float(A1Input.get())

            X2 = float(X2Input.get())
            Z2 = float(Z2Input.get())
            A2 = float(A2Input.get())

            OY = (Z1*math.tan(-A1*(math.pi/180))-Z2*math.tan(-A2*(math.pi/180))+X2-X1)/(math.tan(-A1*(math.pi/180))-math.tan(-A2*(math.pi/180)))
            
            OX = (OY - Z1)*math.tan(-A1*(math.pi/180))+X1

            OXEntry.delete(0, END)
            OXEntry.insert(INSERT,str(OX))
            
            OYEntry.delete(0, END)
            OYEntry.insert(INSERT,str(OY))
            
        except:
            pass

    def clearall():
        X1Input.delete(0, END)
        Z1Input.delete(0, END)
        A1Input.delete(0, END)
        X2Input.delete(0, END)
        Z2Input.delete(0, END)
        A2Input.delete(0, END)
        OXEntry.delete(0, END)
        OYEntry.delete(0, END)

    for i in root.grid_slaves():
        i.destroy()
        
    Frame = LabelFrame(root)
    Frame.grid(row=0,column=0)

    title = Label(Frame, text="Stronghold\nTriangulator",font=("Courier New",15)).grid(row=0,column=0,padx=74,columnspan=6)

    OverworldTitle = Label(Frame, text="Position 1",font=("Courier New bold",10)).grid(row=2,column=0,sticky=W,columnspan=2)

    NetherTitle = Label(Frame, text="Position 2",font=("Courier New bold",10)).grid(row=2,column=2,sticky=W,columnspan=2)
    
    X1Label = Label(Frame, text="X",font=("Courier New",10)).grid(row=3,column=0,sticky=W)
    X1Input = Entry(Frame)
    X1Input.grid(row=3,column=1,sticky=W)

    Z1Label = Label(Frame, text="Z",font=("Courier New",10)).grid(row=4,column=0,sticky=W)
    Z1Input = Entry(Frame, width=20)
    Z1Input.grid(row=4,column=1,sticky=W)

    A1Label = Label(Frame, text="θ",font=("Courier New",10)).grid(row=5,column=0,sticky=W)
    A1Input = Entry(Frame, width=20)
    A1Input.grid(row=5,column=1,sticky=W)

    X2Label = Label(Frame, text="X",font=("Courier New",10)).grid(row=3,column=2,sticky=W)
    X2Input = Entry(Frame, width=20)
    X2Input.grid(row=3,column=3,sticky=W)

    Z2Label = Label(Frame, text="Z",font=("Courier New",10)).grid(row=4,column=2,sticky=W)
    Z2Input = Entry(Frame, width=20)
    Z2Input.grid(row=4,column=3,sticky=W)

    A2Label = Label(Frame, text="θ",font=("Courier New",10)).grid(row=5,column=2,sticky=W)
    A2Input = Entry(Frame, width=20)
    A2Input.grid(row=5,column=3,sticky=W)

    OXLabel = Label(Frame, text="X",font=("Courier New",10)).grid(row=7,column=0,sticky=W)
    OXEntry = Entry(Frame, width=20)
    OXEntry.grid(row=7,column=1,sticky=W)

    OYLabel = Label(Frame, text="Y",font=("Courier New",10)).grid(row=7,column=2,sticky=W)
    OYEntry = Entry(Frame, width=20)
    OYEntry.grid(row=7,column=3,sticky=W)

    Confirm = Button(Frame,text="Calculate Coords",font=("Courier New",10),bd=5,command=CalculateCoords)
    Confirm.grid(row=8,column=0,columnspan=2,sticky=W)
    
    ClearButton = Button(Frame,text="Clear All",font=("Courier New",10),bd=5,command=clearall)
    ClearButton.grid(row=8,column=2,columnspan=2,sticky=E)
    
    back = Button(root,text="Back",font=("Courier New",8),bd=5,command=lambda:mainMenu())
    back.grid(row=1,column=0,sticky=W,columnspan=2)

    Frame.grid_rowconfigure(1, minsize=15)
    Frame.grid_rowconfigure(6, minsize=15)


def ItemCounter():

    def CalculateAmount():
        chests = 0
        stacks = 0
        items = 0

        try:
            total = int(TotInput.get())
            print(total)
            while True:
                if total >= 1728:
                    total -= 1728
                    chests += 1
                else:
                    break

            while True:
                if total >= 64:
                    total -= 64
                    stacks += 1
                else:
                    break

            items = total
            ChInput.delete(0, END)
            ChInput.insert(INSERT,str(chests))

            StInput.delete(0, END)
            StInput.insert(INSERT,str(stacks))

            ItInput.delete(0, END)
            ItInput.insert(INSERT,str(items))
            
        except:
            try:
                chests = ChInput.get()
                stacks = StInput.get()
                items = ItInput.get()

                if chests == "":
                    chests = 0

                if stacks == "":
                    stacks = 0

                if items == "":
                    items = 0

                chests,stacks,items = int(chests),int(stacks),int(items)

                total = (chests*1728)+(stacks*64)+items
                TotInput.delete(0, END)
                TotInput.insert(INSERT,str(total))

            except:
                print("a")
                pass

    def clearAll():
        ChInput.delete(0, END)
        StInput.delete(0, END)
        ItInput.delete(0, END)
        TotInput.delete(0, END)
        
        

    for i in root.grid_slaves():
        i.destroy()
        
    Frame = LabelFrame(root)
    Frame.grid(row=0,column=0)

    title = Label(Frame, text="Item Counter",font=("Courier New",15)).grid(row=0,column=0,padx=74,columnspan=6)

    ChLabel = Label(Frame, text="Chests",font=("Courier New",10)).grid(row=3,column=0,sticky=W)
    ChInput = Entry(Frame, width=30)
    ChInput.grid(row=3,column=1,sticky=W,columnspan=3)

    StLabel = Label(Frame, text="Stacks",font=("Courier New",10)).grid(row=4,column=0,sticky=W)
    StInput = Entry(Frame, width=30)
    StInput.grid(row=4,column=1,sticky=W,columnspan=3)

    ItLabel = Label(Frame, text="Items ",font=("Courier New",10)).grid(row=5,column=0,sticky=W)
    ItInput = Entry(Frame, width=30)
    ItInput.grid(row=5,column=1,sticky=W,columnspan=3)

    TotLabel = Label(Frame, text="Total ",font=("Courier New",10)).grid(row=7,column=0,sticky=W)
    TotInput = Entry(Frame, width=30)
    TotInput.grid(row=7,column=1,sticky=W,columnspan=3)

    Confirm = Button(Frame,text="Calculate Amounts",font=("Courier New",10),bd=5,command=CalculateAmount)
    Confirm.grid(row=8,column=0,columnspan=3,sticky=W)

    ClearButton = Button(Frame,text="Clear All",font=("Courier New",10),bd=5,command=clearAll)
    ClearButton.grid(row=8,column=3,sticky=E)

    back = Button(root,text="Back",font=("Courier New",8),bd=5,command=lambda:mainMenu())
    back.grid(row=999,column=0,sticky=W,columnspan=2)

    Frame.grid_rowconfigure(1, minsize=15)
    Frame.grid_rowconfigure(6, minsize=15)

















mainMenu()

root.mainloop()
