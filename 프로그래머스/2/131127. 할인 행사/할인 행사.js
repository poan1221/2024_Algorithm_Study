function solution(want, number, discount) {
  const wantMap = new Map();

  for (let i = 0; i < want.length; i++) {
    wantMap.set(want[i], number[i]);
  }

  let answer = 0;

  for (let i = 0; i <= discount.length - 10; i++) {
    const windowMap = new Map();

    for (let j = 0; j < 10; j++) {
      const item = discount[i + j];
      windowMap.set(item, (windowMap.get(item) || 0) + 1);
    }

    let ok = true;
    for (const [item, cnt] of wantMap) {
      if ((windowMap.get(item) || 0) !== cnt) {
        ok = false;
        break;
      }
    }

    if (ok) {
      answer++;
    }
  }

  return answer;
}