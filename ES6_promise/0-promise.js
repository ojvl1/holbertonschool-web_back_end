export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const value = 1;
    if (value) {
      resolve();
    } else {
      reject();
    }
  });
}
