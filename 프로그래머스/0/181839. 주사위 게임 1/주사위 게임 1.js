function solution(a, b) {
    const isAOdd = a % 2 === 1;
    const isBOdd = b % 2 === 1;
    
    return isAOdd && isBOdd ? a * a + b * b : isAOdd || isBOdd ? 2 * (a + b) : Math.abs(a - b);
}