from project import db
from project.com.vo.SubjectVO import SubjectVO
from project.com.vo.AssignmentVO import AssignmentVO



class AssignmentDAO:

    def insertAssignment(self, assignmentVO):
        db.session.add(assignmentVO)
        db.session.commit()

    def viewAssignment(self,assignmentVO):
        assignmentList = db.session.query(AssignmentVO, SubjectVO) \
            .filter_by(assignment_LoginId=assignmentVO.assignment_LoginId) \
            .join(SubjectVO, AssignmentVO.assignment_SubjectId == SubjectVO.subjectId).all()

        return assignmentList


    def userViewAssignment(self):
        assignmentList= AssignmentVO.query.all()

        return assignmentList


    def userViewAssignmentBySubject(self,assignmentVO):

        assignmentList=AssignmentVO.query.filter_by(assignment_SubjectId=assignmentVO.assignment_SubjectId).all()

        return assignmentList


    def deleteAssignment(self,assignmentVO):
        assignmentList = AssignmentVO.query.get(assignmentVO.assignmentId)
        db.session.delete(assignmentList)
        db.session.commit()

        return assignmentList


    def editCategory(self,categoryVO):

        # categoryList = CategoryVO.query.get(categoryVO.categoryId)

        # categoryList = CategoryVO.query.filter_by(categoryId=categoryVO.categoryId)

        categoryList = CategoryVO.query.filter_by(categoryId=categoryVO.categoryId).all()

        return categoryList

    def updateCategory(self,categoryVO):

        db.session.merge(categoryVO)

        db.session.commit()
