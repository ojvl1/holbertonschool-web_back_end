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
});

describe("Available payments page", () => {
  const url = "http://localhost:7865/available_payments";

  it("should return the correct status code", (done) => {
    request(url, (err, res, body) => {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      expect(res.statusCode).to.equal(200);
      done();
    });
  });
});

describe("Login page", () => {
  const url = "http://localhost:7865/login";

  it("should return the correct message with valid userName", (done) => {
    const options = {
      url,
      method: "POST",
      json: { userName: "Betty" },
    };
    request(options, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Welcome Betty");
      done();
    });
  });

  it("should return 400 status code when userName is missing", (done) => {
    const options = {
      url,
      method: "POST",
      json: {},
    };
    request(options, (err, res, body) => {
      expect(res.statusCode).to.equal(400);
      expect(body).to.equal("Missing userName");
      done();
    });
  });
});
