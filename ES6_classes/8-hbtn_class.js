export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size === 'number') {
      this._size = size;
    } else {
      throw new Error('size must be a number');
    }
    if (typeof location === 'string') {
      this._location = location;
    } else {
      throw new Error('location must be a string');
    }
  }

  // Symbol method to return the location or size
  [Symbol.toPrimitive](type) {
    if (type === 'string') return this._location;

    return this._size;
  }
}
