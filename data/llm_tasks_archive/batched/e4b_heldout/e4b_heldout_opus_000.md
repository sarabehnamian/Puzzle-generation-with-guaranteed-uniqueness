# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_opus_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The coffee drinker lives next to the cocoa drinker.
2. The person who enjoys cooking is the German.
3. The tea drinker works as the baker.
4. The person who drinks water enjoys painting.
5. The Norwegian lives directly to the left of the owner of the fish.
6. The occupant of the white house is the Brit.
7. Whoever lives in the yellow house works as the pilot.
8. The Dane lives in the third house.
9. The owner of the bird and the lawyer live two houses apart.
10. The Spaniard lives somewhere to the right of the occupant of the red house.
11. The Brit and whoever lives in the purple house are neighbours.
12. The person who drinks milk lives immediately to the right of the baker.
13. The lawyer and the person who drinks milk live two houses apart.
14. The occupant of the blue house lives in the house just left of the one where the Brit lives.
15. The person who enjoys chess and the doctor are neighbours.
16. The occupant of the red house lives in a lower-numbered house than the person who keeps the rabbit.
17. The person who drinks juice either keeps the horse or keeps the rabbit.
18. The teacher lives directly to the left of the occupant of the blue house.
19. The person who enjoys tennis drinks milk.
20. The person who keeps the fish and the owner of the horse are neighbours.
21. The Spaniard enjoys golf.
22. The lawyer either drinks milk or drinks water.
23. The cocoa drinker lives in house 5.
24. The dog owner drinks water.
25. The person who keeps the cat lives in a lower-numbered house than the owner of the fish.

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

## Puzzle e4b-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The person in the green house lives next to the Norwegian.
2. The German lives somewhere to the left of the person who keeps the fish.
3. The person who keeps the dog works as the baker.
4. The person who enjoys golf lives at one end of the row.
5. There is exactly one house between the person who drinks cocoa and the milk drinker.
6. The hiking enthusiast lives immediately to the right of the doctor.
7. The person in the green house works as the lawyer.
8. Whoever lives in the green house and the person who enjoys tennis are not neighbours.
9. The Brit lives in the first house.
10. The person who drinks water keeps the dog.
11. The owner of the horse and the milk drinker live two houses apart.
12. The Swede keeps the rabbit.
13. Whoever lives in the blue house lives in the last house.
14. The cat owner and the tea drinker live in adjacent houses.
15. The person who enjoys golf lives directly to the left of the person who enjoys chess.
16. The teacher lives immediately to the right of the cat owner.
17. The owner of the fish works as the doctor.
18. The lawyer lives immediately to the right of the farmer.
19. The Dane lives next to the dog owner.
20. Whoever lives in the white house lives in the house just left of the one where the person who drinks juice lives.
21. The person in the red house keeps the cat.
22. The person in the yellow house lives in house 3.
23. The owner of the dog lives in the house just left of the one where the doctor lives.
24. There is exactly one house between the cooking enthusiast and the occupant of the white house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
