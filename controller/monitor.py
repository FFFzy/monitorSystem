from flask import Blueprint,request,flash,render_template
from controller.registerUrl import monitor

@monitor.route('/main',methods = ['get'])
def main():
    return render_template('monitor/main.html')
