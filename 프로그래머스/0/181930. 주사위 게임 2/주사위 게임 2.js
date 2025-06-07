function solution(a, b, c) {
    const sum = a + b + c
    const square = a**2 + b**2 + c**2;
    const cube = a**3 + b**3 + c**3;

    const dsttCnt = new Set([a, b, c]).size;
    
    switch(dsttCnt) {
        case 1 : return sum * square * cube;
        case 2 : return sum * square;
        case 3 : return sum;
    }
}