function solution(brown, yellow) {
  const total = brown + yellow;

  for (let innerH = 1; innerH * innerH <= yellow; innerH++) {
    if (yellow % innerH !== 0) continue;

    const innerW = Math.floor(yellow / innerH);
    const w = innerW + 2;
    const h = innerH + 2;

    if (w * h === total) {
      return w >= h ? [w, h] : [h, w];
    }
  }
  return [];
}