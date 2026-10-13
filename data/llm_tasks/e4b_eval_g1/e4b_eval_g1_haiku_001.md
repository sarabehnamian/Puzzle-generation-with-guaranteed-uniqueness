# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g1/e4b_eval_g1_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The dog owner lives in a lower-numbered house than the tea drinker.
2. The teacher enjoys tennis.
3. The cat owner lives immediately to the right of the juice drinker.
4. The Swede and the person in the white house live two houses apart.
5. The horse owner works as the pilot.
6. Whoever lives in the purple house lives next to the Spaniard.
7. The tea drinker and the tennis enthusiast live two houses apart.
8. The owner of the cat enjoys cooking.
9. The person who drinks cocoa and the owner of the dog live in adjacent houses.
10. The occupant of the blue house lives in house 3.
11. The owner of the bird is the Dane.
12. The Brit drinks tea.
13. The person who drinks cocoa and the Norwegian live in adjacent houses.
14. The hiking enthusiast lives in the green house.
15. Whoever lives in the green house lives next to the occupant of the red house.
16. The person who enjoys chess lives in the yellow house.
17. The farmer lives in the house just left of the one where the person who keeps the rabbit lives.
18. The doctor lives next to the person in the red house.
19. The baker lives next to the person who drinks cocoa.
20. The person who drinks coffee enjoys golf.
21. There is exactly one house between the person who keeps the cat and the lawyer.
22. The person who keeps the rabbit lives in the house just left of the one where the painting enthusiast lives.
23. The juice drinker lives in house 2.
24. The person who drinks milk lives in a lower-numbered house than the person who drinks juice.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. The occupant of the green house either works as the doctor or works as the farmer.
2. The Brit lives in house 5.
3. The tea drinker works as the teacher.
4. The hiking enthusiast lives next to the rabbit owner.
5. The German keeps the bird.
6. The person who keeps the horse and the painting enthusiast live in adjacent houses.
7. There is exactly one house between the person in the purple house and the person in the white house.
8. Whoever lives in the yellow house lives somewhere to the left of the German.
9. Whoever lives in the yellow house lives directly to the left of the rabbit owner.
10. The coffee drinker and the occupant of the white house live in adjacent houses.
11. The person who enjoys chess either keeps the cat or keeps the rabbit.
12. The occupant of the red house drinks tea.
13. The tea drinker keeps the fish.
14. The person who enjoys tennis lives immediately to the right of the Norwegian.
15. The person who enjoys cooking either lives in the green house or lives in the purple house.
16. The cocoa drinker and the person who keeps the rabbit are neighbours.
17. The Dane lives in one of the two end houses.
18. The rabbit owner enjoys golf.
19. The person who enjoys chess lives in a lower-numbered house than the person who drinks tea.
20. The person who drinks milk lives in the house just left of the one where the Norwegian lives.
21. The baker lives immediately to the right of the person who keeps the bird.
22. The juice drinker keeps the rabbit.
23. Whoever lives in the blue house is the Norwegian.
24. The doctor lives in the third house.
25. The pilot is the Spaniard.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-10

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. The cooking enthusiast is the Norwegian.
2. Whoever lives in the green house lives in one of the two end houses.
3. The owner of the cat is the Brit.
4. The pilot lives somewhere to the left of the lawyer.
5. Whoever lives in the purple house and the occupant of the red house are neighbours.
6. The Brit and the owner of the dog live two houses apart.
7. Whoever lives in the red house is the Norwegian.
8. The lawyer and the teacher live in adjacent houses.
9. The Brit drinks water.
10. There is exactly one house between the person who keeps the rabbit and the tea drinker.
11. The cooking enthusiast lives in one of the two end houses.
12. The chess enthusiast drinks juice.
13. The doctor lives in the red house.
14. The fish owner lives in the house just left of the one where the Dane lives.
15. The German lives next to the person who enjoys tennis.
16. The German lives somewhere to the left of the rabbit owner.
17. The German is not the farmer.
18. The golf enthusiast lives immediately to the right of the Brit.
19. The person who drinks milk and the person who drinks tea live in adjacent houses.
20. There is exactly one house between the baker and the German.
21. Whoever lives in the white house lives in the house just left of the one where the lawyer lives.
22. The German and the teacher live two houses apart.
23. The Norwegian lives in the house just left of the one where the person who drinks juice lives.
24. The cocoa drinker lives in the red house.
25. The owner of the dog lives in the house just left of the one where the Spaniard lives.
26. The owner of the bird enjoys painting.
27. The German lives in the house just left of the one where whoever lives in the blue house lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The person who enjoys golf drinks coffee.
2. The Swede and the occupant of the white house live two houses apart.
3. The baker and the cocoa drinker live in adjacent houses.
4. The person who keeps the dog lives somewhere to the left of the tea drinker.
5. The person who enjoys hiking lives in the green house.
6. The doctor and the occupant of the red house live in adjacent houses.
7. The Brit drinks tea.
8. The painting enthusiast lives immediately to the right of the person who keeps the rabbit.
9. The person who drinks water lives in the fifth house.
10. The farmer lives directly to the left of the owner of the rabbit.
11. There is exactly one house between the person who keeps the cat and the lawyer.
12. The person who drinks juice lives directly to the left of the owner of the cat.
13. The person who enjoys chess lives in the yellow house.
14. The occupant of the blue house lives in the third house.
15. The juice drinker lives in house 2.
16. The owner of the bird is the Dane.
17. The person in the purple house lives next to the Spaniard.
18. The pilot keeps the horse.
19. The teacher enjoys tennis.
20. The person who drinks coffee lives in the last house.
21. Whoever lives in the green house and whoever lives in the red house are neighbours.
22. The cocoa drinker and the Norwegian live in adjacent houses.
23. The tea drinker and the tennis enthusiast live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
