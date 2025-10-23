from flask import Flask, request, jsonify
app=Flask(__name__)
@app.route('/index',methods=['GET','POST'])
def index():
    age=request.args.get("age")
    pwd=request.args.get("pwd")
    print(age, pwd)
    xx=request.form.get("xx")
    yy=request.form.get("yy")
    print(xx,yy)



    return jsonify(age=age,pwd=pwd,xx=xx,yy=yy)

if __name__=='__main__':
    app.run(debug=True)