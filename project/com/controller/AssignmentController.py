from project import app
from flask import render_template, redirect
from project.com.controller.LoginController import adminLoginSession
from project.com.vo.SubjectVO import SubjectVO
from project.com.dao.SubjectDAO import SubjectDAO
from flask import render_template, request, url_for, redirect, session
from project.com.vo.AssignmentVO import AssignmentVO
from project.com.dao.AssignmentDAO import AssignmentDAO
from werkzeug.utils import secure_filename
import os
from project.com.vo.StudentSubjectVO import StudentSubjectVO
from project.com.dao.StudentSubjectDAO import StudentSubjectDAO
from project.com.vo.StudentAssignmentVO import StudentAssignmentVO
from project.com.dao.StudentAssignmentDAO import StudentAssignmentDAO
import datetime



@app.route('/admin/loadAssignment')
def adminLoadAssignment():
    try:
        if adminLoginSession() == 'admin':

            subjectVO=SubjectVO()
            subjectDAO=SubjectDAO()

            subjectVO.subjectFaculty_LoginId=session['session_loginId']

            subjectVOList=subjectDAO.viewSubject(subjectVO)

            return render_template('admin/addAssignment.html',subjectVOList=subjectVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/insertAssignment', methods=['POST'])
def adminInsertAssignment():
    try:
        if adminLoginSession() == 'admin':

            assignmentVO=AssignmentVO()
            assignmentDAO=AssignmentDAO()

            assignmentName = request.form['assignmentName']
            assignment_SubjectId = request.form['assignment_SubjectId']
            assignmentDeadline=request.form['assignmentDeadline']
            assignment_LoginId=session['session_loginId']


            UPLOAD_FOLDER = 'project/static/adminResources/assignment/'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['file']
            assignmentFileName = secure_filename(file.filename)
            assignmentFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(assignmentFilePath, assignmentFileName))


            assignmentVO.assignmentName=assignmentName
            assignmentVO.assignment_SubjectId=assignment_SubjectId
            assignmentVO.assignmentDeadline=assignmentDeadline
            assignmentVO.assignment_LoginId=assignment_LoginId
            assignmentVO.assignmentFileName=assignmentFileName
            assignmentVO.assignmentFilePath = assignmentFilePath.replace('project', '..')

            assignmentDAO.insertAssignment(assignmentVO)


            return redirect(url_for('adminViewAssignment'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/viewAssignment')
def adminViewAssignment():
    try:
        if adminLoginSession() == 'admin':

            assignmentVO=AssignmentVO()
            assignmentDAO=AssignmentDAO()

            assignmentVO.assignment_LoginId=session['session_loginId']

            assignmentVOList=assignmentDAO.viewAssignment(assignmentVO)


            return render_template('admin/viewAssignment.html',assignmentVOList=assignmentVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/deleteAssignment', methods=['GET'])
def adminDeleteAssignment():
    try:
        if adminLoginSession() == 'admin':

            assignmentVO=AssignmentVO()
            assignmentDAO=AssignmentDAO()

            assignmentId= request.args.get('assignmentId')

            assignmentVO.assignmentId=assignmentId

            assignmentVOList=assignmentDAO.deleteAssignment(assignmentVO)

            assignmentFilePath = assignmentVOList.assignmentFilePath.replace('..', 'project')
            assignmentFile = assignmentFilePath + assignmentVOList.assignmentFileName
            os.remove(assignmentFile)

            return redirect(url_for('adminViewAssignment'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/viewStudentAssignment',methods=['GET'])
def adminViewStudentAssignment():
    try:
         if adminLoginSession() == 'admin':

             studentAssignmentVO = StudentAssignmentVO()
             studentAssignmentDAO = StudentAssignmentDAO()

             studentAssignment_AssignmentId = request.args.get('assignmentId')

             studentAssignmentVO.studentAssignment_AssignmentId=studentAssignment_AssignmentId

             studentAssignmentVOList=studentAssignmentDAO.viewStudentAssignmentByAssignmentId(studentAssignmentVO)


             return render_template('admin/viewStudentAssignment.html', studentAssignmentVOList=studentAssignmentVOList)
         else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/admin/checkStudentAssignment', methods=['GET'])
def admincheckStudentAssignment():
    try:
        if adminLoginSession() == 'admin':

            studentAssignmentVO = StudentAssignmentVO()
            studentAssignmentDAO = StudentAssignmentDAO()

            studentAssignmentId = request.args.get('studentAssignmentId')

            studentAssignmentVO.studentAssignmentId = studentAssignmentId

            studentAssignmentVOList = studentAssignmentDAO.editStudentAssignment(studentAssignmentVO)


            return render_template('admin/checkStudentAssignment.html',studentAssignmentVOList=studentAssignmentVOList)

        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)




@app.route('/admin/updateStudentAssignment', methods=['POST'])
def adminUpdateStudentAssignment():
    try:
        if adminLoginSession() == 'admin':

            studentAssignmentVO = StudentAssignmentVO()
            studentAssignmentDAO = StudentAssignmentDAO()

            assignmentId=request.form['assignmentId']
            studentAssignmentId = request.form['studentAssignmentId']
            studentAssignmentMarks=request.form['studentAssignmentMarks']
            studentAssignmentComment=request.form['studentAssignmentComment']

            studentAssignmentVO.studentAssignmentId=studentAssignmentId
            studentAssignmentVO.studentAssignmentStatus='Checked'
            studentAssignmentVO.studentAssignmentMarks=studentAssignmentMarks
            studentAssignmentVO.studentAssignmentComment=studentAssignmentComment

            studentAssignmentDAO.updateStudentAssignment(studentAssignmentVO)

            return redirect('/admin/viewStudentAssignment?assignmentId={}'.format(assignmentId))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)







#USER



@app.route('/user/loadAssignment')
def userLoadAssignment():
    try:
        if adminLoginSession() == 'user':


            studentSubjectVO=StudentSubjectVO()
            studentSubjectDAO=StudentSubjectDAO()

            studentSubjectVO.student_LoginId=session['session_loginId']

            studentSubjectVOList=studentSubjectDAO.viewStudentSubject(studentSubjectVO)

            assignmentDAO=AssignmentDAO()
            assignmentVOList=assignmentDAO.userViewAssignment()


            return render_template('user/addAssignment.html',studentSubjectVOList=studentSubjectVOList,assignmentVOList=assignmentVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)




@app.route('/user/insertStudentAssignment', methods=['POST'])
def userInsertStudentAssignment():
    try:
        if adminLoginSession() == 'user':

            studentAssignmentVO=StudentAssignmentVO()
            studentAssignmentDAO=StudentAssignmentDAO()

            UPLOAD_FOLDER = 'project/static/adminResources/studentAssignment/'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['file']
            studentAssignmentFileName = secure_filename(file.filename)
            studentAssignmentFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(studentAssignmentFilePath, studentAssignmentFileName))


            studentAssignment_SubjectId=request.form['studentAssignment_SubjectId']
            studentAssignment_AssignmentId=request.form['studentAssignment_AssignmentId']
            studentAssignment_LoginId=session['session_loginId']

            studentAssignmentVO.studentAssignmentFileName=studentAssignmentFileName
            studentAssignmentVO.studentAssignmentFilePath=studentAssignmentFilePath.replace('project', '..')
            studentAssignmentVO.studentAssignmentStatus='Unchecked'
            studentAssignmentVO.studentAssignmentDate=datetime.datetime.now().date()
            studentAssignmentVO.studentAssignmentTime=datetime.datetime.now().time()
            studentAssignmentVO.studentAssignment_SubjectId=studentAssignment_SubjectId
            studentAssignmentVO.studentAssignment_AssignmentId=studentAssignment_AssignmentId
            studentAssignmentVO.studentAssignment_LoginId=studentAssignment_LoginId

            studentAssignmentDAO.insertStudentAssignment(studentAssignmentVO)


            return redirect(url_for('userViewStudentAssignment'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)



@app.route('/user/viewStudentAssignment')
def userViewStudentAssignment():
    try:
        if adminLoginSession() == 'user':


            studentAssignmentVO=StudentAssignmentVO()
            studentAssignmentDAO=StudentAssignmentDAO()

            studentAssignmentVO.studentAssignment_LoginId=session['session_loginId']

            studentAssignmentVOList=studentAssignmentDAO.viewStudentAssignment(studentAssignmentVO)


            return render_template('user/viewAssignment.html',studentAssignmentVOList=studentAssignmentVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)




@app.route('/user/deleteStudentAssignment', methods=['GET'])
def userDeleteStudentAssignment():
    try:
        if adminLoginSession() == 'user':

            studentAssignmentVO=StudentAssignmentVO()
            studentAssignmentDAO=StudentAssignmentDAO()

            studentAssignmentId= request.args.get('studentAssignmentId')

            studentAssignmentVO.studentAssignmentId=studentAssignmentId

            studentAssignmentVOList=studentAssignmentDAO.deleteStudentAssignment(studentAssignmentVO)

            studentAssignmentFilePath = studentAssignmentVOList.studentAssignmentFilePath.replace('..', 'project')
            studentAssignmentFile = studentAssignmentFilePath + studentAssignmentVOList.studentAssignmentFileName
            os.remove(studentAssignmentFile)

            return redirect(url_for('userViewStudentAssignment'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)





@app.route('/user/viewAssignment', methods=['GET'])
def userViewAssignment():
    try:
        if adminLoginSession() == 'user':

            assignmentVO=AssignmentVO()
            assignmentDAO=AssignmentDAO()

            assignment_SubjectId = request.args.get('subjectId')

            assignmentVO.assignment_SubjectId=assignment_SubjectId
            assignmentVOList=assignmentDAO.userViewAssignmentBySubject(assignmentVO)


            return render_template('/user/viewAssignmentBySubject.html',assignmentVOList=assignmentVOList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)

