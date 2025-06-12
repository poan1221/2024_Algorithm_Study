function solution(n, control) {
    const move = { w: 1, s: -1, d: 10, a: -10 }
    
    for ( let c of control){
        n += move[c];
    }
    
    return n;
}