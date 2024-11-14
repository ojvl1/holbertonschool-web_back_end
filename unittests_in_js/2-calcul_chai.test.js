const { expect } = require("chai");
const calculateNumber = require("./2-calcul_chai");

describe("calculateNumber", () => {
  it("...", () => {
    expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
  });
  it("...", () => {
    expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);
  });
  it("...", () => {
    expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.be.closeTo(0.2, 0.001);
  });
  it("...", () => {
    expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
  });
});
