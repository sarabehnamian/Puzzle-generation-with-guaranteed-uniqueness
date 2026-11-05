# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. There is exactly one house between the person in the blue house and the doctor.
2. Whoever lives in the yellow house lives directly to the left of the owner of the horse.
3. The person who keeps the horse lives immediately to the right of the owner of the rabbit.
4. The golf enthusiast and the person who drinks tea are neighbours.
5. The doctor drinks cocoa.
6. The person in the purple house and the person who drinks coffee are different people.
7. The Norwegian and the person in the yellow house live in adjacent houses.
8. The person who keeps the rabbit either is the Dane or is the German.
9. The person who drinks cocoa either works as the doctor or works as the pilot.
10. The baker either keeps the horse or keeps the rabbit.
11. The person who enjoys golf works as the lawyer.
12. The person who enjoys painting drinks coffee.
13. The person who enjoys cooking keeps the fish.
14. The person in the blue house does not drink milk.
15. The dog owner either works as the lawyer or works as the teacher.
16. The milk drinker lives somewhere to the left of the owner of the fish.
17. The Swede lives immediately to the right of the person who drinks water.
18. The farmer and the occupant of the red house live two houses apart.
19. The bird owner works as the farmer.
20. There is exactly one house between the chess enthusiast and the lawyer.
21. The person who drinks tea lives in the house just left of the one where the person in the green house lives.
22. The German lives at one end of the row.
23. The Brit lives in the white house.
24. The tennis enthusiast lives in the white house.
25. Whoever lives in the green house and the tennis enthusiast live in adjacent houses.
26. The Norwegian lives directly to the left of the German.
27. The cat owner and the person in the purple house are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
