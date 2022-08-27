from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.AssignmentVO import AssignmentVO
from project.com.vo.StudentAssignmentVO import StudentAssignmentVO


class StudentAssignmentDAO:

    def viewStudentAssignment(self,studentAssignmentVO):
        studentAssignmentList = db.session.query(StudentAssignmentVO, AssignmentVO) \
            .filter_by(studentAssignment_LoginId=studentAssignmentVO.studentAssignment_LoginId) \
            .join(AssignmentVO,StudentAssignmentVO.studentAssignment_AssignmentId == AssignmentVO.assignmentId).all()

        return studentAssignmentList


    def viewStudentAssignmentByAssignmentId(self,studentAssignmentVO):
        studentAssignmentList = db.session.query(StudentAssignmentVO, LoginVO) \
            .filter_by(studentAssignment_AssignmentId=studentAssignmentVO.studentAssignment_AssignmentId) \
            .join(LoginVO,StudentAssignmentVO.studentAssignment_LoginId == LoginVO.loginId).all()

        return studentAssignmentList


    def insertStudentAssignment(self, studentAssignmentVO):
        db.session.add(studentAssignmentVO)
        db.session.commit()


    def deleteStudentAssignment(self, studentAssignmentVO):

        studentAssignmentList = StudentAssignmentVO.query.get(studentAssignmentVO.studentAssignmentId)
        db.session.delete(studentAssignmentList)
        db.session.commit()

        return studentAssignmentList


    def editStudentAssignment(self, studentAssignmentVO):
        studentAssignmentList = StudentAssignmentVO.query.filter_by(studentAssignmentId=studentAssignmentVO.studentAssignmentId).all()

        return studentAssignmentList


    def updateStudentAssignment(self, studentAssignmentVO):
        db.session.merge(studentAssignmentVO)
        db.session.commit()