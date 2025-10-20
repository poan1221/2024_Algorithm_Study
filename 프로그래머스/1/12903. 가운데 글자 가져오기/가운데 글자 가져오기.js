function solution(s) {
    const len = s.length;
  const mid = Math.floor(len / 2);

  return len % 2 === 1 ? s[mid] : s[mid - 1] + s[mid];
}