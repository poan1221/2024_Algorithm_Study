function solution(s, skip, index) {
    const skipSet = new Set(skip.split(''));
  let ans = '';

  for (const ch of s) {
    let code = ch.charCodeAt(0);
    let moved = 0;

    while (moved < index) {
      code++;
      if (code > 122) code = 97;

      const next = String.fromCharCode(code);
      if (!skipSet.has(next)) {
        moved++;
      }
    }
    ans += String.fromCharCode(code);
  }

  return ans;
}