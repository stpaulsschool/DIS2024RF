from flask import Flask #First we import the Flask class

app = Flask(__name__) #Next we create an instance of this class


@app.route('/') #We then use the route() decorator to tell
                #Flask what URL should trigger our function
def hello_form():
    return "<p>Hello, this is a form!</p>"

if __name__ == '__main__':
   app.run(debug=True)
    #debug true makes it so if you change html and css you just have to refresh page
    #but if you change python code you have to termitate program and open it again

    #in terminal use ls to list directory
    #use cd space then type Unit press tab
    #pip install flask