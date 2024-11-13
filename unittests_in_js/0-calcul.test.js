const chai = require("chai");
const expect = chai.expect;
const calculateNumber = require("./0-calcul");

describe("calculateNumber", () => {
  it("should round both numbers down and return the sum", () => {
    expect(calculateNumber(1, 3)).to.equal(4);
  });

  it("should round both numbers up and return the sum", () => {
    expect(calculateNumber(1, 3.7)).to.equal(5);
  });

  it("should round one number down and one number up, and return the sum", () => {
    expect(calculateNumber(1.2, 3.7)).to.equal(5);
  });

  it("should work when one number is exactly .5", () => {
    expect(calculateNumber(1.5, 3.7)).to.equal(6);
  });
});
