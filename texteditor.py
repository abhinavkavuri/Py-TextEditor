#project by @abhinavkavuri
import tkinter
import tkinter as tk
import os,_thread,subprocess,REPL,multiprocessing,threading,sys
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
locations=open("Compilers.txt","r").read().split("\n")
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

print("Monsoon IDE Version 1.6.1")

class Terminal(threading.Thread):
    def __init__(self,*args,**kwargs):
        super(Terminal,self).__init__(*args,**kwargs)
        self._stop_event=threading.Event()
    def stop(self):
        self._stop_event.set()
        #raise KeyboardInterrupt
        sys.exit()
    def stopped(self):
        return self._stop_event.is_set()
    def run(self):
        print("Console Type Undefined")
class SPPTerminal(Terminal):
    def run(self):
        r=REPL.repl()
        r.start()
#class PyTerminal:
    #def run(self):
        #subprocess.Popen('C:/Users/Clay/AppData/Local/Programs/Python/Python38/python.exe')

console=Terminal()

#console.start()
#def terminal():
    #r=REPL.repl()
    #r.start()

#console=multiprocessing.Process(target=terminal,args=())
#console.
#os.fork()
#console.start()
class CustomText(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self,*args,**kwargs)
    def _proxy(self, command, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result    

        return result
    def highlight_pattern(self,pattern, tag,start="1.0",end="end",regexp=False):
        #print("running")
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)
        count = tkinter.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)
class Notepad:
    
    __root = Tk()
    
    #__root.bind("<Control-S>",saveFile)
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = CustomText(__root,bg="#222",fg="#fff",cursor="xterm white black",insertbackground="#eee",undo=True)
    #__thisTextArea.insert("1.0","int")
    #__thisLineNumbers=TextLineNumbers()
    #__thisLineNumbers.attach(__thisTextArea)
     
    '''__thisTextArea.tag_configure('red', foreground = 'red')
    __thisTextArea.tag_configure('purple', foreground = '#a820a1')
    __thisTextArea.bind('<<TextModified>>', __textchanged__)
    #__thisTextArea.highlight_pattern("int","blue")'''
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisreadoutMenu = Menu(__thisMenuBar, tearoff=0)
    
    #__thismeaningMenu = Menu(__thisMenuBar, tearoff=0)
    __thisoptionsMenu=Menu(__thisMenuBar,tearoff=0)
    
    __thistranslateMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisgsearchMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thismorseMenu = Menu(__thisMenuBar, tearoff=0)
    
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    
   
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None
    
    
    
    
    
    
    
    
    def __init__(self,**kwargs):
        self.changed=False
        self.comp=""
        self.__thisTextArea.bind("<Delete>",self.__textchanged__)
        self.__thisTextArea.bind('<Key>', self.__textchanged__)
        self.__root.bind("<Control-s>",self.saveFile)
        self.__root.bind("<F5>",self.runCode)
        self.__thisTextArea.bind("<Return>",self.autoindent)
        self.__thisTextArea.tag_configure("red",foreground='#ed5576')
        self.__thisTextArea.tag_configure("purple",foreground="#9340ff")
        self.__thisTextArea.tag_configure("orange",foreground="#fd6a02")
        self.__thisTextArea.tag_configure("blue",foreground="#647afa")
        #self.linenumbers = TextLineNumbers(self.__root,width=30)
        #self.linenumbers.attach(self.__thisScrollBar)
        
        #self.linenumbers = Text(self.__thisTextArea, width=3)
        #self.linenumbers.grid(row=__textrow, column=__linenumberscol, sticky=NS)
        #self.linenumbers.config(font=self.__myfont)
        #self.__thisTextArea.bind("<Return>",self.__thisLineNumbers.redraw)   
        try:
                self.__root.wm_iconbitmap("MonsoonLogo.ico") 
        except:
                pass
        #self.__thisTextArea.bind('<<TextModified>>', self.__textchanged__)
        

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        
        self.__root.title("Untitled - Monsoon")

        
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
    
        
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
        
        
        top = (screenHeight / 2) - (self.__thisHeight /2) 
        
        
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                            self.__thisHeight,
                                            left, top)) 

       
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        #self.linenumbers.pack(side="left",fill="y")
        #self.__thisTextArea.pack(side="left",fill="y")
        self.__thisTextArea.grid(column=0,sticky = N + E + S + W)
        
        
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
        
        
        
        
        
        
        
        
        #self.__thismeaningMenu.add_command(label="Find Meaning",
                                        #command=self.__meaning)         
        
        #self.__thisMenuBar.add_cascade(label="Dictionary",
                                    #menu=self.__thismeaningMenu)
        
        
        self.__thisoptionsMenu.add_command(label="Save Executions",command=self.saveexec)
        #self.__thisoptionsMenu.add_command(label="Delete Executions",command=self.delexec)
        self.__thisMenuBar.add_cascade(label="Options",menu=self.__thisoptionsMenu)
        self.saveExe=False
        
        
        
        
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
        self.__thismorseMenu.add_command(label="Begin SPP REPL",
                                        command=self._executerepl)
        #self.__thismorseMenu.add_command(label="Begin Python REPL",
                                        #command=self._executepyrepl)
        self.__thismorseMenu.add_command(label="Execute SPP",
                                        command=self._execute)
        self.__thismorseMenu.add_command(label="Execute C++",
                                        command=self._executecpp)
        self.__thismorseMenu.add_command(label="Execute Python",
                                        command=self._executepy) 
        self.__thismorseMenu.add_command(label="Execute C",
                                        command=self._executec)      
        
        self.__thisMenuBar.add_cascade(label="Execute",
                                    menu=self.__thismorseMenu)
        
        self.__thisHelpMenu.add_command(label="About Monsoon",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                    menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                 
        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    def _on_change(self, event):
        self.linenumbers.redraw()
    def __textchanged__(self,event):
        if not event:pass
        elif event.char.lower() in list("qwertyuiop[]{}|\\asdfghjkl;:'\"zxcvbnm,./<>?1234567890-_+=!@#$%^&*()\t\n\r\x08 `~"):
            self.changed=True
        
            self.title_change()
        else:
            #print(repr(event.char))
            pass
        '''self.__thisTextArea.highlight_pattern("int","blue")
        self.__thisTextArea.highlight_pattern("string","blue")
        self.__thisTextArea.highlight_pattern("float","blue")
        self.__thisTextArea.highlight_pattern("double","blue")
        self.__thisTextArea.highlight_pattern("str","orange")'''
        if not self.__file:
            return
        elif self.__file.endswith(".cpp"):
            self.__thisTextArea.highlight_pattern("(int |bool |string |float |char| double |int\(|string\(|float\(|double\(|char\(|bool\()","blue",regexp=True)
            self.__thisTextArea.highlight_pattern("(while |for | in |class |if |else |\|\||&|include|from |try |catch |cout |cin|endl|return|using |namespace |void |break|continue)","red",regexp=True)
            self.__thisTextArea.highlight_pattern("(\d+(.\d)?)","orange",regexp=True)
            self.__thisTextArea.highlight_pattern("(\+|-|\*|/|\^|<|>|==|!=|<=|>)","purple",regexp=True)
        elif self.__file.endswith(".spp"):
            self.__thisTextArea.highlight_pattern("(let | and | or |not |if |then|elif |else |while |for |to |step |func |end|continue|return|break|each|do |class |print\(|println\(|import\()","red",regexp=True)
            self.__thisTextArea.highlight_pattern("(string\(|float\()","blue",regexp=True)
            self.__thisTextArea.highlight_pattern("(\d+(.\d)?)","orange",regexp=True)
            self.__thisTextArea.highlight_pattern("(\+|-|\*|/|\^|<|>)","purple",regexp=True)
        elif self.__file.endswith(".py"):
            self.__thisTextArea.highlight_pattern("(string\(|float\()","blue",regexp=True)
            self.__thisTextArea.highlight_pattern("(and | or |not |if |elif |else |while |for |to |step |def |continue|return|break|class |print\(|assert |del |try |except|global |local |nonlocal |is|lambda |with |pass|from|import )","red",regexp=True)
            self.__thisTextArea.highlight_pattern("(\d+(.\d)?)","orange",regexp=True)
            self.__thisTextArea.highlight_pattern("(\+|-|\*|/|\^|<|>)","purple",regexp=True)
        elif self.__file.endswith(".c"):
            self.__thisTextArea.highlight_pattern("(int |bool |string |float |char| double |int\(|string\(|float\(|double\(|char\(|bool\()","blue",regexp=True)
            self.__thisTextArea.highlight_pattern("(while |for | in |class |if |else | or | and |include|from |try |catch |printf\(|endl|return|using |namespace )","red",regexp=True)
            self.__thisTextArea.highlight_pattern("(\d+(.\d)?)","orange",regexp=True)
            self.__thisTextArea.highlight_pattern("(\+|-|\*|/|\^|<|>)","purple",regexp=True)
        #self.__thisTextArea.highlight_pattern("int|string|float","red",regexp=True) 
    def saveexec(self):
        self.saveExe= not self.saveExe
        self.__thisoptionsMenu.delete(0)
        if self.saveExe:
            self.__thisoptionsMenu.add_command(label="Delete Executions",command=self.saveexec)
        else:
            self.__thisoptionsMenu.add_command(label="Save Executions",command=self.saveexec)
    #def delexec(self):
        #self.saveExe=False
    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Monsoon","Monsoon V1.0")
        
        
    def __meaning(self):
        
        mytext = self.__thisTextArea.get("1.0",END)
        
        mset=mytext.split(" ")
        mean=[]
        for x in mset:
            mean.append(dictionary.meaning(x))
            
        for j in mean:
            showinfo("Dictionary Meaning",j)
            
    def exec_cmd(self,path,compiler="",restart=True,exec_path=False):
        global console
        if console.is_alive():
            console.stop()
        if restart:
            print("\n=========Restart=========")
        if exec_path:
            os.system(path)
            return
        #subprocess.call(path,shell=True)
        folder = ""
        temp=""
        for i in path:
            if i != "/":
                temp+=i
            else:
                temp += i
                folder += temp
                temp=""
        #print(folder)
        os.system(f"cd {folder} && "+compiler+" "+path)
        #os.system()
        #console=Terminal()
        #console.start()
        #console=multiprocessing.Process(target=terminal,args=())
        #console.start()
    def runCode(self,event=None):
        global locations
        #print(self.comp)
        if self.comp=="spp":
            if self.__file:
                compiler=locations[2]
                path=self.__file
                t1=threading.Thread(target=self.exec_cmd,args=(path,compiler))
                t1.start()
                t1.join()
        elif self.comp=="cpp":
            if self.__file:
                #print("file")
                folder = ""
                temp=""
                for i in self.__file:
                    if i != "/":
                        temp+=i
                    else:
                        temp += i
                        folder += temp
                        temp=""
                #end=self.__file.strip(".cpp")+".exe"
                end=folder+"a.exe"
                print(end)
                compiler=locations[0]
                path=self.__file#+f" && {end}"
                t1=threading.Thread(target=self.exec_cmd,args=("echo Building...","",True,True))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=(path,compiler,False))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=("echo Running...","",False,True))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=(end,"",False,True))
                t1.start()
                t1.join()
                try:
                    if not self.saveExe:
                        os.remove(end)
                    else:
                        name = path.replace(".cpp",".exe")
                        p=path.split("/")[-1].replace(".cpp",".exe")
                        #print(f"cd {folder} & rename a.exe {p}")
                        if os.path.isfile((r:=path.replace(".cpp",".exe"))):
                            os.remove(r)
                        t1=threading.Thread(target=self.exec_cmd,args=(f"cd {folder} & rename a.exe {p}","",False,True))
                        t1.start()
                        t1.join()
                except KeyboardInterrupt as e:
                    print("Error Running or Compiling...")
                    #print(e)
                else:
                    t1=threading.Thread(target=self.exec_cmd,args=("echo Complete...","",False,True))
                    t1.start()
                    t1.join()
        elif self.comp=="c":
            if self.__file:
                #print("file")
                folder = ""
                temp=""
                for i in self.__file:
                    if i != "/":
                        temp+=i
                    else:
                        temp += i
                        folder += temp
                        temp=""
                #end=self.__file.strip(".cpp")+".exe"
                end=folder+"a.exe"
                #print(end)
                compiler=locations[3]
                path=self.__file#+f" && {end}"
                t1=threading.Thread(target=self.exec_cmd,args=("echo Building...","",True,True))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=(path,compiler,False))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=("echo Running...","",False,True))
                t1.start()
                t1.join()
                t1=threading.Thread(target=self.exec_cmd,args=(end,"",False,True))
                t1.start()
                t1.join()
                try:
                    if not self.saveExe:
                        os.remove(end)
                    else:
                        name = path.replace(".c",".exe")
                        p=path.split("/")[-1].replace(".c",".exe")
                        #print(f"cd {folder} & rename a.exe {p}")
                        if os.path.isfile((r:=path.replace(".c",".exe"))):
                            os.remove(r)
                        t1=threading.Thread(target=self.exec_cmd,args=(f"cd {folder} & rename a.exe {p}","",False,True))
                        t1.start()
                        t1.join()
                except:
                    print("Error Running or Compiling...")
                else:
                    t1=threading.Thread(target=self.exec_cmd,args=("echo Complete...","",False,True))
                    t1.start()
                    t1.join()
        elif self.comp=="py":
            if self.__file:
                compiler=locations[1]
                path=self.__file
                _thread.start_new_thread(self.exec_cmd,(path,compiler))
            #os.syste m()
        
                
    def _execute(self):
        self.comp="spp"
        _thread.start_new_thread(self.runCode,())
        
    def _executerepl(self):
        global console
        console=SPPTerminal()
        console.start()
    def _executecpp(self):
        self.comp="cpp"
        _thread.start_new_thread(self.runCode,())
        #print("done")
    def _executec(self):
        self.comp="c"
        _thread.start_new_thread(self.runCode,())
    def _executepy(self):
        self.comp="py"
        _thread.start_new_thread(self.runCode,())
        
    def autoindent(self, event):
        """
            this method implements the callback for the Return Key in the editor widget.
            arguments: the tkinter event object with which the callback is associated
        """
        indentation = ""
        lineindex = self.__thisTextArea.index("insert").split(".")[0]
        linetext = self.__thisTextArea.get(lineindex+".0", lineindex+".end")
        self.changed=True
        self.title_change()
        for character in linetext:
            if character in [" ","\t"]:
                indentation += character
            else:
                break
                
        self.__thisTextArea.insert(self.__thisTextArea.index("insert"), "\n"+indentation)
        return "break"        
    def _executepyrepl(self):
        if self.__file:
            path=""
            _thread.start_new_thread(self.exec_cmd,(path,))
            #os.syste m()
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
            
            self.__root.title(os.path.basename(self.__file) + " - Monsoon")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())
            self.__textchanged__(None)
            file.close()
            self.changed=False
            self.title_change()

        
        
    def __newFile(self):
        self.__root.title("Untitled - Monsoon")
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
      
      
        
          
    def title_change(self):
        if self.__file:
            #print(self.changed)
            if self.changed:
                self.__root.title(os.path.basename(self.__file)+" - Monsoon*")
            else:
                self.__root.title(os.path.basename(self.__file)+" - Monsoon")
        else:
            if self.changed:
                self.__root.title("Untitled - Monsoon*")
            else:
                self.__root.title("Untitled - Monsoon")
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
                self.__root.title(os.path.basename(self.__file) + " - Monsoon")
                
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
            self.__root.title(os.path.basename(self.__file) + " - Monsoon")
        #self.changed=False
        #self.title_change()
        
    def saveFile(self,event):
        #print("Saving")
        self.__saveFile()
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
if console.is_alive():
    console.stop()

