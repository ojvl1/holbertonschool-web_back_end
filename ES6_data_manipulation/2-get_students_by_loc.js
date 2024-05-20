export default function getStudentsByLocation(students, city) {
  const list = students.filter((students) => students.location === city);
  return list;
}
