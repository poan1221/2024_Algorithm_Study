function solution(phone_number) {
    const len = phone_number.length;
    const masked = '*'.repeat(len - 4) + phone_number.slice(-4);
    return masked;
}