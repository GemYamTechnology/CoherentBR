@echo off
python -m easy_install pip
python -m pip install --upgrade pip --force-reinstall
python -m pip install pip --upgrade

python3 -m easy_install pip
python3 -m pip install --upgrade pip --force-reinstall
python3 -m pip install pip --upgrade
pause

pip -V
pip3 -V
pause

python -m pip install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysqlclient
python3 -m pip3 install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysqlclient
python -m pip install mysqlclient-1.3.12-cp27-cp27m-win_amd64.whl
python3 -m pip3 install mysqlclient-1.3.12-cp36-cp36m-win_amd64.whl
pause

pip install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysqlclient --upgrade
pip3 install numpy scipy matplotlib pandas sympy nose scikit-learn virtualenv ipython jupyter mysqlclient --upgrade
pause
