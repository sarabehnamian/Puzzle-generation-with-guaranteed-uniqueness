# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-12

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The owner of the bird and the fish owner are not neighbours.
2. The German keeps the dog.
3. The doctor lives next to the tennis enthusiast.
4. The occupant of the red house works as the doctor.
5. The person who drinks coffee lives next to the Norwegian.
6. The Swede enjoys golf.
7. The baker lives in the green house.
8. The person in the white house is the Brit.
9. The person who keeps the rabbit lives in the house just left of the one where the person who enjoys tennis lives.
10. The person in the white house drinks juice.
11. The milk drinker and the Dane are different people.
12. The teacher lives in the white house.
13. The Brit lives in the house just left of the one where whoever lives in the blue house lives.
14. The teacher lives in a lower-numbered house than the person who enjoys painting.
15. The Spaniard enjoys tennis.
16. There is exactly one house between the cocoa drinker and the Spaniard.
17. The person who enjoys cooking lives immediately to the right of the tennis enthusiast.
18. The person who enjoys golf either works as the farmer or works as the pilot.
19. The person who enjoys golf lives in house 3.
20. The water drinker lives in the house just left of the one where whoever lives in the white house lives.
21. The farmer lives immediately to the right of the Dane.
22. The person who enjoys chess does not live in house 1.
23. The bird owner lives in a lower-numbered house than the golf enthusiast.
24. The person in the purple house keeps the horse.
25. There is exactly one house between the cooking enthusiast and whoever lives in the yellow house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Clues:
1. The teacher lives in the green house.
2. The Spaniard and the German are neighbours.
3. The cat owner lives in a lower-numbered house than the occupant of the yellow house.
4. The person who keeps the fish either is the Spaniard or is the Swede.
5. The person who keeps the dog lives in the yellow house.
6. Whoever lives in the red house lives in one of the two end houses.
7. The juice drinker lives in the white house.
8. The owner of the bird drinks milk.
9. The occupant of the yellow house does not enjoy golf.
10. The Brit and the occupant of the purple house live two houses apart.
11. The person who drinks cocoa either enjoys chess or enjoys painting.
12. The water drinker lives at one end of the row.
13. The pilot is the Dane.
14. The lawyer is the Swede.
15. The tennis enthusiast lives directly to the left of the doctor.
16. The horse owner lives at one end of the row.
17. Whoever lives in the blue house is the Spaniard.
18. The hiking enthusiast lives somewhere to the right of the German.
19. The owner of the horse enjoys chess.
20. The Dane and the Norwegian live two houses apart.
21. The baker and the tea drinker live two houses apart.
22. The person who enjoys chess lives in the green house.
23. The person who drinks juice lives in the fourth house.
24. The milk drinker lives somewhere to the left of the hiking enthusiast.
25. The person in the white house lives directly to the left of the golf enthusiast.
26. The person who keeps the cat does not live next to the person who drinks coffee.
27. The person who enjoys cooking either works as the baker or works as the lawyer.
28. The pilot lives in the fourth house.
29. The farmer either lives in the purple house or lives in the red house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The milk drinker lives immediately to the right of the baker.
2. The Dane lives in the third house.
3. The person who enjoys cooking is the German.
4. The occupant of the white house is the Brit.
5. The owner of the dog drinks water.
6. The owner of the fish and the person who keeps the horse are neighbours.
7. The cocoa drinker lives in the fifth house.
8. The chess enthusiast lives next to the doctor.
9. Whoever lives in the blue house lives immediately to the right of the teacher.
10. The lawyer either drinks milk or drinks water.
11. The person who drinks juice either keeps the horse or keeps the rabbit.
12. The Brit lives immediately to the right of the person in the blue house.
13. The owner of the fish lives immediately to the right of the Norwegian.
14. The pilot lives in the yellow house.
15. The person in the red house lives in a lower-numbered house than the owner of the rabbit.
16. The baker drinks tea.
17. The Brit and the person in the purple house live in adjacent houses.
18. There is exactly one house between the lawyer and the milk drinker.
19. The Spaniard enjoys golf.
20. The tennis enthusiast drinks milk.
21. The golf enthusiast drinks coffee.
22. The person in the red house lives in a lower-numbered house than the Spaniard.
23. The person who drinks water enjoys painting.
24. The owner of the cat enjoys cooking.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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
1. The Dane and the owner of the dog live in adjacent houses.
2. There is exactly one house between the person who drinks cocoa and the person who drinks milk.
3. The lawyer lives immediately to the right of the farmer.
4. The dog owner lives in the house just left of the one where the doctor lives.
5. The person who enjoys golf lives in one of the two end houses.
6. The horse owner drinks cocoa.
7. The teacher lives immediately to the right of the owner of the cat.
8. The Brit and the Swede are not neighbours.
9. The person in the green house and the Norwegian live in adjacent houses.
10. The owner of the fish and the owner of the horse live two houses apart.
11. The water drinker keeps the dog.
12. The horse owner and the milk drinker live two houses apart.
13. The cat owner and the tea drinker are neighbours.
14. There is exactly one house between the hiking enthusiast and the Norwegian.
15. The doctor lives directly to the left of the hiking enthusiast.
16. The German lives somewhere to the left of the person who keeps the fish.
17. The baker keeps the dog.
18. The doctor keeps the fish.
19. The occupant of the blue house lives in the sixth house.
20. The juice drinker lives immediately to the right of whoever lives in the white house.
21. The cooking enthusiast and the person in the white house live two houses apart.
22. The Swede keeps the rabbit.
23. The occupant of the purple house lives in the house just left of the one where the German lives.
24. The Spaniard and the teacher are neighbours.
25. The tea drinker keeps the rabbit.
26. Whoever lives in the green house works as the lawyer.
27. Whoever lives in the red house keeps the cat.
28. The owner of the dog and the golf enthusiast live two houses apart.
29. The occupant of the green house does not live next to the tennis enthusiast.
30. The golf enthusiast lives in the house just left of the one where the person who enjoys chess lives.
31. The Norwegian and the Swede are not neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
