import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

function factorialDigitFrequency(n: number, digit: number) {
  let factorial: bigint = 1n;
  let count = 0;
  for (let i = 1; i <= n; ++i) {
    factorial *= BigInt(i);
  }
  const factorialStr = factorial.toString();
  for (let i = 0; i < factorialStr.length; ++i) {
    if (factorialStr[i] === digit.toString()) count++;
  }
  return count;
}

function main() {
  const linesNum = parseInt(input[0]);
  for (let i = 1; i <= linesNum; ++i) {
    const [n, a] = input[i]
      .split(" ")
      .map((s) => parseInt(s)) as [number, number];
    console.log(factorialDigitFrequency(n, a));
  }
}
main();
