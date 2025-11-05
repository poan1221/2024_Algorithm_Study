    function popcount(x) {
      let c = 0;
      while (x > 0) {
        c += x & 1;
        x >>= 1;
      }
      return c;
    }

function solution(n) {
      const target = popcount(n);
      let x = n + 1;
      while (true) {
        if (popcount(x) === target) return x;
        x++;
      }
    
}