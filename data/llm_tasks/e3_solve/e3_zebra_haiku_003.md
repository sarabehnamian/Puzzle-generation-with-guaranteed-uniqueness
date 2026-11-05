# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01380-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, yellow, blue, white, green
- hobby: hiking, golf, tennis, painting, cooking
- job: pilot, teacher, doctor, farmer, baker
- pet: rabbit, cat, dog, bird, horse

Clues:
1. The owner of the bird lives somewhere to the left of whoever lives in the green house.
2. The dog owner enjoys tennis.
3. Whoever lives in the green house does not live next to the occupant of the yellow house.
4. The person who enjoys golf lives in one of the two end houses.
5. The occupant of the blue house enjoys tennis.
6. The owner of the rabbit does not live in the fifth house.
7. The doctor lives directly to the left of the person in the green house.
8. The farmer and the person in the red house live two houses apart.
9. The person who enjoys painting lives somewhere to the right of the golf enthusiast.
10. The farmer lives in the house just left of the one where the person who enjoys cooking lives.
11. The occupant of the yellow house is not the pilot.
12. The cat owner does not live next to the painting enthusiast.
13. The baker lives in the house just left of the one where the person who enjoys painting lives.
14. The teacher lives in the fourth house.
15. The person who keeps the dog works as the pilot.
16. The cooking enthusiast does not live in the first house.
17. There is exactly one house between the doctor and the person who enjoys tennis.
18. The doctor and the person in the yellow house are not neighbours.
19. The hiking enthusiast lives in the fourth house.
20. The teacher either enjoys hiking or enjoys tennis.
21. The occupant of the green house enjoys hiking.
22. The person in the green house works as the teacher.
23. Whoever lives in the blue house and the rabbit owner live two houses apart.
24. The owner of the rabbit lives in house 3.
25. The bird owner lives in the white house.
26. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
27. The farmer either keeps the cat or keeps the dog.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
