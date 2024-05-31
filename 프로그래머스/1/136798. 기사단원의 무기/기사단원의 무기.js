function solution(number, limit, power) {
    // 약수 개수를 계산하는 함수
    function countDivisors(n) {
        let count = 0;
        for (let i = 1; i <= Math.sqrt(n); i++) {
            if (n % i === 0) {
                count++;
                if (i !== n / i) {
                    count++;
                }
            }
        }
        return count;
    }

    let totalWeight = 0;
    for (let i = 1; i <= number; i++) {
        const divisorsCount = countDivisors(i);
        if (divisorsCount > limit) {
            totalWeight += power;
        } else {
            totalWeight += divisorsCount;
        }
    }

    return totalWeight;
}