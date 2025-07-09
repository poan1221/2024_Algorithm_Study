function solution(arr, intervals) {
  const [[a1, b1], [a2, b2]] = intervals;
  const part1 = arr.slice(a1, b1 + 1);
  const part2 = arr.slice(a2, b2 + 1);
  
  return [...part1, ...part2]; 
}