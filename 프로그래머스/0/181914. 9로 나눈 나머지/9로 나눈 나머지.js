function solution(number) {
    const sum = [...number].reduce((acc,digit) => acc + Number(digit), 0);
    return sum % 9;
}