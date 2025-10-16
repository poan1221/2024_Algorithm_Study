function solution(k, score) {
const hall=  [];
  const ans= [];
  for (const s of score) {
    hall.push(s);
    hall.sort((a, b) => b - a);     // 내림차순
    if (hall.length > k) hall.length = k; // 상위 k개만 유지
    ans.push(hall[hall.length - 1]); // 최하위는 맨 끝
  }
  return ans;
}