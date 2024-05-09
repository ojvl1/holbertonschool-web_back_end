export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const idx of array) {
    let value = array[idx];
    array[idx] = appendString + value;
    newArray.push(value);
  }

  return array;
}
