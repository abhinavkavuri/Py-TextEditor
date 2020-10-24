@echo off
pyinstaller texteditor.py --onefile
RMDIR /S /Q C:\Users\Clay\Clay\Python\Monsoon\build
del C:\Users\Clay\Clay\Python\Monsoon\texteditor.spec
REM cd dist
REM cd C:\Program Files (x86)\Resource Hacker\
REM ResourceHacker.exe -open C:\Users\Clay\Clay\Python\Monsoon\dist\texteditor.exe -save texteditor.exe -action addoverwrite -res C:\Users\Clay\Clay\Python\Py-TextEditor\MonsoonLogo.ico -mask ICONGROUP,MAINICON,
