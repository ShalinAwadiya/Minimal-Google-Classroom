from project import app
from flask import render_template, redirect
from project.com.controller.LoginController import adminLoginSession
from project.com.vo.SubjectVO import SubjectVO
from project.com.dao.SubjectDAO import SubjectDAO
from flask import render_template, request, url_for, redirect, session
from project.com.vo.StudentSubjectVO import StudentSubjectVO
from project.com.dao.StudentSubjectDAO import StudentSubjectDAO


@app.route('/admin/loadSubject')
def adminLoadSubject():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addSubject.html')
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/insertSubject', methods=['POST'])
def adminInsertSubject():
    try:
        if adminLoginSession() == 'admin':

            subjectVO=SubjectVO()
            subjectDAO=SubjectDAO()

            subjectName = request.form['subjectName']
            subjectFaculty_LoginId=session['session_loginId']

            subjectVO.subjectName=subjectName
            subjectVO.subjectFaculty_LoginId=subjectFaculty_LoginId

            subjectDAO.insertSubject(subjectVO)

            return redirect(url_for('adminViewSubject'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/viewSubject')
def adminViewSubject():
    try:
        if adminLoginSession() == 'admin':

            subjectVO=SubjectVO()
            subjectDAO=SubjectDAO()

            subjectVO.subjectFaculty_LoginId=session['session_loginId']

            subjectVOList=subjectDAO.viewSubject(subjectVO)

            return render_template('admin/viewSubject.html',subjectVOList=subjectVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteSubject', methods=['GET'])
def adminDeleteSubject():
    try:
        if adminLoginSession() == 'admin':

            subjectVO=SubjectVO()
            subjectDAO=SubjectDAO()

            subjectId = request.args.get('subjectId')

            subjectVO.subjectId=subjectId

            subjectDAO.deleteSubject(subjectVO)

            return redirect(url_for('adminViewSubject'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



#USER

@app.route('/user/loadSubject')
def userLoadSubject():
    try:
        if adminLoginSession() == 'user':

            subjectDAO=SubjectDAO()
            subjectVOList=subjectDAO.viewAllSubject()

            return render_template('user/addSubject.html',subjectVOList=subjectVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/user/insertStudentSubject', methods=['POST'])
def userInsertStudentSubject():
    try:
        if adminLoginSession() == 'user':

            studentSubjectVO=StudentSubjectVO()
            studentSubjectDAO=StudentSubjectDAO()

            student_LoginId=session['session_loginId']
            subjectId = request.form['subjectId']

            studentSubjectVO.student_LoginId=student_LoginId
            studentSubjectVO.subjectId=subjectId

            studentSubjectDAO.insertStudentSubject(studentSubjectVO)

            return redirect(url_for('userViewStudentSubject'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/user/viewStudentSubject')
def userViewStudentSubject():
    try:
        if adminLoginSession() == 'user':

            studentSubjectVO=StudentSubjectVO()
            studentSubjectDAO=StudentSubjectDAO()

            studentSubjectVO.student_LoginId=session['session_loginId']

            studentSubjectVOList=studentSubjectDAO.viewStudentSubject(studentSubjectVO)

            return render_template('user/viewSubject.html',studentSubjectVOList=studentSubjectVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)




@app.route('/user/deleteStudentSubject', methods=['GET'])
def userDeleteStudentSubject():
    try:
        if adminLoginSession() == 'user':

            studentSubjectVO=StudentSubjectVO()
            studentSubjectDAO=StudentSubjectDAO()

            studentSubjectId = request.args.get('studentSubjectId')

            studentSubjectVO.studentSubjectId=studentSubjectId

            studentSubjectDAO.deleteStudentSubject(studentSubjectVO)

            return redirect(url_for('userViewStudentSubject'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)

