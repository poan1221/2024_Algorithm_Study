function solution(dartResult) {
    // 1. Extract individual dart throws using regex
    const dartPattern = /(\d{1,2}[SDT][*#]?)/g;
    const darts = dartResult.match(dartPattern);

    // 2. Initialize scores array
    const scores = [];

    // 3. Process each dart throw
    darts.forEach((dart, i) => {
        // Extract score, bonus, and option using regex
        const scorePattern = /(\d{1,2})([SDT])([*#]?)/;
        const [, scoreStr, bonus, option] = dart.match(scorePattern);
        let score = parseInt(scoreStr, 10);

        // Calculate the base score according to the bonus
        if (bonus === 'S') {
            score = Math.pow(score, 1);
        } else if (bonus === 'D') {
            score = Math.pow(score, 2);
        } else if (bonus === 'T') {
            score = Math.pow(score, 3);
        }

        // Apply options if any
        if (option === '*') {
            score *= 2;
            if (i > 0) {
                scores[i - 1] *= 2;
            }
        } else if (option === '#') {
            score *= -1;
        }

        // Append the score to the array
        scores.push(score);
    });

    // 4. Calculate the total score
    const totalScore = scores.reduce((sum, current) => sum + current, 0);
    return totalScore;
}