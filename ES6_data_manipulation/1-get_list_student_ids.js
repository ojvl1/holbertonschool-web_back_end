export default function getListStudentsIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const idStudents = students.map((students) => students.id);
  return idStudents;
}
