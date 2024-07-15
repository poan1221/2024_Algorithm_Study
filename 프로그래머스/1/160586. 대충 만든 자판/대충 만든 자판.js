function solution(keymap, targets) {
    let minKeyPresses = {};

    for (let keyIdx = 0; keyIdx < keymap.length; keyIdx++) {
        let keys = keymap[keyIdx];
        for (let pressCount = 0; pressCount < keys.length; pressCount++) {
            let char = keys[pressCount];
            if (!minKeyPresses[char]) {
                minKeyPresses[char] = pressCount + 1;
            } else {
                minKeyPresses[char] = Math.min(minKeyPresses[char], pressCount + 1);
            }
        }
    }

    let results = [];

    for (let i = 0; i < targets.length; i++) {
        let target = targets[i];
        let totalPresses = 0;
        for (let j = 0; j < target.length; j++) {
            let char = target[j];
            if (minKeyPresses[char]) {
                totalPresses += minKeyPresses[char];
            } else {
                totalPresses = -1;
                break;
            }
        }
        results.push(totalPresses);
    }

    return results;
}
