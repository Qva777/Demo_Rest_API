<h1>📍How to install: </h1>
<h4>1 - Connect venv:</h4> 
<i>python -m venv venv</i>
<h4>2 - Activate it:</h4> 
<ul>
  <li>cd venv</li>
  <li>cd Scripts</li>
  <li>activate</li>
</ul>
<h4>3 - In the Console, go to the root folder:</h4>
<i>cd ../..</i>
<h4>4 - Install libraries:</h4>
<pre>pip install -r requirements.txt</pre>
<h4>5 - Run the migration:</h4> 
<pre>python manage.py makemigrations</pre>
<h4>6 - Apply migration:</h4> 
<pre>python manage.py migrate</pre>
<h4>7 - Create Superuser:</h4> 
<pre>python manage.py createsuperuser</pre>
<h4>8 - Run server:</h4> 
<pre>python manage.py runserver</pre>
