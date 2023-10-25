set echo on
set ENV_HOME='D:\Shamil\ChatGPT\venv'
call $ENV_HOME/Scripts/activate.bat

call dir 
echo 'Hello '
pip install --upgrade pip
rem pip install -U g4f

python main.py

