import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

// This problem consists of definite finite state machine + fast-slow pointer

interface PositionVector {
  x: number;
  y: number;
  direction: "north" | "south" | "east" | "west";
}
type Direction = PositionVector["direction"];
interface StateMachineInfo {
  vectorRecords: PositionVector[];
  loopStartAnchor: number;
  loopLength: number;
}

const map: ("." | "*")[][] = [];

const stateMachineCow: StateMachineInfo = {
  vectorRecords: [],
  loopStartAnchor: 0,
  loopLength: 0
};
const stateMachineJohn: StateMachineInfo = {
  vectorRecords: [],
  loopStartAnchor: 0,
  loopLength: 0
};

/**
 * This function check is the position (x, y) out of bounds or occupied by
 * a barrier.
 */
function checkPositionValid(
  map: ("." | "*")[][], 
  x: number,
  y: number
): boolean {
  if (x < 0 || x >= map[0].length) return false;
  if (y < 0 || y >= map.length) return false;
  return map[y][x] === ".";
}

/**
 * It generates state machine (including vector records, an array recording
 * paths cow or John walks through / loop start anchor / loop length)
 */
function generateStateMachine(
  map: ("." | "*")[][],
  targetStateMachine: StateMachineInfo
): void {
  const clockwise = (direction: Direction): Direction => {
    switch (direction) {
      case "north" : return "east";
      case "east"  : return "south";
      case "south" : return "west";
      case "west"  : return "north";
    }
  }
  const targetPath = targetStateMachine.vectorRecords;
  const vectorsSet: Set<string> = new Set();
  vectorsSet.add(JSON.stringify(targetPath[targetPath.length - 1]));

  let exitFlag = false;

  while (!exitFlag) {
    const lastVector = targetPath[targetPath.length - 1];
    const nextVector: PositionVector = {...lastVector};
    let nextX = 0;
    let nextY = 0;

    switch (lastVector.direction) {
      case "north" :
        nextX = lastVector.x;
        nextY = lastVector.y - 1;
        break;
      case "south" :
        nextX = lastVector.x;
        nextY = lastVector.y + 1;
        break;
      case "east" :
        nextX = lastVector.x + 1;
        nextY = lastVector.y;
        break;
      case "west" :
        nextX = lastVector.x - 1;
        nextY = lastVector.y;
        break;
    }
    if (checkPositionValid(map, nextX, nextY)) {
      nextVector.x = nextX;
      nextVector.y = nextY;
      nextVector.direction = lastVector.direction;
    } else {
      nextVector.x = lastVector.x;
      nextVector.y = lastVector.y;
      nextVector.direction = clockwise(lastVector.direction);
    }
    if (vectorsSet.has(JSON.stringify(nextVector))) {
      exitFlag = true;
      for (let i = 0; i < targetPath.length; ++i) {
        if (
          targetPath[i].direction === nextVector.direction &&
          targetPath[i].x === nextVector.x &&
          targetPath[i].y === nextVector.y
        ) {
          targetStateMachine.loopStartAnchor = i;
          targetStateMachine.loopLength = targetPath.length - i;
        }
      }
    } else {
      vectorsSet.add(JSON.stringify(nextVector));
      targetPath.push({...nextVector});
    }
  }
}

function stateMachineEncounterTime(
  first: StateMachineInfo, 
  second: StateMachineInfo
): number {
  const GCD = (a: number, b: number): number => {
    let absA = Math.abs(a);
    let absB = Math.abs(b);
    while (absB !== 0) {
      const temp = absB;
      absB = absA % absB;
      absA = temp;
    }
    return absA;
  }
  const LCM = (a: number, b: number): number => Math.abs(a) * Math.abs(b) / GCD(a, b);

  const k = Math.max(
    first.vectorRecords.length,
    second.vectorRecords.length
  ) + LCM(first.loopLength, second.loopLength);

  for (let i = 0; i < k; ++i) {
    let indexFir = 0;
    let indexSec = 0;

    if (i < first.loopStartAnchor) {
      indexFir = i;
    } else {
      indexFir =
        first.loopStartAnchor +
        ((i - first.loopStartAnchor) % first.loopLength);
    }

    if (i < second.loopStartAnchor) {
      indexSec = i;
    } else {
      indexSec =
        second.loopStartAnchor +
        ((i - second.loopStartAnchor) % second.loopLength);
    }

    if (
      first.vectorRecords[indexFir].x === second.vectorRecords[indexSec].x &&
      first.vectorRecords[indexFir].y === second.vectorRecords[indexSec].y
    ) {
      return i
    }
  }
  return -1;
}

function main() {
  for (let i = 0; i < input.length; ++i) {
    const lineMap: ("." | "*")[] = [];
    for (let j = 0; j < input[i].length; ++j) {
      switch (input[i][j]) {
        case ".":
          lineMap.push(".");
          break;
        case "*":
          lineMap.push("*");
          break;
        case "C":
          lineMap.push(".");
          stateMachineCow.vectorRecords.push({
            x: j,
            y: i,
            direction: "north",
          });
          break;
        case "F":
          lineMap.push(".");
          stateMachineJohn.vectorRecords.push({
            x: j,
            y: i,
            direction: "north",
          });
          break;
      }
    }
    map.push([...lineMap]);
  }
  generateStateMachine(map, stateMachineCow);
  generateStateMachine(map, stateMachineJohn);

  const time = stateMachineEncounterTime(stateMachineCow, stateMachineJohn);
  console.log(time === -1 ? 0 : time);
}
main();
