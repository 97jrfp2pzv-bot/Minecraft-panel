# Minecraft-panel
Управляйте своим майнкрафт севрером в панели!
## Возможности
- управление сервером локально
- отправка любой команды в консоль
- добавление своего сервера через форму
## фотокарточки
![фотокарточка номер 1](static/src1.png)
![фотокарточка номер 2](static/src2.png)
![фотокарточка номер 3](static/src3.png)
##  Зависимости:
- Python 3.14
- Django 
- mctools
## Установка
```bash
git clone https://github.com/97jrfp2pzv-bot/Minecraft-panel
cd Minecraft-panel
source venv/bin/activate
pip install django
pip install mc-tools
python manage.py migrate
python manage.py runserver


