@echo off
cd ..\CoherentBR_Virtual_Environment\Scripts

easy_install pip
pip install --upgrade pip --force-reinstall
pip install pip --upgrade
pause

pip -V
pause

pip install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysql-python mysqlclient cobs PyMySQL
pip install ..\CoherentBRAutoInstall\mysqlclient-1.3.12-cp27-cp27m-win_amd64.whl
pause

pip install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysqlclient cobs PyMySQL --upgrade
pause
