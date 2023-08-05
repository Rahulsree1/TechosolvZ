from flask import Flask,render_template,request,redirect,url_for
import sqlite3
import datetime
app = Flask(__name__,template_folder="templets",static_folder="static")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/form/")
def form():
    return render_template("form.html")
@app.route("/probid",methods = ['POST'])
def probid():
    now = datetime.datetime.now()
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    fname = request.form.get('01')
    lname = request.form.get('02')
    email = request.form.get('03')
    phone = request.form.get('04')
    prob = request.form.get('05')
    print(fname,lname,email,phone,prob)
    f = cur.execute("SELECT * FROM Data")
    id = len(f.fetchall())+1
    pid = int(str(now.day)+str(now.month)+str(now.year)+str(now.hour)+str(now.minute)+str(now.second))
    dat = str(now.date())
    tim = str(now.time())
    cur.execute(f"INSERT INTO Data VALUES({id},{pid},'{fname}','{lname}','{email}',{phone},'{prob}',1,'{dat}','{tim}')")
    con.commit()
    con.close()
    return render_template("probid.html",proid = pid)

@app.route("/getstatus",methods=['POST'])
def gstatus():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    pid = request.form.get('01')
    f = cur.execute(f"SELECT status FROM Data WHERE ProbId == {int(pid)}")
    stat = f.fetchall()[0][0]
    return render_template("stat.html",sdata = stat)

@app.route("/admP",methods = ['POST'])
def adminp():
    user = request.form.get("user")
    passwd = request.form.get("passwd")
    credentials = {"admin":"TechoSolvz@113322","Rahul1122":"Rahul@9676"}
    if user in credentials.keys() and credentials[user] == passwd:
        return render_template("AdminPage.html")
    else:
        return '<h1 style="color: red; text-align: center;">Enter Correct credentials</h1>',False
@app.route("/admin")
def admin():
    return render_template ("admin.html")

@app.route("/up",methods = ['POST'])
def adminup():
        data1 = request.form.get("01")
        data2 = request.form.get("02")
        if data1 == None and data2 == 'updb':
            return render_template("update.html")
        else:
            return "Error"


@app.route("/data",methods=['POST'])
def data():
    data1 = request.form.get("01")
    data2 = request.form.get("02")
    if data1 == 'data' and data2 == None:
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM Data")
        data = data.fetchall()
        con.close()
        return render_template("data.html",data=data)
    else:
        return "Error"

@app.route("/adminupdate",methods = ['POST'])
def adminupdate():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    pidd = request.form.get("pid")
    col = request.form.get("col")
    val = request.form.get("val")
    cur.execute(f"UPDATE Data SET {col}='{val}' WHERE Id={pidd}")
    con.commit()
    return '<h1 style="color: red; text-align: center;">Data Updated</h1>'











if __name__=="__main__":
    app.run(debug=True)