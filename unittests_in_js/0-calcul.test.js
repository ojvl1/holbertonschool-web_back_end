const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", () => {
  it("should round both numbers down and return the sum", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it("should round both numbers up and return the sum", () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it("should round one number down and one number up, and return the sum", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it("should work when one number is exactly .5", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
