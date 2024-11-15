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

  it("should handle other requests gracefully", (done) => {
    request(`${url}random`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
