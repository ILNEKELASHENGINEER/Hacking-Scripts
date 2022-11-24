echo Hi do you love me (yes or no)!!!
set /p love=
if %love%==yes goto love
if %love%==no goto hate
:love
echo i love you too...
echo Meet you soon :)
pause
exit
:hate
echo But I LOVE YOU...hehe eh eh
echo you are hacked...
echo Your Pc will crash in 5 seconds
timeout 5
shutdown -s -t 50
