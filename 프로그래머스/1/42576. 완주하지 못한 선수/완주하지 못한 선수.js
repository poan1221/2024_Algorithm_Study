function solution(participant, completion) {
    const participantMap = new Map();

    // participant 배열을 순회하며 해시 테이블에 저장
    for (let name of participant) {
        if (participantMap.has(name)) {
            participantMap.set(name, participantMap.get(name) + 1);
        } else {
            participantMap.set(name, 1);
        }
    }

    // completion 배열을 순회하며 해시 테이블에서 제거
    for (let name of completion) {
        if (participantMap.get(name) === 1) {
            participantMap.delete(name);
        } else {
            participantMap.set(name, participantMap.get(name) - 1);
        }
    }

    // 해시 테이블에 남아 있는 이름을 찾기
    for (let [name, count] of participantMap) {
        if (count > 0) {
            return name;
        }
    }

    return null; // 모든 선수들이 완주한 경우, 주어진 조건에서는 발생하지 않음
}
