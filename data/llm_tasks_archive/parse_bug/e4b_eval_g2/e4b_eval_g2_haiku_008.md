# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_008.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. The German lives immediately to the right of the Norwegian.
2. The cooking enthusiast keeps the fish.
3. The person who keeps the cat and the person who drinks cocoa live two houses apart.
4. The occupant of the yellow house lives in the house just left of the one where the horse owner lives.
5. The water drinker lives somewhere to the left of the Swede.
6. The rabbit owner either is the Dane or is the German.
7. The person who drinks tea lives in the house just left of the one where the person in the green house lives.
8. There is exactly one house between the horse owner and the person in the purple house.
9. The baker either keeps the horse or keeps the rabbit.
10. The person who enjoys painting drinks coffee.
11. The lawyer enjoys golf.
12. The German lives at one end of the row.
13. The tennis enthusiast lives in the white house.
14. The dog owner either works as the lawyer or works as the teacher.
15. The occupant of the green house and the tennis enthusiast live in adjacent houses.
16. The coffee drinker and whoever lives in the purple house are different people.
17. The Norwegian lives next to whoever lives in the yellow house.
18. The person who enjoys golf lives next to the person who drinks tea.
19. The rabbit owner lives directly to the left of the owner of the horse.
20. The person who drinks juice lives in the blue house.
21. The farmer and the occupant of the red house live two houses apart.
22. There is exactly one house between the person who enjoys chess and the lawyer.
23. The owner of the bird and the Brit are not neighbours.
24. The cat owner and whoever lives in the purple house live in adjacent houses.
25. There is exactly one house between the person in the blue house and the doctor.
26. The cocoa drinker either works as the doctor or works as the pilot.
27. The person who keeps the bird works as the farmer.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
