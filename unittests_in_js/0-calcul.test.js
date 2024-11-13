const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", () => {
  it("should round both numbers down and return the sum", () => {
    assert.strictEqual(calculateNumber(1.4, 2.4), 3);
  });

  it("should round both numbers up and return the sum", () => {
    assert.strictEqual(calculateNumber(1.6, 2.6), 5);
  });

  it("should round one number down and one number up, and return the sum", () => {
    assert.strictEqual(calculateNumber(1.4, 2.6), 4);
  });

  it("should work when one number is exactly .5", () => {
    assert.strictEqual(calculateNumber(2.5, 3.4), 6);
  });

  it("should work when both numbers are exactly .5", () => {
    assert.strictEqual(calculateNumber(2.5, 3.5), 6);
  });

  it("should work with negative numbers", () => {
    assert.strictEqual(calculateNumber(-1.4, -2.6), -4);
    assert.strictEqual(calculateNumber(-1.5, -2.5), -4);
  });

  it("should return the correct sum when numbers are integers", () => {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });
});
