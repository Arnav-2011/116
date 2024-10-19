#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/studentactivity2")
def student_webpage():
    name = 'Arnav'
    return render_template('studentactivity2.html', student_name = name)

#run the application on local server
app.run(debug=True)
