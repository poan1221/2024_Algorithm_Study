function solution(array, commands) {
    const result = [];

    // commands 배열을 순회하면서 각 명령을 처리
    for (const command of commands) {
        const [i, j, k] = command;  // 명령을 i, j, k로 디스트럭처링 할당
        const slicedArray = array.slice(i - 1, j);  // 배열 자르기 - 인덱스는 0부터 시작하므로 -1
        const sortedArray = slicedArray.sort((a, b) => a - b);  // 자른 배열을 정렬
        result.push(sortedArray[k - 1]);  // k번째 숫자를 결과 배열에 추가, 인덱스는 0부터 시작하므로 -1
    }

    return result;
}