# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-10

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. The person who keeps the rabbit lives directly to the left of the person who keeps the horse.
2. The person who enjoys golf works as the lawyer.
3. The occupant of the purple house does not drink coffee.
4. The baker either keeps the horse or keeps the rabbit.
5. The Brit lives in the white house.
6. The person in the yellow house lives in the house just left of the one where the horse owner lives.
7. The baker lives somewhere to the right of the hiking enthusiast.
8. The person who drinks water lives in the house just left of the one where the Swede lives.
9. The person who keeps the cat and the person in the purple house live in adjacent houses.
10. There is exactly one house between the farmer and the person in the red house.
11. The Norwegian lives next to whoever lives in the yellow house.
12. The person who enjoys painting drinks coffee.
13. The chess enthusiast and the lawyer live two houses apart.
14. There is exactly one house between whoever lives in the blue house and the doctor.
15. The person who keeps the bird works as the farmer.
16. The cocoa drinker either works as the doctor or works as the pilot.
17. The person who drinks tea lives in the house just left of the one where the person in the green house lives.
18. The German lives at one end of the row.
19. The occupant of the blue house drinks juice.
20. The German lives immediately to the right of the Norwegian.
21. The owner of the dog either works as the lawyer or works as the teacher.
22. The person who keeps the rabbit either is the Dane or is the German.
23. The owner of the fish enjoys cooking.
24. The person in the white house enjoys tennis.
25. The golf enthusiast and the tea drinker are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
