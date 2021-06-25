@ECHO OFF

pyinstaller --onefile -w src/formbuilder.py > nul

SET HOUR=%time:~0,2%
SET dtStamp9=%date:~-4%%date:~4,2%%date:~7,2%_0%time:~1,1%%time:~3,2%%time:~6,2%
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%

if "%HOUR:~0,1%" == " " (SET dtStamp=%dtStamp9%) else (SET dtStamp=%dtStamp24%)

set projdir=..\%dtStamp%_docbuilder_bin
set bindir=%projdir%\bin

mkdir %bindir%

mv dist\formbuilder.exe %bindir%
rmdir /s /q build\
rmdir /s /q dist\
del /s /q formbuilder.spec

robocopy in\ %projdir%\in /MIR /FFT /R:3 /W:10 /Z /NP /NDL > nul
robocopy res\ %projdir%\res /MIR /FFT /R:3 /W:10 /Z /NP /NDL > nul
robocopy out\ %projdir%\out /MIR /FFT /R:3 /W:10 /Z /NP /NDL > nul
robocopy .\ %projdir% *.md /FFT /R:3 /W:10 /Z /NP /NDL > nul
robocopy .\ %projdir% *.yaml /FFT /R:3 /W:10 /Z /NP /NDL > nul

echo "bin\formbuilder.exe -c config.yaml" > %projdir%\Zapolnyator_3000.cmd
