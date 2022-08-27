from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.StudentSubjectVO import StudentSubjectVO


class StudentSubjectDAO:

    def viewStudentSubject(self,studentSubjectVO):
        studentSubjectList = db.session.query(StudentSubjectVO, SubjectVO) \
            .filter_by(student_LoginId=studentSubjectVO.student_LoginId) \
            .join(SubjectVO, StudentSubjectVO.subjectId == SubjectVO.subjectId).all()

        return studentSubjectList

    def insertStudentSubject(self, studentSubjectVO):
        db.session.add(studentSubjectVO)
        db.session.commit()

    def deleteStudentSubject(self, studentSubjectVO):
        studentSubjectList = StudentSubjectVO.query.get(studentSubjectVO.studentSubjectId)
        db.session.delete(studentSubjectList)
        db.session.commit()
    '''
    def editCrossroad(self, crossroadVO):
        crossroadList = CrossroadVO.query.filter_by(crossroadId=crossroadVO.crossroadId)

        return crossroadList

    def updateCrossroad(self, crossroadVO):
        db.session.merge(crossroadVO)
        db.session.commit()
    '''