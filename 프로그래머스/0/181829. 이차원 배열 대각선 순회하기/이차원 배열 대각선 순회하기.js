function solution(board, k) {
  const n = board.length;
  const m = board[0].length;
  let sum = 0;

  for (let i = 0; i < n; i++) {
    const maxJ = Math.min(m - 1, k - i);
    if (maxJ < 0) break;
    for (let j = 0; j <= maxJ; j++) sum += board[i][j];
  }

  return sum;
}