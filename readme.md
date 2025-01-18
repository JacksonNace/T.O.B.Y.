if you want to boot this discord bot up follow the next 3 lines:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
deactivate



alternatively here are the libraries
pip install discord.py python-dotenv apscheduler
pip freeze > requirements.txt
deactivate


if you are using 3.13 python to clone it doesnt have the required library for audioop
pip install audioop-lts 
install it manually ^