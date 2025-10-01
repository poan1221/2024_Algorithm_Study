function solution(picture, k) {
  const result = [];

  for (const row of picture) {
    // 가로로 k배 늘리기
    const expandedRow = [...row].map(ch => ch.repeat(k)).join("");

    // 세로로 k배 늘리기
    for (let i = 0; i < k; i++) {
      result.push(expandedRow);
    }
  }

  return result;
}