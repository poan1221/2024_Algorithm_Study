function solution(x, n) {
    return Array.from({ length: n }, (_, index) => x * (index + 1));
}