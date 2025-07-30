function solution(myString) {
    return [...myString].map(char => {
        if (char === "a") return "A";
        if (char !== "A") return char.toLowerCase();
        return char;
    }).join('');
}