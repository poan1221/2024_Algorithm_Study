function solution(myString, pat) {
    const swapped = [...myString].map(ch => ch === "A" ? "B" : "A").join("");
    
    return swapped.includes(pat) ? 1 : 0;
}