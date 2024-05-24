function solution(name, yearning, photo) {
    // 이름과 그리움 점수를 매핑하는 딕셔너리 생성
    const yearningMap = {};
    for (let i = 0; i < name.length; i++) {
        yearningMap[name[i]] = yearning[i];
    }

    // 각 사진에 대해 추억 점수를 계산
    const result = photo.map(persons => {
        let totalScore = 0;
        for (let person of persons) {
            if (yearningMap[person]) {
                totalScore += yearningMap[person];
            }
        }
        return totalScore;
    });

    return result;
}