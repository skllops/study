from flask import Flask, render_template
from flask import request

import pymysql

app = Flask(__name__) #Flask 객체를 인스턴스 생성

#연동
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '12345678',
    db = 'test',
    charset='utf8'
)
print(db_conn)

#커서 객체 생성
cursor = db_conn.cursor()
query = "select * from player"
cursor.execute(query)
for i in cursor:
    print(i)

@app.route('/sqltest')
def sqltest():
    #커서객체 생성
    cursor = db_conn.cursor()
    query = "select * from player"
    cursor.execute(query)
    result =[]

    for i in cursor:
        temp = {'player_id':i[0],'player_name':i[1]}
        result.append(temp)
    return render_template('sqltest.html', result_table = result)

@app.route('/detail')
def detailtest():
    temp = request.args.get('id')
    temp1 = request.args.get('name')

    cursor = db_conn.cursor()

    query = "select * from player where player_id = {} and player_name like '{}'".format(temp,temp1)
        #sql 쿼리에 작은 따옴표 쿼리문에 넣으니까 넣어줘야한다??
    cursor.execute(query)

    result = []
    for i in cursor:            
        temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2],'weight':i[-1]}
        result.append(temp)

    return render_template('detail.html', result_table = result)

# @app.route('/')                 #접속하는 url
# def index():
#     temp = request.args.get('uid')
#     temp1 = request.args.get('cid')
#     print(temp,temp1)

#     return render_template('index.html')

# @app.route('/test', methods=['POST'])
# def testget():
#     value = request.form['input']
#     print(value)
#     return render_template('posttest.html')

if __name__ =="__main__":
    app.run(debug=True)

#host 등을 직접 지정하고 싶다면
#app.run(host="127.0.0.1", port="5000",debug=True)