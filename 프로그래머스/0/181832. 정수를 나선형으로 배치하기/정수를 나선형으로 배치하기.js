function solution(n) {
  const a = Array.from({ length: n }, () => Array(n).fill(0));
  const dx = [0, 1, 0, -1];   // → ↓ ← ↑
  const dy = [1, 0, -1, 0];
  let x = 0, y = 0, d = 0;

  for (let v = 1; v <= n * n; v++) {
    a[x][y] = v;
    let nx = x + dx[d], ny = y + dy[d];
    if (nx < 0 || nx >= n || ny < 0 || ny >= n || a[nx][ny] !== 0) {
      d = (d + 1) % 4;                 // 회전
      nx = x + dx[d]; ny = y + dy[d];
    }
    x = nx; y = ny;
  }
  return a;
}