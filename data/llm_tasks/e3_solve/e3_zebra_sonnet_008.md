# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_008.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00369

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, cooking, painting, golf, tennis
- drink: cocoa, coffee, juice, milk, tea
- color: yellow, purple, blue, red, white
- pet: horse, bird, fish, rabbit, dog

Clues:
1. The occupant of the white house lives directly to the left of the owner of the horse.
2. The person in the blue house lives in a lower-numbered house than the person who keeps the dog.
3. The person who enjoys chess lives in the first house.
4. The person who drinks cocoa keeps the dog.
5. The juice drinker lives in the yellow house.
6. The person who keeps the fish lives in a lower-numbered house than the milk drinker.
7. The person who keeps the bird drinks juice.
8. The person in the yellow house lives in the house just left of the one where whoever lives in the red house lives.
9. The person who keeps the dog enjoys cooking.
10. The occupant of the red house lives in the house just left of the one where the person who drinks coffee lives.
11. The owner of the rabbit lives directly to the left of the person who enjoys painting.
12. The golf enthusiast lives in the yellow house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
