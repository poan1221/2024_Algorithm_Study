function solution(arr, k) {
    const result = [];
    for (let num of arr) {
    if (!result.includes(num)) {
      result.push(num);
          if (result.length === k) break;
        }
    }

    while (result.length < k) {
    result.push(-1);
    }
    return result;
}