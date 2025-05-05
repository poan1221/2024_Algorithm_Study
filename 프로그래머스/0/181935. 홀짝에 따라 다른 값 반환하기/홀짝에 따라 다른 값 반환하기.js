function solution(n) {
  let result = 0;

  if (n % 2 === 1) {
    // 홀수일 경우: 홀수 합
    for (let i = 1; i <= n; i += 2) {
      result += i;
    }
  } else {
    // 짝수일 경우: 짝수 제곱의 합
    for (let i = 2; i <= n; i += 2) {
      result += i * i;
    }
  }

  return result;
}
