function solution(n, left, right) {
  const answer = [];

  for (let idx = left; idx <= right; idx++) {
    const row = Math.floor(idx / n);
    const col = idx % n;
    answer.push(Math.max(row, col) + 1);
  }

  return answer;
}