import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

function generatePolynomial(coefficients: number[]): string {
  const terms: string[] = [];
  const degree = coefficients.length - 1;

  for (let i = 0; i < coefficients.length; ++i) {
    if (coefficients[i] === 0) continue;

    const currentDegree = degree - i;
    const absoluteCoefficient = Math.abs(coefficients[i]);
    let sign: string = "";

    if (coefficients[i] > 0 && terms.length !== 0) {
      sign = "+";
    } else if (coefficients[i] > 0 && terms.length === 0) {
      sign = "";
    } else if (coefficients[i] < 0) {
      sign = "-";
    }

    let term: string;
    if (currentDegree === 0) {
      term = `${sign}${absoluteCoefficient}`;
    } else {
      let coefficientStr = "";
      let variableStr = "";

      if (absoluteCoefficient === 1) {
        coefficientStr = ""
      } else {
        coefficientStr = `${absoluteCoefficient}`;
      }

      if (currentDegree === 1) {
        variableStr = "x";
      } else {
        variableStr = `x^${currentDegree}`;
      }
      term = `${sign}${coefficientStr}${variableStr}`;
    }
    terms.push(term);
  }

  return (terms.length !== 0 ? terms.join("") : "0");
}

function main() {
  const coefficients = input[1].split(" ").map((s) => parseInt(s));
  console.log(generatePolynomial(coefficients));
}
main();
