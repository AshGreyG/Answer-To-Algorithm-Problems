import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

function main() {
  const n = parseInt(input[0]);
  const a = 2n ** BigInt(n) - 1n;
  const s = a.toString();
  const sLast500 = s.slice(s.length < 500 ? 0 : s.length - 500);
  let prefix = "";
  for (let i = 0; i < 500 - sLast500.length; ++i) {
    prefix += "0";
  }
  const prefixsLast500 = prefix.concat(sLast500);

  console.log(s.length);
  let line = "";
  for (let i = 1; i <= 500; ++i) {
    if (i % 50 === 0) {
      line += prefixsLast500[i - 1];
      console.log(line);
      line = "";
    } else {
      line += prefixsLast500[i - 1];
    }
  }
}
main();
