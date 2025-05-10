function solution(code) {
    let ret = "";
    let mode = 0;
    
    [...code].forEach((char, i) => {
        if (char === "1") mode = 1 - mode; //모드 변경
        else if ( (mode === 0 && i % 2 === 0) || (mode === 1 && i % 2 === 1)) {
            // 0 이고 짝수 또는 1이고 홀수 일 때, 저장
            ret += char;
        }
    })
    
    return ret || "EMPTY"; // 빈문자열이면 EMPTY
}