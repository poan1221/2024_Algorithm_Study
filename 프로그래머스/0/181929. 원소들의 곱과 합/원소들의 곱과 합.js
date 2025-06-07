function solution(num_list) {
  const sum = num_list.reduce((acc, cur) => acc + cur, 0);
  const product = num_list.reduce((acc, cur) => acc * cur, 1);

  return product < sum ** 2 ? 1 : 0;
}