# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_011.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01132

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, red, yellow
- job: baker, doctor, teacher, farmer, pilot
- nationality: Norwegian, Brit, Dane, Spaniard, German
- hobby: painting, hiking, chess, golf, tennis

Clues:
1. The hiking enthusiast either works as the baker or works as the farmer.
2. The person who enjoys golf is the Norwegian.
3. There is exactly one house between the person who enjoys golf and the person who enjoys painting.
4. The person in the green house works as the teacher.
5. The chess enthusiast lives in the leftmost house.
6. The person who enjoys hiking is the Dane.
7. The person in the yellow house works as the pilot.
8. The Spaniard lives in house 4.
9. The German is not the doctor.
10. The person in the green house either is the Brit or is the Dane.
11. Whoever lives in the red house lives next to the occupant of the yellow house.
12. The farmer lives in the middle house.
13. The person in the white house lives immediately to the right of whoever lives in the blue house.
14. The painting enthusiast lives in one of the two end houses.
15. The Norwegian lives somewhere to the right of the occupant of the green house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
