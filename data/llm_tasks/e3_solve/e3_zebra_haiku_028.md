# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_028.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00790

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, golf, tennis, cooking
- job: doctor, teacher, farmer, baker, pilot
- drink: tea, coffee, juice, cocoa, water
- color: blue, yellow, green, white, red

Clues:
1. The person in the green house lives in the fifth house.
2. The person who enjoys cooking and the water drinker live in adjacent houses.
3. The person who drinks water lives in the house just left of the one where the occupant of the white house lives.
4. The tennis enthusiast lives directly to the left of the golf enthusiast.
5. Whoever lives in the blue house and whoever lives in the yellow house live two houses apart.
6. The tea drinker lives in the house just left of the one where whoever lives in the yellow house lives.
7. There is exactly one house between the person who drinks coffee and the person who drinks water.
8. The teacher lives in house 4.
9. The water drinker lives immediately to the right of the baker.
10. The doctor lives in the last house.
11. The person who enjoys golf lives in house 5.
12. The pilot drinks juice.
13. The farmer and the person who enjoys hiking live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
