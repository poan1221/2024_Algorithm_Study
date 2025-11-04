function solution(n) {
    let count = 0;
    for (let d = 1; d*d <= n; d++){
        if (n % d === 0){
            const d2 = n/d;
            if (d % 2 === 1) count++;
            if (d2 !== d && d2 % 2 === 1) count++;
        }
    }
    return count;
}