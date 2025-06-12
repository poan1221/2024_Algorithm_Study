function solution(numLog) {
  const commandMap = {
    "1": "w",
    "-1": "s",
    "10": "d",
    "-10": "a"
  };

  let result = "";

  for (let i = 1; i < numLog.length; i++) {
    const diff = numLog[i] - numLog[i - 1];
    result += commandMap[diff];
  }

  return result;
}
