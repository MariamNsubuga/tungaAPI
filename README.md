# tungaAPI

instructions on how to run the project locally

cd test
You will find two folders bookface api and demo

#bookfaceapi
cd bookfaceapi

sudo apt install python3-venv

python3 -m venv venv
source venv env/bin/activate

pip install requirement.txt

python3 manage.py runserver

#demo
cd demo  
 
sudo apt install python3-venv

python3 -m venv venv
source venv env/bin/activate
cd crud
pip install requirement.txt

python3 manage.py runserver


the crud project has 3 apps that is events, api and todo