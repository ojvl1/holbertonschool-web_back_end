export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { message: "Succesfull" };
      resolve(data);
    }, 1000);
  });
}

getResponseFromAPI()
  .then(data => log(data.message))
  .catch(error => console.error(error));
