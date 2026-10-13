# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g2/e4b_eval_g2_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The occupant of the green house lives next to the person in the yellow house.
2. The Brit and the person in the red house live two houses apart.
3. The teacher keeps the dog.
4. The person who drinks water does not live in house 2.
5. The person in the green house works as the lawyer.
6. The occupant of the red house keeps the horse.
7. The person in the red house lives immediately to the right of the tennis enthusiast.
8. The tea drinker enjoys golf.
9. The coffee drinker lives next to the Dane.
10. The person who drinks milk and the person in the yellow house live two houses apart.
11. The coffee drinker and the juice drinker are neighbours.
12. The person in the white house is the Swede.
13. The person in the red house lives immediately to the right of the person who keeps the cat.
14. The milk drinker is the Spaniard.
15. The person in the red house drinks juice.
16. The Swede works as the doctor.
17. The baker and the dog owner live in adjacent houses.
18. The owner of the rabbit lives in house 4.
19. The bird owner and the German are neighbours.
20. The farmer lives somewhere to the left of the person in the purple house.
21. The person in the green house lives immediately to the right of the occupant of the blue house.
22. The owner of the fish lives directly to the left of the person who enjoys painting.
23. The hiking enthusiast lives in the sixth house.
24. The Spaniard and the person who keeps the fish are different people.
25. The person who enjoys cooking lives in house 2.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The person who drinks tea is the Brit.
2. There is exactly one house between the water drinker and the person who drinks cocoa.
3. The juice drinker lives directly to the left of the cat owner.
4. The tea drinker lives somewhere to the right of the dog owner.
5. The milk drinker does not live in the fifth house.
6. Whoever lives in the green house enjoys hiking.
7. The bird owner is the Dane.
8. The person who drinks coffee lives in one of the two end houses.
9. The person who enjoys golf drinks coffee.
10. The cocoa drinker lives next to the Norwegian.
11. The painting enthusiast lives immediately to the right of the person who keeps the rabbit.
12. The farmer lives directly to the left of the person who keeps the rabbit.
13. The cat owner and the lawyer live two houses apart.
14. The Norwegian lives in house 2.
15. Whoever lives in the blue house lives in house 3.
16. The pilot keeps the horse.
17. Whoever lives in the green house and the person in the red house are neighbours.
18. The person who keeps the fish lives immediately to the right of the person who drinks tea.
19. The juice drinker lives in the second house.
20. The person who enjoys tennis works as the teacher.
21. The person who drinks tea and the person who enjoys tennis live two houses apart.
22. There is exactly one house between the Swede and the occupant of the white house.
23. There is exactly one house between the occupant of the blue house and the doctor.
24. Whoever lives in the purple house and the Spaniard live in adjacent houses.
25. The chess enthusiast lives in the yellow house.
26. The doctor lives next to whoever lives in the red house.
27. The baker and the cocoa drinker live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. There is exactly one house between whoever lives in the purple house and the person in the white house.
2. The person who enjoys chess lives in house 4.
3. The person who enjoys chess either keeps the cat or keeps the rabbit.
4. The person who enjoys tennis lives immediately to the right of the Norwegian.
5. The person who keeps the bird lives directly to the left of the baker.
6. Whoever lives in the red house drinks tea.
7. The Norwegian lives in the blue house.
8. Whoever lives in the yellow house lives directly to the left of the rabbit owner.
9. The doctor lives in house 3.
10. The tea drinker works as the teacher.
11. The cooking enthusiast either lives in the green house or lives in the purple house.
12. The Spaniard works as the pilot.
13. The Dane lives in one of the two end houses.
14. The Spaniard lives in house 1.
15. The rabbit owner enjoys golf.
16. The German keeps the bird.
17. The person who keeps the fish drinks tea.
18. The coffee drinker and the occupant of the white house live in adjacent houses.
19. The person who drinks juice keeps the rabbit.
20. The person in the green house either works as the doctor or works as the farmer.
21. The Norwegian lives immediately to the right of the person who drinks milk.
22. There is exactly one house between the Brit and the German.
23. The occupant of the yellow house lives somewhere to the left of the German.
24. The owner of the horse and the painting enthusiast live in adjacent houses.
25. The person who drinks cocoa lives next to the rabbit owner.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. The person who drinks tea lives in the red house.
2. The owner of the rabbit lives immediately to the right of the occupant of the yellow house.
3. The doctor lives next to the Norwegian.
4. The Norwegian lives directly to the left of the tennis enthusiast.
5. The Dane lives in house 6.
6. The German keeps the bird.
7. The bird owner lives in the house just left of the one where the baker lives.
8. The person who enjoys golf keeps the rabbit.
9. The person who enjoys chess either keeps the cat or keeps the rabbit.
10. Whoever lives in the green house either works as the doctor or works as the farmer.
11. The cocoa drinker and the rabbit owner live in adjacent houses.
12. The person who drinks tea works as the teacher.
13. The coffee drinker and the person in the white house are neighbours.
14. Whoever lives in the purple house and the person in the white house live two houses apart.
15. The doctor lives in the third house.
16. The juice drinker keeps the rabbit.
17. The person who enjoys cooking either lives in the green house or lives in the purple house.
18. The pilot is the Spaniard.
19. The Norwegian lives immediately to the right of the milk drinker.
20. The person who enjoys chess lives somewhere to the right of the German.
21. The owner of the horse and the painting enthusiast are neighbours.
22. The Brit lives in the fifth house.
23. The tea drinker keeps the fish.
24. The person in the yellow house lives in a lower-numbered house than the German.
25. Whoever lives in the blue house is the Norwegian.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
