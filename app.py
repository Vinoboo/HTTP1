from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")
database={'Ramya': 'Ram@123', 'Nalini': 'Nali@123', 'Vinothini': 'Vino@123'}
@app.route('/form_login',methods=['POST','GET'])
def form_login():
    if request.method=='POST':
        name1=request.form['username']
        password1=request.form['password']
        if name1  not in database:
            return render_template('login.html',info="Invalid User")
        else:
            if database[name1]!=password1:
                return render_template('login.html',info="Invalid Password")
            else:
                return render_template('home.html', name=name1)
    return render_template('login.html')
#main program
if __name__=='__main__':
    app.run(debug=True)


