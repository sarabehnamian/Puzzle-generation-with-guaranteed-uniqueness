# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_haiku_007.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The occupant of the yellow house lives in house 3.
2. The Dane and the owner of the dog live in adjacent houses.
3. Whoever lives in the green house does not live next to the tennis enthusiast.
4. There is exactly one house between the person who enjoys cooking and the person in the white house.
5. The German lives in a lower-numbered house than the owner of the fish.
6. The person who enjoys golf lives directly to the left of the chess enthusiast.
7. The juice drinker lives immediately to the right of the occupant of the white house.
8. The person who keeps the dog works as the baker.
9. The lawyer lives immediately to the right of the farmer.
10. The cocoa drinker and the person who drinks milk live two houses apart.
11. The owner of the cat lives in the red house.
12. The teacher lives immediately to the right of the owner of the cat.
13. The person who enjoys golf lives in a lower-numbered house than the person who enjoys cooking.
14. The doctor keeps the fish.
15. The cat owner and the tea drinker live in adjacent houses.
16. The person in the purple house enjoys golf.
17. There is exactly one house between the horse owner and the milk drinker.
18. The person who keeps the dog lives in the house just left of the one where the doctor lives.
19. The dog owner drinks water.
20. The person in the blue house lives at one end of the row.
21. The Swede keeps the rabbit.
22. The doctor lives directly to the left of the hiking enthusiast.
23. The person in the green house works as the lawyer.
24. The occupant of the green house lives next to the Norwegian.
25. The Brit lives in the first house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
