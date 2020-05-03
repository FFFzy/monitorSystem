import os

from flask_sqlalchemy import SQLAlchemy
# from controller.registerUrl import user,monitor
from controller.monitor import monitor
from controller.user import user
from flask import Flask,render_template,request,flash,session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/monitor_system'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config['SECRET_KEY'] = os.urandom(24)
# 添加数据到session中
# 操作session的时候 跟操作字典是一样的。
# SECRET_KEY

app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(monitor,url_prefix = '/monitor')

if __name__ == '__main__':
    app.run(debug=True)

#session(app)

@app.route('/', methods = ["get"])
def index():
    return render_template('index.html')






