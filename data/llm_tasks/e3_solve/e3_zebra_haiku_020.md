# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_020.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00230

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, green, yellow, red
- job: pilot, baker, doctor, teacher, lawyer
- nationality: Swede, Spaniard, Brit, German, Dane
- hobby: painting, tennis, golf, chess, cooking

Clues:
1. The teacher lives in the fifth house.
2. The Brit and the person in the red house are neighbours.
3. Whoever lives in the green house is not the German.
4. The cooking enthusiast lives directly to the left of the teacher.
5. Whoever lives in the purple house lives directly to the left of the Dane.
6. The Dane enjoys painting.
7. The occupant of the yellow house enjoys chess.
8. The person in the green house lives immediately to the right of the Brit.
9. The Dane and the pilot are not neighbours.
10. The doctor and the Swede live two houses apart.
11. The doctor lives in house 2.
12. The painting enthusiast lives in the last house.
13. The baker lives at one end of the row.
14. The golf enthusiast lives in the leftmost house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
