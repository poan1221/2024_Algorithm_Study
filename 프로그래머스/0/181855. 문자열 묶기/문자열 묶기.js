function solution(strArr) {
    const counts = {};
  
  for (let str of strArr) {
    const len = str.length;
    counts[len] = (counts[len] || 0) + 1;
  }

  return Math.max(...Object.values(counts));
}