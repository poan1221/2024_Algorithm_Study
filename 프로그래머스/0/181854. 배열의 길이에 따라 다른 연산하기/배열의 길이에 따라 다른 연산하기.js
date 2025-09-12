function solution(arr, n) {
    const isEven = arr.length % 2 === 0;
    
    return arr.map((val,idx) => {
        return (!isEven && idx % 2 === 0) || (isEven && idx % 2 === 1) ? val + n : val;
    })
}