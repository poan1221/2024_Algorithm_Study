function solution(s) {
    let lastSeen = {};  // 문자의 마지막 위치를 기록하는 객체
    let result = [];    // 결과 배열

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (lastSeen.hasOwnProperty(char)) {
            // 현재 위치와 마지막 위치의 차이를 결과에 추가
            result.push(i - lastSeen[char]);
        } else {
            // 처음 등장한 문자는 -1을 결과에 추가
            result.push(-1);
        }
        // 현재 문자의 마지막 위치를 업데이트
        lastSeen[char] = i;
    }
    
    return result;
}