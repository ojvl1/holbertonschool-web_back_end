export default class Car {
  constructor(brand, motor, color) {
    // Check if brand is a string
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Create a new object with the same prototype
    const NewObj = this.constructor[Symbol.species] || this.constructor;
    // Create a new instance of the object
    const clone = new NewObj();
    // Copy the properties of the object
    return clone;
  }
}
