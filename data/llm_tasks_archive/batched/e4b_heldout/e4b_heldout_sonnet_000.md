# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_sonnet_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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

## Puzzle e4b-g0-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Clues:
1. The occupant of the white house enjoys painting.
2. The rabbit owner lives directly to the left of the lawyer.
3. The dog owner either works as the doctor or works as the pilot.
4. The coffee drinker either enjoys cooking or enjoys tennis.
5. The person in the blue house either drinks juice or drinks tea.
6. The person in the blue house and the milk drinker live two houses apart.
7. The teacher lives in the third house.
8. The person who keeps the horse lives directly to the left of the person who keeps the bird.
9. The person who keeps the fish lives directly to the left of the person in the yellow house.
10. The doctor and the milk drinker are not neighbours.
11. The Norwegian does not live in the green house.
12. The person who enjoys tennis lives in house 5.
13. The doctor lives next to the person who keeps the horse.
14. The Spaniard lives in the third house.
15. The baker and the cocoa drinker are neighbours.
16. Whoever lives in the yellow house lives in the house just left of the one where the hiking enthusiast lives.
17. The person who drinks tea lives immediately to the right of the Brit.
18. The cocoa drinker lives somewhere to the left of the person who keeps the horse.
19. The German lives in the house just left of the one where the Swede lives.
20. The person who drinks coffee lives in the green house.
21. The golf enthusiast works as the baker.
22. Whoever lives in the purple house lives in the fifth house.
23. The person who keeps the dog enjoys hiking.
24. The milk drinker lives immediately to the right of the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The person in the white house lives in the third house.
2. The person who keeps the bird lives directly to the left of the person who keeps the horse.
3. The Spaniard lives in the last house.
4. The cat owner lives directly to the left of the juice drinker.
5. The person who drinks cocoa lives at one end of the row.
6. The golf enthusiast lives in the fourth house.
7. The person who keeps the horse lives in the yellow house.
8. The baker lives in the house just left of the one where the occupant of the green house lives.
9. The chess enthusiast lives in one of the two end houses.
10. Whoever lives in the blue house lives in the sixth house.
11. The German keeps the fish.
12. There is exactly one house between the owner of the dog and the person who drinks milk.
13. There is exactly one house between the person in the blue house and the Norwegian.
14. Whoever lives in the purple house is the Dane.
15. The person who drinks tea works as the doctor.
16. The horse owner and the lawyer are neighbours.
17. The pilot lives somewhere to the right of the person who drinks tea.
18. The German works as the teacher.
19. The painting enthusiast keeps the rabbit.
20. The farmer keeps the bird.
21. The Swede lives in the fifth house.
22. The owner of the bird lives immediately to the right of the person who drinks coffee.
23. The golf enthusiast and the tennis enthusiast live two houses apart.
24. The hiking enthusiast lives next to the person in the white house.

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
