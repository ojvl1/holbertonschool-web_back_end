export default function hasValuesFromArray(set, array) {
  const mySet = new Set(array);
  return mySet.has(set);
}
