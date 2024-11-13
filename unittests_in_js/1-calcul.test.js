const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", () => {
  it("...", () => {
    assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
  });
  it("...", () => {
    assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
  });
  it("...", () => {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
  });
  it("...", () => {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
  });
});
