from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SubjectVO import SubjectVO


class StudentSubjectVO(db.Model):
    __tablename__ = 'studentsubjectmaster'
    studentSubjectId = db.Column('studentSubjectId', db.Integer, primary_key=True, autoincrement=True)
    student_LoginId = db.Column('student_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))
    subjectId = db.Column('subjectId', db.Integer, db.ForeignKey(SubjectVO.subjectId))

    def as_dict(self):
        return {
            'studentSubjectId':self.studentSubjectId,
            'student_LoginId': self.student_LoginId,
            'subjectId': self.subjectId
        }


db.create_all()
