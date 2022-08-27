from project import db
from project.com.vo.LoginVO import LoginVO

class SubjectVO(db.Model):
    __tablename__ = 'subjectmaster'
    subjectId = db.Column('subjectId', db.Integer, primary_key=True, autoincrement=True)
    subjectName = db.Column('subjectName', db.String(100),unique=True, nullable=False)
    subjectFaculty_LoginId=db.Column('subjectFaculty_LoginId',db.Integer,db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {

            'subjectId': self.subjectId,
            'subjectName': self.subjectName,
            'subjectFaculty_LoginId': self.subjectFaculty_LoginId

        }


db.create_all()
