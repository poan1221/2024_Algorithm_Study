function solution(A,B){
    const a = [...A].sort((x,y) => x - y);
    const b = [...B].sort((x,y) => y - x);
    
    let sum = 0;
    for (let i = 0; i < a.length; i++){
        sum += a[i] * b[i]
    }
    
    return sum;
}