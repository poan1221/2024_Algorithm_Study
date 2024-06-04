function solution(n) {
    // 1. n을 3진법으로 변환
    let ternary = n.toString(3);
    
    // 2. 변환된 3진법 숫자를 뒤집기
    let reversedTernary = '';
    for (let i = ternary.length - 1; i >= 0; i--) {
        reversedTernary += ternary[i];
    }
    
    // 3. 뒤집힌 3진법 숫자를 10진법으로 변환
    let result = parseInt(reversedTernary, 3);
    
    return result;
}