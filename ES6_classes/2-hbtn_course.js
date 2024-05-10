export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;

    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;

    if (Array.isArray(students)) {
      this._students = students;
    }
    else {
      throw new TypeError('Students must be an array of strings');
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string'){
      return this._name = newName;
    }
    else {
      throw new TypeError('Name msut be a string');
    }
  }

  get length() {
    this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    }
    else {
      throw new TypeError('Lenght must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newstudents) {
    if (
        Array.isArray(newstudents) 
        && newstudents.every((student) => typeof student === 'string')
        ) {
          this._students = [...newstudents];
        }
    else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
