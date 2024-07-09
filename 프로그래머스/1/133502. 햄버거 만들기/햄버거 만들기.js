function solution(ingredient) {
    let stack = [];
    let count = 0;
    const hamburger = [1, 2, 3, 1];

    for (let ing of ingredient) {
        stack.push(ing);
        // 스택의 마지막 4개 요소가 햄버거 순서와 일치하는지 확인
        if (stack.length >= 4 && stack.slice(-4).toString() === hamburger.toString()) {
            count += 1;
            // 햄버거를 만들었으므로, 스택의 마지막 4개 요소 제거
            stack.splice(-4);
        }
    }

    return count;
}
