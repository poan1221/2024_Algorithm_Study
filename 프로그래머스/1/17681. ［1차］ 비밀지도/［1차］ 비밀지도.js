function solution(n, arr1, arr2) {
    const result = [];

    for (let i = 0; i < n; i++) {
        // 두 배열의 값을 OR 연산한 결과를 2진수 문자열로 변환
        const mapRow = (arr1[i] | arr2[i]).toString(2).padStart(n, '0');

        // 2진수 문자열을 #과 공백으로 변환
        const mapRowStr = mapRow.replace(/1/g, '#').replace(/0/g, ' ');

        // 결과 배열에 추가
        result.push(mapRowStr);
    }

    return result;
}