function solution(arr) {
    const n = arr.length;
    let pow = 1;
    while (pow < n) {
        pow *= 2;
    }
    const zeros = pow - n;
    return arr.concat(Array(zeros).fill(0));
}