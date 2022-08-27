from project import app
from flask import render_template, request, url_for, redirect, session
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from project.com.controller.LoginController import adminLoginSession


@app.route('/admin/loadStudent')
def adminLoadStudent():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addStudent.html')
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/insertStudent', methods=['POST'])
def adminInsertStudent():
    try:
        if adminLoginSession() == 'admin':

            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginUsername = request.form['loginUsername']


            loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
            sender = 'aipythonshalin@gmail.com'
            receiver = loginUsername

            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = 'PYTHON PASSWORD'
            msg.attach(MIMEText(loginPassword, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, 'vnzbkfmgtaubsgut')
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            loginVO.loginUsername = loginUsername
            loginVO.loginPassword = loginPassword
            loginVO.loginRole = 'user'
            loginVO.loginStatus = 'active'

            loginDAO.insertLogin(loginVO)

            return redirect(url_for('adminViewStudent'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/viewStudent')
def adminViewStudent():
    try:
        if adminLoginSession() == 'admin':

            loginVO=LoginVO()
            loginDAO=LoginDAO()

            loginRole='user'

            loginVO.loginRole=loginRole

            loginVOList=loginDAO.viewLogin(loginVO)

            return render_template('admin/viewStudent.html',loginVOList=loginVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteStudent', methods=['GET'])
def adminDeleteStudent():
    try:
        if adminLoginSession() == 'admin':

            loginVO=LoginVO()
            loginDAO=LoginDAO()

            loginId = request.args.get('loginId')

            loginVO.loginId=loginId

            loginDAO.deleteLogin(loginVO)

            return redirect(url_for('adminViewStudent'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)
