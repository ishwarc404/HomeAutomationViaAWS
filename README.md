THERE ARE 4 MAJOR COMPONENTS TO THIS PROJECT

1. NODE MCU CODE TO CONTROL THE DEVICES - This is coded by Drasti & Co.
2. LOCAL FLASK SERVER - This flask server is used to keep polling the remote server set up on AWS and once it gets
back a JSON response, it accordingly acts by sending signals to the local server set up by the NODE MCU's wifi unit.
3. AMAZON EC2 instance - This is set up on my cloud with the email id=emailishwarc@gmail.com
4. EC2 FLASK SERVER - This flask server is made public by setting up a proxy in the sites-enables file of NginX. Nginx interacts with 
the flask server running on the ec2 via gunicorn.


FOLDER STRUCTURE:
1. The "miniproject_ec2" folder contains all the files which need to be run on the flask server
2. The "webserver_led" folder contains the NODEMCU code.
3. The rest of the files for now are the local computer's flask server code.

CHANGES MADE IN THE AWS EC2 INSTANCE:
1. INSTALLED PIP3
2. INSTALLED NGINX AND REMOVED /sites-enabled/default as it keeps loading up the apache page.
3. Removed apache2 also just to remove any hinderance.
4. Installed gunicorn3
5. created a folder /miniproject in root. We go insside and run "gunicorn3 miniproject_server:app" 
6. Before installing flask, ran "EXPORT LC_ALL=C"