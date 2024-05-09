export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const idx of array) {
    let value = idx;
    value = appendString + value;
    newArray.push(value);
  }

  return newArray;
}
