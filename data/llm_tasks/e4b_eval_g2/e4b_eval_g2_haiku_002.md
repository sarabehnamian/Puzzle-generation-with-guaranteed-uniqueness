# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The cooking enthusiast and the person in the white house live two houses apart.
2. The person who keeps the cat lives in the red house.
3. The lawyer lives immediately to the right of the farmer.
4. The doctor keeps the fish.
5. The cocoa drinker and the person who drinks milk live two houses apart.
6. The doctor lives in the house just left of the one where the person who enjoys hiking lives.
7. The person in the yellow house and whoever lives in the red house are not neighbours.
8. The Brit lives in the purple house.
9. The person who keeps the dog lives directly to the left of the doctor.
10. The occupant of the white house lives in the house just left of the one where the person who drinks juice lives.
11. The teacher lives immediately to the right of the owner of the cat.
12. The person who drinks water keeps the dog.
13. The person in the green house and the tennis enthusiast are not neighbours.
14. The golf enthusiast lives in the house just left of the one where the chess enthusiast lives.
15. The person who keeps the horse and the milk drinker live two houses apart.
16. The person in the blue house lives in the sixth house.
17. The baker keeps the dog.
18. The owner of the cat and the person who drinks tea live in adjacent houses.
19. The Swede keeps the rabbit.
20. The Dane and the dog owner live in adjacent houses.
21. The German lives somewhere to the left of the fish owner.
22. The person in the green house and the Norwegian are neighbours.
23. The Brit lives in one of the two end houses.
24. The person in the green house works as the lawyer.
25. The person who enjoys golf lives in one of the two end houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
