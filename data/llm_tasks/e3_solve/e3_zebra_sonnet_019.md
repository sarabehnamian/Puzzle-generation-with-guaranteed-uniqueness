# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_019.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01211

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, doctor, teacher, lawyer
- color: green, yellow, white, purple, blue
- drink: water, coffee, cocoa, milk, juice
- hobby: painting, golf, hiking, tennis, cooking

Clues:
1. The person who enjoys cooking either drinks cocoa or drinks milk.
2. The lawyer lives directly to the left of the doctor.
3. The coffee drinker enjoys golf.
4. Whoever lives in the blue house works as the baker.
5. The farmer drinks milk.
6. The coffee drinker lives next to whoever lives in the yellow house.
7. The person who enjoys tennis lives somewhere to the right of whoever lives in the white house.
8. The person in the blue house lives immediately to the right of the cocoa drinker.
9. The person who drinks juice lives directly to the left of the occupant of the purple house.
10. The person who enjoys hiking works as the teacher.
11. Whoever lives in the purple house lives directly to the left of the person who enjoys cooking.
12. There is exactly one house between the person who enjoys hiking and the person who enjoys tennis.
13. The baker and the water drinker live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
