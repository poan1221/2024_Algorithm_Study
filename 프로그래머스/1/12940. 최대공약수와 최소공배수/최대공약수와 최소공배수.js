function solution(a, b) {
    const gcd = (x, y) => {
        while (y !== 0) {
            let temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

    const lcm = (x, y, gcd) => {
        return (x * y) / gcd;
    }

    const gcdValue = gcd(a, b);
    const lcmValue = lcm(a, b, gcdValue);

    return [gcdValue, lcmValue];
}