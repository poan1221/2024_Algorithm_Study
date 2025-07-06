function solution(my_string, indices) {
  const removeSet = new Set(indices);

  return [...my_string]
    .filter((_, idx) => !removeSet.has(idx))
    .join('');
}