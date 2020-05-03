from flask import Blueprint,request,flash,render_template
from controller.registerUrl import user
from sever.userSever import *

@user.route('/login_form',methods=['get'])
def login_form():
    return render_template('account/login.html')

@user.route('/login',methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username,password]):
        message = '参数不完整'
        model = {"message":message}
        return render_template('account/login.html',model)

    elif getUserByNameAndPass(username,password) == None:
        message = '用户名或密码错误'
        model = {"message":message}
        return render_template('account/login.html',model = model)

    else:
   #     session['user'] = getUserByNameAndPass(username,password)
        return render_template('monitor/main.html')

@user.route('/register_form',methods=['get'])
def register_form():
    return render_template('account/register.html')

@user.route('/register',methods=['post'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    repeatpassword = request.form.get('repeatpassword')
    print("password",password.strip(),"reap",repeatpassword.strip())

    if not all([username,password,repeatpassword]):
        message = '参数不完整'
        model = {"message":message}
        return render_template('account/register.html',model = model)
    elif getUserByUsername(username)!=None:
        message = '用户名已存在'
        model = {"message":message}
        return render_template('account/register.html',model = model)
    elif password == repeatpassword:
        insertUser(username, password)
        return render_template('account/login.html')

    else:
        message = '两次输入密码不一致'
        model = {"message":message}
        return render_template('account/register.html',model = model)






