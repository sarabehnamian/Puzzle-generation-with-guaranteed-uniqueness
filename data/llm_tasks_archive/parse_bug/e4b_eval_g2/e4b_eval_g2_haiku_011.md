# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_011.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The occupant of the white house lives directly to the left of the person who drinks juice.
2. The dog owner lives in the house just left of the one where the doctor lives.
3. Whoever lives in the blue house lives in the sixth house.
4. Whoever lives in the yellow house drinks water.
5. The golf enthusiast lives in a lower-numbered house than the tennis enthusiast.
6. The Dane and the person who keeps the dog are neighbours.
7. The owner of the cat and the tea drinker live in adjacent houses.
8. There is exactly one house between the cooking enthusiast and the person in the white house.
9. The owner of the dog works as the baker.
10. The cat owner lives in the red house.
11. The owner of the horse either drinks cocoa or drinks water.
12. Whoever lives in the yellow house does not live next to the person in the blue house.
13. The German lives somewhere to the left of the fish owner.
14. The Brit lives in one of the two end houses.
15. The golf enthusiast lives directly to the left of the chess enthusiast.
16. The painting enthusiast is the Norwegian.
17. The farmer lives directly to the left of the lawyer.
18. The horse owner does not enjoy cooking.
19. The occupant of the green house does not live next to the person who enjoys tennis.
20. The owner of the dog drinks water.
21. There is exactly one house between the person who keeps the horse and the milk drinker.
22. The Swede lives in one of the two end houses.
23. The cat owner lives in the house just left of the one where the teacher lives.
24. The Swede keeps the rabbit.
25. The hiking enthusiast lives immediately to the right of the doctor.
26. The doctor keeps the fish.
27. The rabbit owner lives next to whoever lives in the red house.
28. Whoever lives in the green house and the Norwegian are neighbours.
29. The person who drinks cocoa and the milk drinker live two houses apart.
30. Whoever lives in the green house works as the lawyer.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
