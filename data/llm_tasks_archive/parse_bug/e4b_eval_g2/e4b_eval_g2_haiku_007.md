# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_007.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-11

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. There is exactly one house between the farmer and the occupant of the red house.
2. The person who keeps the bird does not live next to the Brit.
3. The person who keeps the dog either works as the lawyer or works as the teacher.
4. The person who enjoys tennis lives in the white house.
5. The cocoa drinker either works as the doctor or works as the pilot.
6. The Norwegian and whoever lives in the yellow house live in adjacent houses.
7. The baker either keeps the horse or keeps the rabbit.
8. The cat owner and the cocoa drinker live two houses apart.
9. The person who enjoys golf and the person who drinks tea are neighbours.
10. The cat owner lives next to the occupant of the purple house.
11. The water drinker lives somewhere to the left of the Swede.
12. There is exactly one house between the occupant of the blue house and the doctor.
13. The person who enjoys cooking keeps the fish.
14. The tea drinker lives in the house just left of the one where whoever lives in the green house lives.
15. Whoever lives in the purple house and the coffee drinker are different people.
16. The owner of the rabbit either is the Dane or is the German.
17. The owner of the horse lives immediately to the right of the person who keeps the rabbit.
18. The Norwegian lives in the house just left of the one where the German lives.
19. The golf enthusiast works as the lawyer.
20. The German lives in the sixth house.
21. The Brit does not live in the red house.
22. Whoever lives in the green house and the person who enjoys tennis are neighbours.
23. The painting enthusiast drinks coffee.
24. The bird owner works as the farmer.
25. The person who enjoys chess and the lawyer live two houses apart.
26. Whoever lives in the yellow house lives directly to the left of the horse owner.
27. There is exactly one house between the owner of the horse and whoever lives in the purple house.
28. Whoever lives in the blue house drinks juice.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
