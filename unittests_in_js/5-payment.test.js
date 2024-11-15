const sinon = require("sinon");
const sendPaymentRequestToAPI = require("./5-payment");
const { expect } = require("chai");

describe("sendPaymentRequestToAPI", function () {
  let consoleSpy;

  beforeEach(function () {
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(function () {
    consoleSpy.restore();
  });

  it("should log 'The total is: 120' for inputs 100 and 20", function () {
    sendPaymentRequestToAPI(100, 20);
    expect(consoleSpy.calledOnceWithExactly("The total is: 120")).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it("should log 'The total is: 20' for inputs 10 and 10", function () {
    sendPaymentRequestToAPI(10, 10);
    expect(consoleSpy.calledOnceWithExactly("The total is: 20")).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
