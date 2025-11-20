function solution(n, words) {
  const used = new Set(); 
  used.add(words[0]);   

  for (let i = 1; i < words.length; i++) {
    const prev = words[i - 1];
    const curr = words[i];

    const isRepeated = used.has(curr);
    const isWrongChain = prev[prev.length - 1] !== curr[0];

    if (isRepeated || isWrongChain) {
      const player = (i % n) + 1;          
      const turn = Math.floor(i / n) + 1;   
      return [player, turn];
    }

    used.add(curr);
  }

  return [0, 0];
}