export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const filteredStudents = studentList.filter(
    (student) => student.location === city,
  );
  const studentsAndGrades = filteredStudents.map((student) => {
    // Filter by student.id and grade.studentId
    const studentGrade = newGrades.find(
      (grade) => grade.studentId === student.id,
    );
    // Found a grade that has the student id
    if (studentGrade) {
      return { ...student, grade: studentGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return studentsAndGrades;
}
