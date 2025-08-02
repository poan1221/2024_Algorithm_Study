const solution = (myString, pat) => {
  let count = 0;
  let index = 0;

  while (true) {
    index = myString.indexOf(pat, index);
    if (index === -1) break;
    count++;
    index += 1;
  }

  return count;
};
