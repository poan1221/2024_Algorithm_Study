function solution(arr) {
  let x = 0;

  while (true) {
    const next = arr.map(num => {
      if (num >= 50 && num % 2 === 0) return num / 2;
      if (num < 50 && num % 2 === 1) return num * 2 + 1;
      return num;
    });

    if (arr.every((v, i) => v === next[i])) break;

    arr = next;
    x++;
  }

  return x;
}
