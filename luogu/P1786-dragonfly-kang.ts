import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

const CharacterEnum = Object.freeze({
  "BangZhu": 6,
  "FuBangZhu": 5,
  "HuFa": 4,
  "ZhangLao": 3,
  "TangZhu": 2,
  "JingYing": 1,
  "BangZhong": 0,
});

type CharacterString = keyof typeof CharacterEnum;

interface Member {
  name: string;
  character: CharacterString;
  contribution: number;
  level: number;
  originalIndex: number;
}

function main() {
  const memberNum = input[0]
    .split(" ")
    .map((s) => parseInt(s))[0];
  const members: Member[] = [];
  let memberBZ: Member = {
    name: "",
    character: "BangZhong",
    contribution: 0,
    level: 0,
    originalIndex: 0,
  };
  const memberFBZs: Member[] = [];

  for (let i = 0; i < memberNum; ++i) {
    const info = input[i + 1].split(" ");
    switch (info[1] as CharacterString) {
      case "BangZhu" :
        memberBZ = {
          name: info[0],
          character: info[1] as CharacterString,
          contribution: parseInt(info[2]),
          level: parseInt(info[3]),
          originalIndex: i
        };
        break;
      case "FuBangZhu" :
        memberFBZs.push({
          name: info[0],
          character: info[1] as CharacterString,
          contribution: parseInt(info[2]),
          level: parseInt(info[3]),
          originalIndex: i
        });
        break;
      default :
        members.push({
          name: info[0],
          character: info[1] as CharacterString,
          contribution: parseInt(info[2]),
          level: parseInt(info[3]),
          originalIndex: i
        });
        break;
    }
  }

  const sortedMembers = members.sort((a, b) => {
    if (b.contribution !== a.contribution) {
      return b.contribution - a.contribution;
    }
    return a.originalIndex - b.originalIndex;
  });

  for (let i = 0; i < sortedMembers.length; ++i) {
    if (i < 2) {
      sortedMembers[i].character = "HuFa";
    } else if (i < 6) {
      sortedMembers[i].character = "ZhangLao";
    } else if (i < 13) {
      sortedMembers[i].character = "TangZhu";
    } else if (i < 38) {
      sortedMembers[i].character = "JingYing";
    } else {
      sortedMembers[i].character = "BangZhong";
    }
  }
  const showedMembers = [memberBZ, ...memberFBZs, ...sortedMembers].sort(
    (a, b) => {
      if (CharacterEnum[a.character] !== CharacterEnum[b.character]) {
        return CharacterEnum[b.character] - CharacterEnum[a.character];
      }
      if (a.level !== b.level) {
        return b.level - a.level;
      }
      return a.originalIndex - b.originalIndex;
    }
  );
  for (let i = 0; i < showedMembers.length; ++i) {
    console.log(`${showedMembers[i].name} ${showedMembers[i].character} ${showedMembers[i].level}`);
  }
}
main();
