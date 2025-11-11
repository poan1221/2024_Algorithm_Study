function solution(s) {
  const n = s.length;
  if (n % 2 === 1) return 0;

  const cnt = { '(':0, ')':0, '[':0, ']':0, '{':0, '}':0 };
  for (const ch of s) cnt[ch]++;
  if (cnt['('] !== cnt[')'] || cnt['['] !== cnt[']'] || cnt['{'] !== cnt['}']) return 0;

  const open = new Set(['(', '[', '{']);
  const pair = { ')':'(', ']':'[', '}':'{' };

  const isValid = (str) => {
    const stack = [];
    for (const ch of str) {
      if (open.has(ch)) stack.push(ch);
      else {
        if (!stack.length || stack[stack.length - 1] !== pair[ch]) return false;
        stack.pop();
      }
    }
    return stack.length === 0;
  };

  let ans = 0;
  for (let x = 0; x < n; x++) {
    const rotated = s.slice(x) + s.slice(0, x);
    if (isValid(rotated)) ans++;
  }
  return ans;
}