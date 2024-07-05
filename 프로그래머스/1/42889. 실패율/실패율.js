function solution(N, stages) {
    // 각 스테이지에 도달한 플레이어 수를 저장할 배열
    const stageCounts = Array(N + 2).fill(0);

    // 각 스테이지에 도달한 플레이어 수 계산
    stages.forEach(stage => {
        stageCounts[stage]++;
    });

    // 실패율을 계산하여 저장할 배열
    const failRates = [];
    let totalPlayers = stages.length;

    for (let i = 1; i <= N; i++) {
        if (totalPlayers === 0) {
            failRates.push([i, 0]);
        } else {
            const failRate = stageCounts[i] / totalPlayers;
            failRates.push([i, failRate]);
        }
        totalPlayers -= stageCounts[i];
    }

    // 실패율을 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 오름차순 정렬
    failRates.sort((a, b) => {
        if (b[1] === a[1]) {
            return a[0] - b[0];
        } else {
            return b[1] - a[1];
        }
    });

    // 정렬된 스테이지 번호만 추출하여 반환
    return failRates.map(item => item[0]);
}
