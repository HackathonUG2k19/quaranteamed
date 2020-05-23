!!!!!!!!!!NOTE!!!!!!!!!!!!!!!!!!!!
PLease use this for updating your local repo
```
git remote add orig https://github.com/orientor/lost-found.git
git pull --rebase orig master
```

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/orientor/lost-found.git
cd lost-found
```

Make virtualenv
```
pip3 install virtualenv
virtualenv env
source env/bin/activate
```
Install Dependencies 

```
pip3 install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Run site
```
python3 manage.py runserver
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 

#### That's it! Happy Coding!
