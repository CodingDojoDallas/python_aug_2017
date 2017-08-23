# Important Notes
```
{{repoName}} == the name of your repository on GitLab
{{projectName}} == the name you used for the django-admin startproject command
```
# Deployment Instructions

Follow instructions on Learn to create a new Amazon EC2 instance.  Make sure to select `Ubuntu 16.04`.  You can use an existing `.pem` file or you can create a new one.  Save the `.pem` file in a location OUTSIDE OF YOUR PROJECT FOLDER.  A folder on the desktop for `.pem` files is a good idea.

Create a new repository on GitLab for your project.

Activate your virutal environment then navigate to your project folder and make a list of your dependencies
```
pip freeze > requirements.txt
```

Setup .gitignore file
```
touch .gitignore
```

Use your text editor and edit the contents of .gitignore like so
```
*.pyc
venv/
```
Push your project to GitLab
```
git remote add origin <address_to_repo_on_GitLab>
git add .
git commit -m 'initial commit'
git push -u origin master
```

Navigate to the directory where you saved your `.pem` file

IF you have NEVER used this `.pem` file before to connect to an Amazon Instance then change permissions
```
chmod 400 <pem_file>
```

Now, connect to your Amazon Instance
```
ssh -i <pem_file> ubuntu@<public_ip>
```

Update the Ubuntu machine
```
sudo apt-get update
sudo apt-get install python-pip python-dev nginx git
sudo apt-get update
sudo pip install virtualenv
```

Clone your repository
```
git clone <address_to_repo_on_GitLab>
```

Create `virtual environment` and install dependencies
```
cd <repo_name>
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install django bcrypt django-extensions
pip install gunicorn
```

Update your `settings.py` file
```
cd <project_name>
sudo vim settings.py
```

You're now using vim, press `i` to go into Insert Mode and edit the following lines
```
# Inside settings.py
# modify these lines
DEBUG = False
ALLOWED_HOSTS = ['{{yourEC2.public.ip}}']
# add the line below to the bottom of the file
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```

After editing, press `esc` to exit Insert Mode

Collect your static files
```
cd ..
python manage.py collectstatic
```
If a `yes/no` prompt appears.  Type `yes`

Deactivate your `virutal environment` and create the `gunicorn.service` file
```
deactivate
sudo vim /etc/systemd/system/gunicorn.service
```

You're now using vim, press `i` to go into Insert Mode and paste the following code
```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/{{repoName}}
ExecStart=/home/ubuntu/{{repoName}}/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/{{repoName}}/{{projectName}}.sock {{projectName}}.wsgi:application
[Install]
WantedBy=multi-user.target
```
Edit the code by replacing {{repoName}} and {{projectName}} with the appropriate data.  Then, press `esc` to exit Insert Mode.  Then, type `:wq` and press `enter` to exit VIM.

Restart Gunicorn
```
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

Edit your Nginx Files, replace {{repoName}} with the appropriate data
```
cd /etc/nginx/sites-available
sudo vim {{repoName}}
```

You're now using vim, press `i` to go into Insert Mode and paste the following code
```
server {
  listen 80;
  server_name {{yourEC2.public.ip}};
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
      root /home/ubuntu/{{repoName}};
  }
  location / {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/{{repoName}}/{{projectName}}.sock;
  }
}
```
Replace {{yourEC2.public.ip}}, {{repoName}}, and {{projectName}} with the appropriate data.  Then, press `esc` to exit Insert Mode.  Then, type `:wq` and press `enter` to exit VIM.

Remove the default file and create the symbolic link
```
sudo rm default
sudo ln -s /etc/nginx/sites-available/{{repoName}} /etc/nginx/sites-enabled
sudo nginx -t
```

Restart Nginx
```
sudo service nginx restart
```

You're deployed!  Just type your public-ip into the address bar of your web browser and you should see your website!
