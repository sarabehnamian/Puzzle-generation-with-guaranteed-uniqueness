# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The person in the blue house lives immediately to the right of the Brit.
2. The teacher lives in a lower-numbered house than the person who enjoys painting.
3. The cooking enthusiast and whoever lives in the yellow house live two houses apart.
4. The person who drinks juice lives in the white house.
5. The teacher lives in the white house.
6. The Dane lives directly to the left of the farmer.
7. The owner of the horse lives in the purple house.
8. The tennis enthusiast is the Spaniard.
9. The person who keeps the bird and the owner of the fish are not neighbours.
10. The person who enjoys golf either works as the farmer or works as the pilot.
11. The person who drinks coffee and the Norwegian live in adjacent houses.
12. The chess enthusiast lives in house 2.
13. The cocoa drinker and the Spaniard live two houses apart.
14. The tennis enthusiast lives in the house just left of the one where the cooking enthusiast lives.
15. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.
16. The bird owner lives in house 2.
17. The Dane and the person who drinks milk are different people.
18. The Swede enjoys golf.
19. The occupant of the red house works as the doctor.
20. The Brit lives in the white house.
21. The German keeps the dog.
22. The occupant of the white house lives immediately to the right of the person who drinks water.
23. The baker lives in the green house.
24. The golf enthusiast lives in house 3.
25. The doctor and the person who enjoys tennis live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. The person in the green house lives immediately to the right of the person who drinks tea.
2. Whoever lives in the blue house drinks juice.
3. The farmer and whoever lives in the red house live two houses apart.
4. The German lives at one end of the row.
5. Whoever lives in the yellow house lives directly to the left of the horse owner.
6. The person in the green house lives next to the person who enjoys tennis.
7. The person who drinks coffee does not live in the purple house.
8. The person who drinks water lives directly to the left of the Swede.
9. The person who keeps the cat and the person in the purple house are neighbours.
10. The owner of the rabbit lives in the house just left of the one where the horse owner lives.
11. The Norwegian lives next to whoever lives in the yellow house.
12. The Brit lives in the white house.
13. The fish owner enjoys cooking.
14. The owner of the dog either works as the lawyer or works as the teacher.
15. The person who enjoys golf works as the lawyer.
16. The person who keeps the rabbit either is the Dane or is the German.
17. The Norwegian lives in the house just left of the one where the German lives.
18. There is exactly one house between the chess enthusiast and the lawyer.
19. The baker either keeps the horse or keeps the rabbit.
20. The tennis enthusiast lives in the white house.
21. The occupant of the blue house and the doctor live two houses apart.
22. The golf enthusiast and the person who drinks tea live in adjacent houses.
23. The person who drinks cocoa either works as the doctor or works as the pilot.
24. The painting enthusiast drinks coffee.
25. The owner of the bird works as the farmer.

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
