function solution(citations) {
  citations.sort((a, b) => b - a);

  let h = 0;

  for (let i = 0; i < citations.length; i++) {
    const count = i + 1; 
    if (citations[i] >= count) {
      h = count; 
    } else {
      break;
    }
  }

  return h;
}