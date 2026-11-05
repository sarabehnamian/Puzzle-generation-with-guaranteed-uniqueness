# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_007.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, juice, coffee
- color: white, green, purple, yellow, red, blue
- pet: dog, cat, bird, rabbit, horse, fish
- hobby: chess, hiking, tennis, cooking, painting, golf
- job: farmer, lawyer, pilot, baker, doctor, teacher
- nationality: German, Norwegian, Brit, Swede, Spaniard, Dane

Clues:
1. The person who enjoys chess and the juice drinker live in adjacent houses.
2. The doctor either is the Brit or is the Norwegian.
3. The Brit enjoys chess.
4. The person who enjoys golf lives immediately to the right of the person who enjoys hiking.
5. The pilot is the Swede.
6. The milk drinker lives somewhere to the right of the tea drinker.
7. The person who drinks cocoa enjoys tennis.
8. The owner of the horse enjoys cooking.
9. The occupant of the white house either works as the doctor or works as the lawyer.
10. The person in the red house lives in the house just left of the one where the occupant of the blue house lives.
11. The person in the white house lives at one end of the row.
12. The painting enthusiast does not keep the fish.
13. The cat owner lives in the house just left of the one where the bird owner lives.
14. The cooking enthusiast and the water drinker live in adjacent houses.
15. The owner of the cat drinks coffee.
16. The owner of the cat lives in the purple house.
17. The Spaniard keeps the bird.
18. The teacher lives in the blue house.
19. The person who drinks water and the occupant of the yellow house live two houses apart.
20. The baker enjoys golf.
21. The dog owner either works as the farmer or works as the pilot.
22. The person who keeps the cat lives in the second house.
23. There is exactly one house between the German and the Swede.
24. The person who enjoys hiking works as the pilot.
25. The person who keeps the cat and the lawyer live two houses apart.
26. The teacher enjoys tennis.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
