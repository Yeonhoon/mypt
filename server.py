from re import T, template
from flask import Flask, jsonify, render_template, request, session, redirect
import pandas as pd
import os
from flask_login import LoginManager
import json
import model

md = model.Record()

app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def main():
    x= 'hello'
    return render_template('index.html')

@app.route('/2')
def main2():
    x= 'hello'
    return render_template('index2.html')

@app.route('/diary')
def diary():
    return render_template('diary.html')

@app.route('/loginform')
def loginForm():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['check_id']
    user_pw = request.form['check_pw']
    result = md.login(user_id, user_pw)
    if md.checkId(user_id) is None:
        return jsonify(result='ID_Fail')

    if md.checkPw(user_id)[0] != user_pw:
        return jsonify(result='PW_Fail')
    session['user_id']=result[0]
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


@app.route('/save', methods=['POST'])
def save_record():
    user_id = session['user_id']
    date = request.form['date']
    big= request.form['big']
    middle= request.form['middle']
    small=request.form['small']
    setNum=request.form['setNum']
    weight=request.form['weight']
    repNum = request.form['repNum']
    etc = request.form['etc']
    print(user_id, date,big,middle,small,setNum,weight,repNum,etc)
    md.save(user_id, date, big, middle, small, setNum, weight, repNum, etc)
    return redirect('/diary')

@app.route('/dashboard')
def to_dash():
    conn = model.conn
    sql = sql = f"""select sum(workout_weight * WORKOUT_REPNUM) as volume, to_char(workout_date) as dates, workout_big as category
                from workout_diary
                where workout_user = '{session['user_id']}'
                group by workout_date, workout_big
                order by workout_date """

    df = pd.read_sql(sql,con=conn)
    print(df)
    # result = md.getData(session['user_id'])
    data = df.to_json(orient='columns')
    
    return render_template('/dashboard.html', data=data)




if __name__ == '__main__':
    app.run(debug=True)