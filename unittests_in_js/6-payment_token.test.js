const getPaymentTokenFromAPI = require("./6-payment_token");
const { expect } = require("chai");

describe("getPaymentTokenFromAPI", function () {
  it("should resolve with the correct object when success is true", function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({
          data: "Successful response from the API",
        });
        done(); // Signal that the test is complete
      })
      .catch((error) => done(error)); // Handle unexpected errors
  });
});
