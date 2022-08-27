from project import db
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.LoginVO import LoginVO


class SubjectDAO:

    '''
    def viewSubject(self):
        subjectList = db.session.query(SubjectVO, LoginVO).join(LoginVO,
                                                                   SubjectVO.subjectFaculty_LoginId == LoginVO.loginId).all()

        return subjectList
    '''
    def viewSubject(self,subjectVO):
        subjectList = SubjectVO.query.filter_by(subjectFaculty_LoginId=subjectVO.subjectFaculty_LoginId).all()

        return subjectList
    def viewAllSubject(self):
        subjectList=SubjectVO.query.all()

        return subjectList

    def insertSubject(self, subjectVO):
        db.session.add(subjectVO)
        db.session.commit()

    def deleteSubject(self, subjectVO):
        subjectList = SubjectVO.query.get(subjectVO.subjectId)
        db.session.delete(subjectList)
        db.session.commit()

    def editSubject(self, subjectVO):
        subjectList = SubjectVO.query.filter_by(subjectId=subjectVO.subjectId).all()

        return subjectList

    def updateSubject(self, subjectVO):
        db.session.merge(subjectVO)
        db.session.commit()
