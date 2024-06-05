function solution(numbers) {
    const sums = new Set(); // 중복을 방지하기 위해 Set 사용

    // 두 개의 수를 뽑아 더하는 모든 조합 찾기
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            sums.add(numbers[i] + numbers[j]);
        }
    }

    // Set을 배열로 변환하고 오름차순으로 정렬
    return Array.from(sums).sort((a, b) => a - b);
}