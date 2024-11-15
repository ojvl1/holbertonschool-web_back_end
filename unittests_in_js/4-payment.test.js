const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToAPI = require("./4-payment");
const { expect } = require("chai");

describe("sendPaymentRequestToApi", function () {
  it("...", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const consoleSpy = sinon.spy(console, "log");
    sendPaymentRequestToAPI(100, 20);
    expect(stub.calledOnceWithExactly("SUM", 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly("The total is: 10")).to.be.true;
    stub.restore();
    consoleSpy.restore();
  });
});
