from flask import Flask, request, jsonify,render_template
app=Flask(__name__)
@app.route('/login',methods=['GET'])
def login():
    return render_template('loginPage.html')
@app.route('/login',methods=['post'])
def login_post():
    account=request.form['account']
    password=request.form['password']
    print(account,password)
    return render_template('loginPage.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('Register.html')
@app.route('/change_pwd',methods=['GET'])
def change_pwd():
    return render_template('changePassword.html')





if __name__=='__main__':
    app.run(debug=True)