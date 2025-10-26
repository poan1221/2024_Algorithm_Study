function solution(n){
    return [...String(n)].reduce((a, b) => a + +b, 0);
}