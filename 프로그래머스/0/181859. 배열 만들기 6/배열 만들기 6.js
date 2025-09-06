function solution(arr) {
    
    const stk = [];
    for (let i = 0; i < arr.length; i++) {
        const a = arr[i];
        if (stk.length === 0) {
            stk.push(a);
        } else if (stk[stk.length-1] === a){
            stk.pop();
        } else {
            stk.push(a);
        }
    }
    return stk.length === 0 ? [-1] : stk;
}