# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_004.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00414-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, doctor, pilot, baker
- hobby: tennis, painting, cooking, hiking, golf
- color: red, blue, white, green, yellow
- nationality: Spaniard, Swede, German, Dane, Brit

Clues:
1. The Dane lives in the house just left of the one where the Swede lives.
2. The Dane and the farmer live in adjacent houses.
3. The occupant of the yellow house does not live in the third house.
4. The person in the blue house and whoever lives in the white house are not neighbours.
5. The occupant of the green house lives at one end of the row.
6. The person who enjoys painting lives in the yellow house.
7. The person who enjoys cooking either is the German or is the Swede.
8. The occupant of the green house enjoys cooking.
9. The Swede and the occupant of the yellow house are neighbours.
10. The baker and the painting enthusiast live in adjacent houses.
11. The Brit enjoys hiking.
12. The lawyer and the Spaniard live two houses apart.
13. The occupant of the white house lives directly to the left of the pilot.
14. The pilot lives somewhere to the right of whoever lives in the green house.
15. The Spaniard lives in the yellow house.
16. The pilot and the Swede live in adjacent houses.
17. The pilot lives in house 5.
18. The Dane is not the doctor.
19. Whoever lives in the blue house lives immediately to the right of the person who enjoys cooking.
20. Whoever lives in the white house enjoys tennis.
21. The pilot lives somewhere to the right of the Dane.
22. The Spaniard does not live in house 3.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
