#project by @abhinavkavuri
import tkinter
import os 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from gtts import gTTS
#from google import *
from PyDictionary import PyDictionary
import goslate
from numpy.distutils.fcompiler import none
dictionary=PyDictionary()
gl = goslate.Goslate()

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',' ':' ',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
    
CODE_REVERSED = {value:key for key,value in CODE.items()}



class Notepad:

    __root = Tk()

   
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisreadoutMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thismeaningMenu = Menu(__thisMenuBar, tearoff=0)
    
    
    __thistranslateMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisgsearchMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thismorseMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    
   
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None
    
    
    
    
    
    
    

    def __init__(self,**kwargs):

        
        try:
                self.__root.wm_iconbitmap("Notepad.ico") 
        except:
                pass

        

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        
        self.__root.title("Untitled - Notepad")

        
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
    
        
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
        
        
        top = (screenHeight / 2) - (self.__thisHeight /2) 
        
        
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                            self.__thisHeight,
                                            left, top)) 

       
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        
        self.__thisTextArea.grid(sticky = N + E + S + W)
        
        
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile) 
        
        
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)
        
       
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile) 

      
        self.__thisFileMenu.add_separator()                                         
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                    menu=self.__thisFileMenu)     
        
        
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)             
    
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
        
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
        
        self.__thisMenuBar.add_cascade(label="Edit",
                                    menu=self.__thisEditMenu)    
        
        
        
        self.__thisreadoutMenu.add_command(label="Read out in English",
                                        command=self.__readouten)    
        
        self.__thisreadoutMenu.add_separator()
        
        self.__thisreadoutMenu.add_command(label="Read out in Italian",
                                        command=self.__readoutit)
        self.__thisreadoutMenu.add_separator()
        
        self.__thisreadoutMenu.add_command(label="Read out in Chinese",
                                        command=self.__readoutch)
        self.__thisreadoutMenu.add_separator()
        
        self.__thisreadoutMenu.add_command(label="Read out in German",
                                        command=self.__readoutde)
        self.__thisreadoutMenu.add_separator()  
        
        self.__thisreadoutMenu.add_command(label="Read out in Spanish",
                                        command=self.__readoutes) 
        self.__thisreadoutMenu.add_separator() 
        
        self.__thisreadoutMenu.add_command(label="Read out in hindi",
                                        command=self.__readouthi) 
        self.__thisreadoutMenu.add_separator() 
        
        self.__thisMenuBar.add_cascade(label="Text to Speech",
                                    menu=self.__thisreadoutMenu)
        
        
        
        
        
        
        
        
        self.__thismeaningMenu.add_command(label="Find Meaning",
                                        command=self.__meaning)         
        
        self.__thisMenuBar.add_cascade(label="Dictionary",
                                    menu=self.__thismeaningMenu)
        
        
        
        
        
        
        
        self.__thistranslateMenu.add_command(label="Translate to English",
                                        command=self.__translatetoeng) 
        
        self.__thistranslateMenu.add_separator()
        
        self.__thistranslateMenu.add_command(label="Translate to Italian",
                                        command=self.__translatetoit)  
        self.__thistranslateMenu.add_separator()
        self.__thistranslateMenu.add_command(label="Translate to Chinese",
                                        command=self.__translatetoch)   
        self.__thistranslateMenu.add_separator()
        self.__thistranslateMenu.add_command(label="Translate to German",
                                        command=self.__translatetode) 
        self.__thistranslateMenu.add_separator()
        self.__thistranslateMenu.add_command(label="Translate to Hindi",
                                        command=self.__translatetohi)     
        self.__thistranslateMenu.add_separator()
        self.__thisMenuBar.add_cascade(label="Translate",
                                    menu=self.__thistranslateMenu)
         
        
        '''
        self.__thisgsearchMenu.add_command(label="Search on Google",
                                        command=self.__search)         
        
        self.__thisMenuBar.add_cascade(label="Goooooogle",
                                    menu=self.__thisgsearchMenu)'''
        
        
        '''self.__thismorseMenu.add_command(label="Translate to Morse",
                                        command=self.__tomorse)  '''
        self.__thismorseMenu.add_command(label="Translate from Morse",
                                        command=self.__frommorse)       
        
        self.__thisMenuBar.add_cascade(label="Morse",
                                    menu=self.__thismorseMenu)
        
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                    menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                 
        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Notepad","Notepad V1.0")
        
        
    def __meaning(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        
        mset=mytext.split(" ")
        mean=[]
        for x in mset:
            mean.append(dictionary.meaning(x))
            
        for j in mean:
            showinfo("Dictionary Meaning",j)
            
     
     
     
    def __translatetoeng(self):
        mytext = self.__thisTextArea.get("1.0",END)
        englishText = gl.translate(mytext,'en')
        showinfo("Translated to English",englishText)
              
         
    def __translatetoit(self):
        mytext = self.__thisTextArea.get("1.0",END)
        italianText = gl.translate(mytext,'it')
        showinfo("Translated to italian",italianText)     
        

    def __translatetoch(self):
        mytext = self.__thisTextArea.get("1.0",END)
        chineseText = gl.translate(mytext,'zh')
        showinfo("Translated to Chinese",chineseText)
     
 
    def __translatetode(self):
        mytext = self.__thisTextArea.get("1.0",END)
        germanText = gl.translate(mytext,'de')
        showinfo("Translated to English",germanText)
     

      
    def __translatetohi(self):
        mytext = self.__thisTextArea.get("1.0",END)
        hindiText = gl.translate(mytext,'hi')
        showinfo("Translated to hindi",hindiText) 
      
    '''def __search(self):
        mytext = self.__thisTextArea.get("1.0",END)
        for j in search(mytext, tld="co.in", num=10, stop=1, pause=2):
               print(j)'''
        
    ''' def __tomorse(self):
        mytext = self.__thisTextArea.get("1.0",END)
        print(mytext)
                
        rt=' '.join(CODE.get(i.upper()) for i in mytext)
        showinfo("Translated to Morse",rt)'''
    

    def __frommorse(self):
        mytext = self.__thisTextArea.get("1.0",END)
        tr=''.join(CODE_REVERSED.get(i) for i in mytext.split())
        showinfo("Translated to english from morse",tr)
        

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])

        if self.__file == "":
            
            self.__file = None
        else:
            
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
        
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
        
        
  
  
        
        
    def __readouten(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("eng.mp3")
        os.system("eng.mp3")
        
        
    def __readoutit(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'it'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("ita.mp3")
        os.system("ita.mp3")
            
    def __readoutch(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'zh'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("chi.mp3")
        os.system("chi.mp3")
    
    def __readoutde(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'de'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("ger.mp3")
        os.system("ger.mp3")
    
    def __readoutes(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'es'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("spa.mp3")
        os.system("spa.mp3")            
        
    def __readouthi(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        language = 'hi'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("hin.mp3")
        os.system("hin.mp3")    
      
      
        
          

    def __saveFile(self):

        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        self.__root.mainloop()




notepad = Notepad(width=600,height=400)
notepad.run()
