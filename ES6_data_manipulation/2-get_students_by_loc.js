export default function getStudentsByLocation(listObjects, location) {
  if (!Array.isArray(listObjects)) {
    return [];
  }
  return listObjects.filter((student) => student.location === location);
}