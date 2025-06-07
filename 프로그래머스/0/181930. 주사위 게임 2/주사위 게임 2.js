function solution(a, b, c) {
    const sum = a + b + c
    const square = a**2 + b**2 + c**2;
    const cube = a**3 + b**3 + c**3;
    
    if ( a ===b && b === c) {
        return sum * square * cube;
    } else if (a ===b || b === c || a === c){
        return sum * square;
    } else {
        return sum;
    }
}