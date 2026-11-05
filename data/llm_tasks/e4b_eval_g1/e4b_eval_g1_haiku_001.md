# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The person in the green house lives next to the Norwegian.
2. The German lives somewhere to the left of the person who keeps the fish.
3. The person who keeps the dog works as the baker.
4. The person who enjoys golf lives at one end of the row.
5. There is exactly one house between the person who drinks cocoa and the milk drinker.
6. The hiking enthusiast lives immediately to the right of the doctor.
7. The person in the green house works as the lawyer.
8. Whoever lives in the green house and the person who enjoys tennis are not neighbours.
9. The Brit lives in the first house.
10. The person who drinks water keeps the dog.
11. The owner of the horse and the milk drinker live two houses apart.
12. The Swede keeps the rabbit.
13. Whoever lives in the blue house lives in the last house.
14. The cat owner and the tea drinker live in adjacent houses.
15. The person who enjoys golf lives directly to the left of the person who enjoys chess.
16. The teacher lives immediately to the right of the cat owner.
17. The owner of the fish works as the doctor.
18. The lawyer lives immediately to the right of the farmer.
19. The Dane lives next to the dog owner.
20. Whoever lives in the white house lives in the house just left of the one where the person who drinks juice lives.
21. The person in the red house keeps the cat.
22. The person in the yellow house lives in house 3.
23. The owner of the dog lives in the house just left of the one where the doctor lives.
24. There is exactly one house between the cooking enthusiast and the occupant of the white house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
