# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The person who enjoys hiking and the occupant of the white house live in adjacent houses.
2. The person who enjoys painting keeps the rabbit.
3. The doctor drinks tea.
4. The person who keeps the cat lives directly to the left of the juice drinker.
5. The occupant of the yellow house keeps the horse.
6. Whoever lives in the white house and the person in the green house live in adjacent houses.
7. There is exactly one house between the person who enjoys golf and the tennis enthusiast.
8. The German keeps the fish.
9. The person who drinks coffee lives directly to the left of the owner of the bird.
10. The occupant of the blue house lives in the last house.
11. There is exactly one house between the person who keeps the dog and the milk drinker.
12. The German lives in house 2.
13. The person who keeps the horse lives immediately to the right of the owner of the bird.
14. The pilot lives somewhere to the right of the tea drinker.
15. The Dane lives in the purple house.
16. There is exactly one house between the person in the blue house and the Norwegian.
17. The teacher is the German.
18. The bird owner works as the farmer.
19. The Spaniard lives immediately to the right of the Swede.
20. Whoever lives in the green house lives immediately to the right of the baker.
21. The person who enjoys chess lives at one end of the row.
22. The person who keeps the horse and the lawyer are neighbours.
23. The golf enthusiast lives in the fourth house.
24. The Spaniard lives at one end of the row.
25. The person who drinks cocoa lives at one end of the row.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Clues:
1. The Swede lives directly to the left of the milk drinker.
2. The person in the white house enjoys painting.
3. The person who drinks coffee either enjoys cooking or enjoys tennis.
4. The teacher lives in the third house.
5. The Norwegian does not live in the green house.
6. The person in the blue house and the milk drinker live two houses apart.
7. The person who keeps the fish lives directly to the left of whoever lives in the yellow house.
8. The baker and the cocoa drinker are neighbours.
9. The doctor and the owner of the horse are neighbours.
10. The cooking enthusiast lives in house 6.
11. The person who drinks cocoa lives in a lower-numbered house than the horse owner.
12. The coffee drinker lives in the green house.
13. Whoever lives in the purple house and whoever lives in the green house live in adjacent houses.
14. The person who enjoys tennis lives in house 5.
15. The occupant of the yellow house lives in the house just left of the one where the hiking enthusiast lives.
16. The owner of the dog either works as the doctor or works as the pilot.
17. The German lives directly to the left of the Swede.
18. The person who drinks coffee and the person who enjoys tennis are neighbours.
19. The Brit lives in the house just left of the one where the person who drinks tea lives.
20. The golf enthusiast works as the baker.
21. The doctor and the milk drinker are not neighbours.
22. The person who keeps the dog enjoys hiking.
23. The person who keeps the bird lives immediately to the right of the person who keeps the horse.
24. The Spaniard works as the teacher.
25. The lawyer lives immediately to the right of the rabbit owner.
26. Whoever lives in the blue house either drinks juice or drinks tea.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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
1. The rabbit owner lives directly to the left of the owner of the horse.
2. The owner of the dog either works as the lawyer or works as the teacher.
3. The farmer keeps the bird.
4. Whoever lives in the blue house and the doctor live two houses apart.
5. The tennis enthusiast and the person in the red house are different people.
6. The baker either keeps the horse or keeps the rabbit.
7. The golf enthusiast and the person who drinks tea live in adjacent houses.
8. The person who drinks juice lives in the blue house.
9. The person in the yellow house lives directly to the left of the horse owner.
10. The person who drinks cocoa and the pilot live two houses apart.
11. There is exactly one house between the farmer and the occupant of the red house.
12. The lawyer enjoys golf.
13. The owner of the bird and the Spaniard live in adjacent houses.
14. The person who drinks tea lives in the house just left of the one where the occupant of the green house lives.
15. The hiking enthusiast drinks milk.
16. The person who drinks cocoa either works as the doctor or works as the pilot.
17. The Norwegian and the person in the yellow house are neighbours.
18. The person who drinks coffee does not live in the purple house.
19. The German lives immediately to the right of the Norwegian.
20. The person who keeps the rabbit either is the Dane or is the German.
21. The person who drinks water lives directly to the left of the Swede.
22. The fish owner enjoys cooking.
23. The Brit lives in the white house.
24. Whoever lives in the green house and the tennis enthusiast are neighbours.
25. The German lives at one end of the row.
26. There is exactly one house between the chess enthusiast and the lawyer.
27. The owner of the cat and the person in the purple house live in adjacent houses.
28. The painting enthusiast drinks coffee.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. There is exactly one house between the chess enthusiast and the lawyer.
2. The baker either keeps the horse or keeps the rabbit.
3. The German lives in house 6.
4. The person who drinks juice lives in the blue house.
5. The farmer and the person in the red house live two houses apart.
6. The tea drinker lives directly to the left of the person in the green house.
7. The horse owner lives immediately to the right of whoever lives in the yellow house.
8. The lawyer enjoys golf.
9. The Norwegian and the occupant of the yellow house are neighbours.
10. The occupant of the white house is the Brit.
11. The water drinker lives in the house just left of the one where the Swede lives.
12. The owner of the rabbit either is the Dane or is the German.
13. The person who enjoys painting drinks coffee.
14. The person in the purple house does not drink coffee.
15. The farmer keeps the bird.
16. The person in the blue house and the doctor live two houses apart.
17. The rabbit owner lives directly to the left of the owner of the horse.
18. The golf enthusiast and the person who drinks tea are neighbours.
19. The cat owner lives next to the person in the purple house.
20. The person who drinks cocoa either works as the doctor or works as the pilot.
21. The fish owner enjoys cooking.
22. The person in the green house lives next to the tennis enthusiast.
23. The Norwegian lives in the house just left of the one where the German lives.
24. The owner of the dog either works as the lawyer or works as the teacher.
25. The person in the white house enjoys tennis.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
