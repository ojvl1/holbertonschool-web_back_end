export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  let result = [];
  for (let value of set) {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.lenght));
    }
  }
  return result.join('-');
}
