function solution(myString) {
    return [...myString].map(ch => ch < "l" ? "l" : ch).join("");
}