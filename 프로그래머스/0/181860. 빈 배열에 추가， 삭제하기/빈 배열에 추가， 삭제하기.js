function solution(arr, flag) {
    const X = [];
    for (let i = 0; i < arr.length; i++){
        const a = arr[i];
        if (flag[i]) {
            for (let k = 0; k < a * 2; k++) X.push(a);
        } else {
            X.length = Math.max(0, X.length - a);
        }
    }
    return X;
}