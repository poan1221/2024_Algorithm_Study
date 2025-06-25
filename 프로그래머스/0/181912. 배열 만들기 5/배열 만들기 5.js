function solution(intStrs, k, s, l) {
    const parts = intStrs.map(str => Number(str.slice(s, s+l)));
    
    return parts.filter(num => num > k);
}