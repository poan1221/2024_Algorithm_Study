function solution(my_string) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const counts = Array(52).fill(0);
    
  my_string.split("").map((n) => {
    counts[alphabet.indexOf(n)] += 1
  });

  return counts;
}
