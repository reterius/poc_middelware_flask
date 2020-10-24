1) cd poc_middelware_flask
2) python3 -m venv venv
3) pip install -r rewuirements.txt
4) python3 app.py

Fort test:

$ curl -u Tony:IamBatMan http://localhost:5000
Authorization failed

$ curl -u admin:1234 http://localhost:5000
Hi Mehmet