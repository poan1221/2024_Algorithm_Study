function solution(s) {
    let transform = 0;
    let removeZero = 0;
    
    while (s !== "1") {
        transform++;
        
        let arr = s.split("");
        let ones = [];
        
        for (let ch of arr){
            if (ch === "0") removeZero++
            else ones.push(ch);
        }
        
        s = ones.length.toString(2);
    }
    
    return [transform, removeZero];
}