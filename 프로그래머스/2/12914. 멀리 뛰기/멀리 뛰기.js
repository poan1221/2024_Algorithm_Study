function solution(n) {
  const MOD = 1234567;

  if (n === 1) return 1;
  if (n === 2) return 2;

  let prev2 = 1;
  let prev1 = 2;
  let current = 0;

  for (let i = 3; i <= n; i++) {
    current = (prev1 + prev2) % MOD;
    
    prev2 = prev1;
    prev1 = current;
  }

  return current;
}