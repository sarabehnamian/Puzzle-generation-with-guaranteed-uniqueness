# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_023.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01256

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, hiking, tennis, painting
- nationality: Swede, Spaniard, German, Norwegian, Dane
- color: white, purple, red, green, yellow
- job: pilot, lawyer, doctor, baker, farmer

Clues:
1. There is exactly one house between the person who enjoys cooking and the pilot.
2. The person in the red house either enjoys hiking or enjoys painting.
3. The Dane lives somewhere to the left of whoever lives in the red house.
4. The lawyer and the Spaniard live two houses apart.
5. The doctor lives in the purple house.
6. The Swede does not live in the fifth house.
7. The hiking enthusiast works as the lawyer.
8. The Dane and the German are neighbours.
9. The doctor lives immediately to the right of the occupant of the yellow house.
10. The farmer lives directly to the left of the German.
11. The German lives immediately to the right of the person who enjoys tennis.
12. The occupant of the green house lives in the house just left of the one where the lawyer lives.
13. The lawyer and the painting enthusiast live in adjacent houses.
14. Whoever lives in the yellow house is the Dane.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
