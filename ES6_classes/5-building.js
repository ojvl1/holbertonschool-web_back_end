export default class Building {
  constructor(sqft) {
    // Check if istance is not of 'Buildin'(force a subclass)
    // Check that the instance has .evacuationWarningMessage
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }
}
