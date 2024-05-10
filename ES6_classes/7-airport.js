export default class Airport {
  constructor(name, code) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('Name must be a string');
    }
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new Error('Code must be a string');
    }
  }

  // Getter to overwrite .toString() all objects have this
  // Is like the __str__ representation from python
  get [Symbol.toStringTag]() {
    return `${this._code}`;
  }
}
