import Swamipp as Swami
import os,datetime
import _thread, sys

directory="C:/Swamipp/Programs/"

class repl():
    def __init__(self):
        print("\n=========Restart=========")
        print("Swami++ 2.9.2, type credits for more info")
    def start(self):
        while 1:
            text=input("Swami++ > ")
            if text.strip()=="":
                continue
            if text=="exit":
                break
            try:
                result,error=Swami.run("<Shell>",text)
            except KeyboardInterrupt:
                continue
            if error:
                print(error.toString())
            elif result:
                if len(result.elements)==1:
                    print(repr(result.elements[0]))
                else:
                    for i in result.elements:
                        print(repr(i))
