function solution(numbers, n) {
    let sum = 0;
    for (const num of numbers) {
        sum += num;
        if (sum > n) return sum;
    };
}