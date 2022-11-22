# django-mysql.github.io
This is a basic login and register System which is Implemented by mySql database.
To run this,<br/>
->Activate Virtual Environment ("venv\Scripts\activate")<br/>
->create a table("tab") in mySql database("loginsys")<br/>
->now, Connect using " pip install mysql-connector-python " it will connect to our database<br/>
->run "python manage.py makemigrations"<br/>
->run "python manage.py migrate"<br/>
->run "python manage.py runserver"<br/>
now, it will give like this (Starting development server at http://127.0.0.1:8000/)<br/>
open that link.<br/><br>
It will ask for register<br/>
<img src="ScreenShots/Register.png" height="300" width="600">
<br/><br/>
Before Entering details, The database is:<br/>

<img src="ScreenShots/pre.png" height="300" width="600">

<br/><br/>
After Registering, Check Your database, It will be like this..<br/>
<img src="ScreenShots/post.png" height="300" width="600"><br/>
The above picture tells that the data which we are given in registration form is inserted into this table.<br/>
</br>
Now login With your Credientils,<br/>
<img src="ScreenShots/login.png" height="300" width="600"><br/>
<br/>
If you enter the correct Details in login, You will be Redirected to welcome page,<br/>
<img src="ScreenShots/home.png" height="300" width="600"><br/><br/>
Otherwise, You will get a popup notification and resirected to Error page,:<br/>
<img src="ScreenShots/popup.png" height="300" width="600">

For any Queries, you can contact me on Linkedin:
<img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" height="20" width="20">&nbsp;<a href="https://www.linkedin.com/in/muppuri-venkateswara-vamsi-kumar-2a6167208/"><button value="contact Me">Contact Me</button></a>
