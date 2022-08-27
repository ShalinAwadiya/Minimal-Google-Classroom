from project import db
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.LoginVO import LoginVO



class AssignmentVO(db.Model):
    __tablename__ = 'assignmentmaster'
    assignmentId = db.Column('assignmentId',db.Integer, primary_key=True, autoincrement=True)
    assignmentName = db.Column('assignmentName', db.String(100),unique=True)
    assignmentDeadline = db.Column('assignmentDeadline', db.String(100))
    assignmentFileName = db.Column('assignmentFileName', db.String(100))
    assignmentFilePath = db.Column('assignmentFilePath', db.String(100))
    assignment_SubjectId = db.Column('assignment_SubjectId', db.Integer, db.ForeignKey(SubjectVO.subjectId))
    assignment_LoginId=db.Column('assignment_LoginId',db.Integer,db.ForeignKey(LoginVO.loginId))


    def as_dict(self):
        return {

            'assignmentId': self.assignmentId,
            'assignmentName': self.assignmentName,
            'assignmentDeadline': self.assignmentDeadline,
            'assignmentFileName': self.assignmentFileName,
            'assignmentFilePath': self.assignmentFilePath,
            'assignment_SubjectId': self.assignment_SubjectId,
            'assignment_LoginId':self.assignment_LoginId

        }

db.create_all()