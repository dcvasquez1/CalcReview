import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

#app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
#The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
	if request.post != nil {
		return render_template('page2.html')
	}
    return render_template('page1.html')
  
if __name__=="__main__":
  app.run(debug=False)