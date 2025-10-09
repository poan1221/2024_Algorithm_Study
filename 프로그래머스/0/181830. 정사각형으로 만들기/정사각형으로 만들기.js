function solution(arr) {
    const row = arr.length;
  const col = arr[0].length;

  if (row > col) {
    return arr.map(r => [...r, ...Array(row - col).fill(0)]);
  }

  if (col > row) {
    const zeroRow = Array(col).fill(0);
    return [...arr, ...Array(col - row).fill(null).map(() => [...zeroRow])];
  }

  return arr;
}