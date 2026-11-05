# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00383

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, red, blue, yellow
- drink: tea, juice, milk, coffee, cocoa
- hobby: cooking, painting, hiking, chess, golf
- pet: dog, cat, fish, bird, rabbit

Clues:
1. The fish owner does not live in the red house.
2. The person who keeps the rabbit lives in a lower-numbered house than the golf enthusiast.
3. The cocoa drinker lives next to the rabbit owner.
4. Whoever lives in the blue house does not live next to the person who keeps the cat.
5. The person in the yellow house either keeps the cat or keeps the dog.
6. Whoever lives in the green house lives in a lower-numbered house than the occupant of the red house.
7. The person who enjoys painting lives in the green house.
8. The person who keeps the bird and the tea drinker live two houses apart.
9. The fish owner and the rabbit owner are not neighbours.
10. The chess enthusiast and the cocoa drinker live two houses apart.
11. The person who drinks juice either lives in the blue house or lives in the purple house.
12. The person who drinks milk keeps the cat.
13. The owner of the rabbit lives immediately to the right of the coffee drinker.
14. The person who drinks juice lives directly to the left of the cooking enthusiast.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
