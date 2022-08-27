from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.AssignmentVO import AssignmentVO


class StudentAssignmentVO(db.Model):
    __tablename__ = 'studentassignmentmaster'
    studentAssignmentId = db.Column('studentAssignmentId', db.Integer, primary_key=True, autoincrement=True)
    studentAssignmentFileName=db.Column('studentAssignmentFileName', db.String(100))
    studentAssignmentFilePath=db.Column('studentAssignmentFilePath', db.String(100))
    studentAssignmentStatus=db.Column('studentAssignmentStatus', db.String(10))
    studentAssignmentDate=db.Column('studentAssignmentDate', db.DATE)
    studentAssignmentTime=db.Column('studentAssignmentTime', db.TIME)
    studentAssignmentMarks=db.Column('studentAssignmentMarks', db.Integer)
    studentAssignmentComment=db.Column('studentAssignmentComment', db.String(200))
    studentAssignment_SubjectId=db.Column('studentAssignment_SubjectId', db.Integer, db.ForeignKey(SubjectVO.subjectId))
    studentAssignment_AssignmentId=db.Column('studentAssignment_AssignmentId', db.Integer, db.ForeignKey(AssignmentVO.assignmentId))
    studentAssignment_LoginId = db.Column('studentAssignment_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))


    def as_dict(self):
        return {

            'studentAssignmentId': self.studentAssignmentId,
            'studentAssignmentFileName': self.studentAssignmentFileName,
            'studentAssignmentFilePath': self.studentAssignmentFilePath,
            'studentAssignmentStatus': self.studentAssignmentStatus,
            'studentAssignmentDate': self.studentAssignmentDate,
            'studentAssignmentTime': self.studentAssignmentTime,
            'studentAssignmentMarks': self.studentAssignmentMarks,
            'studentAssignmentComment': self.studentAssignmentComment,
            'studentAssignment_SubjectId': self.studentAssignment_SubjectId,
            'studentAssignment_AssignmentId': self.studentAssignment_AssignmentId,
            'studentAssignment_LoginId': self.studentAssignment_LoginId
        }


db.create_all()
