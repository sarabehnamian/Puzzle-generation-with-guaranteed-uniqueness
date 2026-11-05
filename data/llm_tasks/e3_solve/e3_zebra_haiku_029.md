# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_029.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00551-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Brit, Spaniard, Swede
- color: white, green, red, purple, yellow
- pet: horse, dog, cat, rabbit, fish
- job: doctor, lawyer, teacher, pilot, farmer

Clues:
1. The German lives in the fourth house.
2. The Norwegian lives in the third house.
3. The German works as the farmer.
4. The doctor and the pilot live in adjacent houses.
5. The owner of the dog lives directly to the left of the person who keeps the rabbit.
6. The person who keeps the dog and the pilot are neighbours.
7. There is exactly one house between the Brit and the German.
8. There is exactly one house between the person who keeps the fish and the pilot.
9. The rabbit owner lives in the second house.
10. The Norwegian lives immediately to the right of the Brit.
11. The person who keeps the dog lives directly to the left of the person in the white house.
12. The farmer either is the German or is the Norwegian.
13. The Brit and the owner of the dog are different people.
14. There is exactly one house between the cat owner and the occupant of the green house.
15. The Brit either works as the pilot or works as the teacher.
16. The doctor lives in the house just left of the one where whoever lives in the yellow house lives.
17. The teacher keeps the horse.
18. The Swede lives in house 5.
19. The person in the purple house lives in house 1.
20. The Spaniard and the doctor are different people.
21. The dog owner lives in the first house.
22. The person who keeps the horse either lives in the green house or lives in the yellow house.
23. The Brit lives next to the lawyer.
24. Whoever lives in the red house lives in the house just left of the one where the farmer lives.
25. The person in the white house lives somewhere to the left of the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
