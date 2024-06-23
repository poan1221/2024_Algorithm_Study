function solution(arr) {
    // 배열의 길이가 1인 경우 [-1] 반환
    if (arr.length === 1) {
        return [-1];
    }

    // 배열에서 가장 작은 수 찾기
    const min = Math.min(...arr);

    // 가장 작은 수를 제외한 새로운 배열 만들기
    const result = arr.filter(num => num !== min);

    return result;
}