# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_010.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00668

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, purple, green, blue, yellow
- hobby: chess, hiking, cooking, golf, painting
- pet: bird, horse, fish, cat, dog
- drink: cocoa, coffee, juice, milk, tea

Clues:
1. The dog owner and the person in the yellow house live two houses apart.
2. Whoever lives in the red house and the person who drinks tea live two houses apart.
3. The cocoa drinker lives in one of the two end houses.
4. The person who drinks juice keeps the fish.
5. The occupant of the yellow house enjoys painting.
6. The cocoa drinker does not live next to the person who enjoys cooking.
7. There is exactly one house between the occupant of the red house and the occupant of the yellow house.
8. The occupant of the red house lives immediately to the right of the person who keeps the bird.
9. The cat owner drinks milk.
10. Whoever lives in the blue house enjoys hiking.
11. The owner of the cat lives in the green house.
12. The owner of the fish enjoys chess.
13. The coffee drinker either enjoys cooking or enjoys painting.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
