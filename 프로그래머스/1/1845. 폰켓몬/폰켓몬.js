function solution(nums) {
  const n = nums.length;
  const maxCanTake = n / 2;

  const kinds = new Set(nums).size;
    
  return Math.min(kinds, maxCanTake);
}