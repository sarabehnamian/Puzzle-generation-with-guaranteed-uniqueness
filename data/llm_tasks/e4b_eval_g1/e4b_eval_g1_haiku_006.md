# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_006.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The occupant of the blue house lives in one of the two end houses.
2. The cooking enthusiast and the person in the white house live two houses apart.
3. The doctor lives directly to the left of the person who enjoys hiking.
4. The person in the red house keeps the cat.
5. The lawyer lives immediately to the right of the farmer.
6. The person who keeps the cat lives directly to the left of the teacher.
7. The occupant of the white house lives directly to the left of the juice drinker.
8. The Brit lives in the leftmost house.
9. The occupant of the purple house lives in the house just left of the one where the German lives.
10. The lawyer lives in the green house.
11. The golf enthusiast lives at one end of the row.
12. The Dane and the owner of the dog live in adjacent houses.
13. The doctor lives immediately to the right of the owner of the dog.
14. The owner of the dog works as the baker.
15. The fish owner lives somewhere to the right of the German.
16. The cocoa drinker and the milk drinker live two houses apart.
17. The person who keeps the cat and the person who drinks tea are neighbours.
18. Whoever lives in the green house does not live next to the person who enjoys tennis.
19. The person who keeps the dog drinks water.
20. The golf enthusiast lives directly to the left of the chess enthusiast.
21. The occupant of the white house lives somewhere to the right of whoever lives in the yellow house.
22. The Swede keeps the rabbit.
23. The owner of the fish works as the doctor.
24. The occupant of the green house and the Norwegian are neighbours.
25. The horse owner and the person who drinks milk live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
