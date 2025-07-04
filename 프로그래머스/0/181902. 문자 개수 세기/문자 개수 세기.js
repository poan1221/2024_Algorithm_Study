function solution(my_string) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const counts = Array(52).fill(0);

  for (let ch of my_string) {
    const idx = alphabet.indexOf(ch);
    if (idx !== -1) counts[idx]++;
  }

  return counts;
}
