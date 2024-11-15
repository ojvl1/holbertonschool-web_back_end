const request = require("request");
const { expect } = require("chai");

describe("Index page", () => {
  const url = "http://localhost:7865/";

  it("should return the correct status code", (done) => {
    request(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it("should return the correct message", (done) => {
    request(url, (err, res, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
});

describe("Cart page", () => {
  const baseUrl = "http://localhost:7865/cart/";

  it("should return the correct status code and message for a valid cart ID", (done) => {
    request(`${baseUrl}12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("should return a 404 status code for an invalid cart ID", (done) => {
    request(`${baseUrl}hello`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it("should return a 404 status code for a missing cart ID", (done) => {
    request(`${baseUrl}`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
