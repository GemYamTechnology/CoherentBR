@echo off
ECHO.%Path:;= & ECHO.%
ECHO.%Path:;= & ECHO.%
pause

set $env=%Path%;C:\Python27\;C:\Python27\Scripts\;
setx /m Path "%$env%"
ECHO.%Path:;= & ECHO.%
pause

set $env1=%Path%;C:\Prongram Files\Python36\;C:\Prongram Files\Python36\Scripts\
setx /m Path "%$env1%"
ECHO.%Path:;= & ECHO.%
pause

cd /d C:\Program Files\Python36\
move python.exe python3.exe

call .\AutoPip.bat
