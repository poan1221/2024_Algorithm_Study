function solution(n, m, section) {
    let count = 0;  // 롤러 사용 횟수
    let i = 0;      // 현재 검사할 section의 인덱스

    while (i < section.length) {
        // 롤러를 현재 section에서 사용할 수 있는 최대 범위까지 사용
        let currentStart = section[i];
        let currentEnd = currentStart + m - 1;
        
        // 롤러가 커버하는 범위 내에 있는 구역들은 모두 스킵
        while (i < section.length && section[i] <= currentEnd) {
            i++;
        }
        
        // 롤러 사용 횟수 증가
        count++;
    }
    
    return count;
}