const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToAPI = require("./3-payment");
const { expect } = require("chai");

describe("sendPaymentRequestToApi", function () {
  it("...", function () {
    const spy = sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToAPI(100, 20);
    expect(spy.calledOnceWithExactly("SUM", 100, 20)).to.be.true;
    spy.restore();
  });
});
