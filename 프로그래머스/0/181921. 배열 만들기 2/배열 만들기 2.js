function solution(l, r) {
  const result = [];

  for (let i = l; i <= r; i++) {
    if ([...String(i)].every((ch) => ch === '0' || ch === '5')) {
      result.push(i);
    }
  }

  return result.length > 0 ? result : [-1];
}