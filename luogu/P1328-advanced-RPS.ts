import { readFileSync } from "node:fs";
import process from "node:process";

const data = readFileSync("./dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

const GestureEnum = Object.freeze({
  Scissors: 0,
  Rock: 1,
  Paper: 2,
  Lizard: 3,
  Spock: 4
});

type GestureType
  = typeof GestureEnum extends Readonly<infer O>
    ? O[keyof O]
    : never;

const result: Array<0 | 1 | 2> = [];

function main() {
  const [n, na, nb] = input[0].split(/\s+/).map((s) => parseInt(s));
  const gesturesA: GestureType[]
    = input[1].split(/\s+/).map((s) => parseInt(s) as GestureType);
  const gesturesB: GestureType[]
    = input[2].split(/\s+/).map((s) => parseInt(s) as GestureType);

  for (let i = 0; i < n; ++i) {
    const currentGetureA = gesturesA[i % na]; 
    const currentGetureB = gesturesB[i % nb]; 

    if (currentGetureA === currentGetureB) {
      result.push(0);
    } else switch ([currentGetureA, currentGetureB].join(".")) {
      case [GestureEnum.Scissors, GestureEnum.Rock    ].join(".") : result.push(2); break;
      case [GestureEnum.Scissors, GestureEnum.Paper   ].join(".") : result.push(1); break;
      case [GestureEnum.Scissors, GestureEnum.Lizard  ].join(".") : result.push(1); break;
      case [GestureEnum.Scissors, GestureEnum.Spock   ].join(".") : result.push(2); break;

      case [GestureEnum.Rock,     GestureEnum.Scissors].join(".") : result.push(1); break;
      case [GestureEnum.Rock,     GestureEnum.Paper   ].join(".") : result.push(2); break;
      case [GestureEnum.Rock,     GestureEnum.Lizard  ].join(".") : result.push(1); break;
      case [GestureEnum.Rock,     GestureEnum.Spock   ].join(".") : result.push(2); break;

      case [GestureEnum.Paper,    GestureEnum.Scissors].join(".") : result.push(2); break;
      case [GestureEnum.Paper,    GestureEnum.Rock    ].join(".") : result.push(1); break;
      case [GestureEnum.Paper,    GestureEnum.Lizard  ].join(".") : result.push(2); break;
      case [GestureEnum.Paper,    GestureEnum.Spock   ].join(".") : result.push(1); break;

      case [GestureEnum.Lizard,   GestureEnum.Scissors].join(".") : result.push(2); break;
      case [GestureEnum.Lizard,   GestureEnum.Rock    ].join(".") : result.push(2); break;
      case [GestureEnum.Lizard,   GestureEnum.Paper   ].join(".") : result.push(1); break;
      case [GestureEnum.Lizard,   GestureEnum.Spock   ].join(".") : result.push(1); break;

      case [GestureEnum.Spock,    GestureEnum.Scissors].join(".") : result.push(1); break;
      case [GestureEnum.Spock,    GestureEnum.Rock    ].join(".") : result.push(1); break;
      case [GestureEnum.Spock,    GestureEnum.Paper   ].join(".") : result.push(2); break;
      case [GestureEnum.Spock,    GestureEnum.Lizard  ].join(".") : result.push(2); break;
    }
  }

  console.log(
    result.filter((r) => r === 1).length + " " +
    result.filter((r) => r === 2).length
  );
  process.exit();
}

main();
