function solution(numbers, hand) {
    // 키패드의 각 위치를 정의
    const keyPad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    };
    
    // 현재 손의 위치를 초기화
    let leftHand = keyPad['*'];
    let rightHand = keyPad['#'];

    let result = '';

    for (let number of numbers) {
        if ([1, 4, 7].includes(number)) {
            // 왼쪽 열
            result += 'L';
            leftHand = keyPad[number];
        } else if ([3, 6, 9].includes(number)) {
            // 오른쪽 열
            result += 'R';
            rightHand = keyPad[number];
        } else {
            // 가운데 열
            const targetPos = keyPad[number];

            const leftDist = Math.abs(targetPos[0] - leftHand[0]) + Math.abs(targetPos[1] - leftHand[1]);
            const rightDist = Math.abs(targetPos[0] - rightHand[0]) + Math.abs(targetPos[1] - rightHand[1]);

            if (leftDist < rightDist) {
                result += 'L';
                leftHand = targetPos;
            } else if (leftDist > rightDist) {
                result += 'R';
                rightHand = targetPos;
            } else {
                if (hand === 'right') {
                    result += 'R';
                    rightHand = targetPos;
                } else {
                    result += 'L';
                    leftHand = targetPos;
                }
            }
        }
    }

    return result;
}
