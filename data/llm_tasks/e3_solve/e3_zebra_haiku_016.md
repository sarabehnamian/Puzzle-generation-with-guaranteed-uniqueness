# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_016.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00284

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, hiking, tennis, cooking
- pet: bird, fish, cat, dog, rabbit
- color: yellow, blue, red, white, purple
- drink: tea, milk, water, coffee, cocoa

Clues:
1. The person who drinks coffee lives next to the person who enjoys tennis.
2. The person who drinks water lives in the leftmost house.
3. The person who keeps the bird and the person who enjoys cooking are neighbours.
4. The owner of the fish drinks tea.
5. Whoever lives in the purple house enjoys hiking.
6. The cocoa drinker and the owner of the rabbit are different people.
7. The owner of the cat and the occupant of the yellow house live in adjacent houses.
8. The person who drinks tea and whoever lives in the yellow house live two houses apart.
9. The occupant of the red house lives in the house just left of the one where the person in the white house lives.
10. The person who keeps the bird lives in one of the two end houses.
11. The person who drinks coffee lives somewhere to the right of the person who enjoys chess.
12. The person who drinks milk and the occupant of the red house live two houses apart.
13. Whoever lives in the purple house drinks water.
14. The person in the blue house lives directly to the left of the coffee drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
