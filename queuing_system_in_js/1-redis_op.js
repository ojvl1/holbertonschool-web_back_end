import { createClient, print } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a value in Redis for the given key
 * @param {string} schoolName - The key
 * @param {string} value - The value to set
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting value for ${schoolName}: ${err.message}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

/**
 * Retrieves the value for a given key from Redis and logs it
 * @param {string} schoolName - The key to fetch the value for
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error fetching value for ${schoolName}: ${err.message}`);
    } else {
      console.log(value || "School");
    }
  });
}

// Function calls
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
