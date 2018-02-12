import os
from flask import Flask, url_for, render_template, request, Markup
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key = '\x17\x96e\x94]\xa0\xb8\x1e\x8b\xee\xdd\xe9\x91^\x9c\xda\x94\t\xe8S\xa1Oe_'

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

#app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
#The value should be set in Heroku (Settings->Config Vars).  

@app.route("/")
def renderMain():
	session["test-score"]=0
	session["record-score"]=0
	session["comment"]="You finished"
	return render_template('page1.html')
	
@app.route("/retest")
def restartTest():
	session["test-score"]=0
	session["comment"]="You finished"
	return render_template('page1.html')
	
@app.route('/question-two', methods=['POST'])
def render_page2():
	if request.form["question1"] == 'B':
		session["test-score"]+=1
	return render_template('page2.html')
	
@app.route('/question-three', methods=['POST'])
def render_page3():
	if request.form["question2"] == 'A':
		session["test-score"]+=1
	return render_template('page3.html')
	
@app.route('/question-four', methods=['POST'])
def render_page4():
	if request.form["question3"] == 'C':
		session["test-score"]+=1
	return render_template('page4.html')
	
@app.route('/final', methods=['POST'])
def render_final():
	if request.form["question4"] == 'B':
		session["test-score"]+=1
	if session["test-score"] > session["record-score"] and session["test-score"] != 4: #Personal high score but not 4/4
		session["record-score"]=session["test-score"]
		session["comment"]="That's your personal high score!"
	elif session["test-score"] == 4: #Perfect Score
		session["record-score"]=4
		session["comment"]="You've matched the high score!!!"
	return render_template('review.html', finalscore="You score: " + str(session["test-score"]) + "/4", sessionHighScore="Session high score: " + str(session["record-score"]) + "/4", finishingComment = session["comment"])
	
if __name__=="__main__":
	app.run(debug=False)