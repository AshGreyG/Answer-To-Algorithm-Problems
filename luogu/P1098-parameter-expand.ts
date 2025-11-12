import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

function expand(target: string, params: number[]): string {
  // Notice parameters as a param name is invalid and dangerous

  const replaced = (left: string, right: string): string => {
    let temp = "";
    if (params[0] === 1) {
      for (
        let i = left.toLowerCase().charCodeAt(0) + 1;
        i <= right.toLowerCase().charCodeAt(0) - 1;
        i++
      ) {
        temp += String.fromCharCode(i).repeat(params[1]);
      }
    } else if (params[0] === 2) {
      for (
        let i = left.toUpperCase().charCodeAt(0) + 1;
        i <= right.toUpperCase().charCodeAt(0) - 1;
        i++
      ) {
        temp += String.fromCharCode(i).repeat(params[1]);
      }
    } else {
      for (let i = left.charCodeAt(0) + 1; i <= right.charCodeAt(0) - 1; i++) {
        temp += "*".repeat(params[1]);
      }
    }

    return (
      params[2] === 2
        ? [...temp].reverse().join("")
        : temp
    );
  }

  let result = "";
  for (let i = 0; i < target.length; ++i) {
    if (
      target[i] === "-" && 
      i >= 1 &&
      i <= target.length - 2 &&
      ((
        target[i - 1].charCodeAt(0) < target[i + 1].charCodeAt(0) && 
        target[i - 1].charCodeAt(0) >= 97 &&
        target[i - 1].charCodeAt(0) <= 122 &&
        target[i + 1].charCodeAt(0) >= 97 &&
        target[i + 1].charCodeAt(0) <= 122
       ) || (
        target[i - 1].charCodeAt(0) < target[i + 1].charCodeAt(0) && 
        target[i - 1].charCodeAt(0) >= 48 &&
        target[i - 1].charCodeAt(0) <= 57 &&
        target[i + 1].charCodeAt(0) >= 48 &&
        target[i + 1].charCodeAt(0) <= 57
       )
      )
    ) {
      if (target[i - 1].charCodeAt(0) + 1 === target[i + 1].charCodeAt(0)) {
        continue;
      } else {
        result += replaced(target[i - 1], target[i + 1]);
      }
    } else {
      result += target[i];
    }
  }
  return result;
}

function main() {
  const params = input[0].split(" ").map((s) => parseInt(s));
  const target = input[1];
  console.log(expand(target, params));
}
main();
