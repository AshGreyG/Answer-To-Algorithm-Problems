import { readFileSync } from "node:fs";

const data = readFileSync("/dev/stdin");
const input: string[] = data.toString("ascii").trim().split("\n");

interface Items {
  /**
   * @field processOrder : The processing order of an item, like [1, 2] indicates
   * this item should be processed by machine 1 and then machine 2
   */
  processOrder?: number[];
  /**
   * @field processTime: The processing times of corresponding machine processing
   * with this item.
   */
  processTime?: number[];
}

function continuousElementIndex<T>(
  array: T[],
  element: T
): Array<[number, number]> {
  let recordIndex = 0;
  let recordLength = 0;
  const result: Array<[number, number]> = [];

  for (let i = 0; i < array.length; ++i) {
    if (array[i] === element) {
      recordLength++;
    } else {
      recordIndex = i;
      if (recordLength !== 0 && recordIndex !== 0) {
        result.push([recordIndex - recordLength, recordLength]);
      }
      recordLength = 0;
    }
  }
  if (recordLength !== 0 && recordIndex !== 0) {
    result.push([array.length - recordLength, recordLength]);
  }
  return result;
}

function leastProcessTime(
  machinesNum: number,
  itemsNum: number,
  itemsProcessOrder: number[],
  items: Items[]
): number {
  const machineSchedules: number[][] = [];
  for (let i = 0; i < machinesNum; ++i) machineSchedules.push([]);

  for (let i = 0; i < machinesNum * itemsNum; ++i) {
    const currentItem = itemsProcessOrder[i]; // notice it begins with 1
    // currentItem is the item now processing, and it is read from itemsProcessOrder
    const currentItemProcess = itemsProcessOrder
      .filter((value, index) => (value === currentItem && index < i))
      .length + 1;
    // currentItemProcess is the order of the item now processing, the order
    // should be got from the itemsProcessOrder
    const currentMachine = (items[currentItem - 1] as Required<Items>)
      .processOrder[currentItemProcess - 1];
    // currentMachine is the machine now processing
    const currentMachineSchedule = machineSchedules[currentMachine - 1];
    // currentMachineSchedule is the current schedule of current machine
    const currentTime = (items[currentItem - 1] as Required<Items>)
      .processTime[currentItemProcess - 1];
    // currentTime is the needed time of current (machine-item) pair
    const currentVacantIndexMap = continuousElementIndex(currentMachineSchedule, 0);
    const lastTime = Math.max(
      ...machineSchedules.map((arr) => arr.lastIndexOf(currentItem) + 1)
    );
    // Notice lastTime has been added 1 so it starts from 1

    if (
      currentMachineSchedule.length < currentTime ||
      Math.max(
        ...currentVacantIndexMap.map(
          (t) => t[0] + t[1] - Math.max(t[0], lastTime)
        )
      ) < currentTime
    ) {
      // [+] If the length of currentMachineSchedule is less than needed time of
      //     current processing step, then we need to add the job at the end of
      //     currentMachineSchedule
      // [+] If length of every continuous sub-array consisting of 0 is less
      //     than needed time of current processing step, then we need to add
      //     the job at the end of currentMachineSchedule
      //
      //  000111100222220000333
      //  ↑     ↑       ↑
      //  |   lastTime  |
      //  |             +- t[0] = 14, t[1] = 4, t[0] + t[1] - lastTime = 11
      //  +- t[0] = 0, t[1] = 3, lastTime = 7, t[0] + t[1] - lastTime = -4
      //  Notice lastTime is 1-based and t[0] is 0-based

      const initialLength = currentMachineSchedule.length;
      for (let j = 0; j < lastTime - initialLength; ++j) {
          currentMachineSchedule.push(0);
      }
      for (let j = 0; j < currentTime; ++j) {
        currentMachineSchedule.push(currentItem);
      }
    } else {
      for (let j = 0; j < currentVacantIndexMap.length; ++j) {
        if (
          currentVacantIndexMap[j][0] + currentVacantIndexMap[j][1] - lastTime >= currentTime
        ) {
          for (let k = 0; k < currentTime; ++k) {
            currentMachineSchedule[
              Math.max(currentVacantIndexMap[j][0], lastTime)
              + k] = currentItem;
          }
          break;
        }
      }
    }
  }
  return Math.max(...machineSchedules.map((arr) => arr.length));
}

function main() {
  const [machinesNum, itemsNum] = input[0]
    .trim()
    .split(" ")
    .map((s) => parseInt(s));
  const itemsProcessOrder = input[1]
    .trim()
    .split(" ")
    .map((s) => parseInt(s));
  const items: Items[] = [];

  for (let i = 0; i < itemsNum; ++i) {
    items.push({
      processOrder: input[i + 2]
        .trim()
        .split(" ")
        .map((s) => parseInt(s))
    });
  }
  for (let i = 0; i < itemsNum; ++i) {
    items[i].processTime = input[i + itemsNum + 2]
      .trim()
      .split(" ")
      .map((s) => parseInt(s));
  }
  console.log(leastProcessTime(
    machinesNum, 
    itemsNum,
    itemsProcessOrder,
    items
  ));
}
main();
