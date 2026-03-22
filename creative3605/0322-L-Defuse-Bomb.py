# Metadata
# Created: 2026-03-22T17:02:39 (UTC +08:00)
# Source: https://acm.creative3605.com/competition/2035365536273735680/problem/L
# Problem Title: Bomb Defusal
#
# Problem Description:
# A bomb defusal requires passing 5 sequential stages. Each stage presents 
# a display number (1-4) and 4 buttons with distinct labels (1-4). 
# You must identify the correct button to press based on the manual.
#
# Key Requirements:
# - Track the POSITION (1st, 2nd, 3rd, 4th from left) of the pressed button.
# - Track the LABEL (the actual number on the button) of the pressed button.
# - Incorrect presses cause immediate failure.
#
# Defusal Manual Summary:
# Stage 1:
#     If the display is 1, press the button in the second position.
#     If the display is 2, press the button in the second position.
#     If the display is 3, press the button in the third position.
#     If the display is 4, press the button in the fourth position.
# Stage 2:
#     If the display is 1, press the button labeled "4".
#     If the display is 2, press the button in the same position as you pressed in stage 1.
#     If the display is 3, press the button in the first position.
#     If the display is 4, press the button in the same position as you pressed in stage 1.
# Stage 3:
#     If the display is 1, press the button with the same label you pressed in stage 2.
#     If the display is 2, press the button with the same label you pressed in stage 1.
#     If the display is 3, press the button in the third position.
#     If the display is 4, press the button labeled "4".
# Stage 4:
#     If the display is 1, press the button in the same position as you pressed in stage 1.
#     If the display is 2, press the button in the first position.
#     If the display is 3, press the button in the same position as you pressed in stage 2.
#     If the display is 4, press the button in the same position as you pressed in stage 2.
# Stage 5:
#     If the display is 1, press the button with the same label you pressed in stage 1.
#     If the display is 2, press the button with the same label you pressed in stage 2.
#     If the display is 3, press the button with the same label you pressed in stage 4.
#     If the display is 4, press the button with the same label you pressed in stage 3.
#
# Constraints:
# - 5 stages total.
# - Labels on buttons are always a permutation of {1, 2, 3, 4}.
#
# Implementation Tip: 
# Store history in two arrays: `pos_history` and `label_history` (1-indexed 
# for clarity) to reference previous stages easily.

STAGE = 5

def main() -> None :
    t = int(input().rstrip())
    """number of test cases"""
    stages = []
    presses = [] 
    for _ in range(t):
        stages.clear()
        presses.clear()

        for i in range(STAGE) :
            stages.append(list(map(int, input().rstrip().split())))
            """stores every displaying number and button labels at every stage"""
    
        for i, stage in enumerate(stages) :
            if i == 0 :
                if stage[0] == 1 :
                    presses.append([2, stage[2]])
                    # Press the button in the second position
                else :
                    presses.append([stage[0], stage[stage[0]]])
                    # Press the button in the corresponding position
            elif i == 1 :
                if stage[0] == 1 :
                    presses.append([stage.index(4, 1), 4])
                    # Notice the searching must start from 1 because 0 is the displaying number
                    # Press the button labeled 4
                elif stage[0] == 2 or stage[0] == 4 :
                    presses.append([presses[0][0], stage[presses[0][0]]])
                    # Press the button in the same position as you pressed in stage 1
                elif stage[0] == 3 :
                    presses.append([1, stage[1]])
                    # Press the button in the first position
            elif i == 2 :
                if stage[0] == 1 :
                    presses.append([stage.index(presses[1][1], 1), presses[1][1]])
                    # Press the button with the same label you pressed in stage 2
                elif stage[0] == 2 :
                    presses.append([stage.index(presses[0][1], 1), presses[0][1]])
                    # Press the button with the same label you pressed in stage 1
                elif stage[0] == 3 :
                    presses.append([3, stage[3]])
                    # Press the button in the third position
                elif stage[0] == 4 :
                    presses.append([stage.index(4, 1), 4])
                    # Press the button labeled 4
            elif i == 3 :
                if stage[0] == 1 :
                    presses.append([presses[0][0], stage[presses[0][0]]])
                    # Press the button in the same position as you pressed in stage 1
                elif stage[0] == 2 :
                    presses.append([1, stage[1]])
                    # Press at first position
                elif stage[0] == 3 or stage[0] == 4 :
                    presses.append([presses[1][0], stage[presses[1][0]]])
                    # Press the button in the same position as you pressed in stage 2
            elif i == 4 :
                if stage[0] == 1 :
                    presses.append([stage.index(presses[0][1], 1), presses[0][1]])
                    # Press the button with the same label you pressed in stage 1.
                elif stage[0] == 2 :
                    presses.append([stage.index(presses[1][1], 1), presses[1][1]])
                    # Press the button with the same label you pressed in stage 2.
                elif stage[0] == 3 :
                    presses.append([stage.index(presses[3][1], 1), presses[3][1]])
                    # Press the button with the same label you pressed in stage 4.
                elif stage[0] == 4 :
                    presses.append([stage.index(presses[2][1], 1), presses[2][1]])
                    # Press the button with the same label you pressed in stage 3.
    
        for stage in presses :
            print(" ".join(map(str, stage)))

if __name__ == "__main__" :
    main()
