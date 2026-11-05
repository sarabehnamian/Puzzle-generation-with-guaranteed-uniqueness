# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, juice, coffee
- color: white, green, purple, yellow, red, blue
- pet: dog, cat, bird, rabbit, horse, fish
- hobby: chess, hiking, tennis, cooking, painting, golf
- job: farmer, lawyer, pilot, baker, doctor, teacher
- nationality: German, Norwegian, Brit, Swede, Spaniard, Dane

Clues:
1. The person who enjoys tennis drinks cocoa.
2. The doctor either is the Brit or is the Norwegian.
3. The person who enjoys hiking lives in the house just left of the one where the person who enjoys golf lives.
4. There is exactly one house between the German and the Swede.
5. The person who enjoys hiking works as the pilot.
6. The person who keeps the cat lives in the second house.
7. There is exactly one house between the person who drinks water and whoever lives in the yellow house.
8. The teacher enjoys tennis.
9. The person who enjoys chess lives next to the juice drinker.
10. The owner of the dog either works as the farmer or works as the pilot.
11. Whoever lives in the red house lives in the house just left of the one where the occupant of the blue house lives.
12. The person in the white house either works as the doctor or works as the lawyer.
13. The Swede drinks coffee.
14. There is exactly one house between the person who keeps the cat and the lawyer.
15. The teacher lives in the blue house.
16. The person who enjoys golf works as the baker.
17. The pilot is the Swede.
18. The Spaniard does not live in house 6.
19. The person who enjoys cooking keeps the horse.
20. The person who enjoys cooking lives next to the water drinker.
21. The owner of the cat lives in the purple house.
22. The chess enthusiast is the Brit.
23. The person who enjoys painting does not keep the fish.
24. Whoever lives in the white house lives at one end of the row.
25. The bird owner lives immediately to the right of the cat owner.
26. The tea drinker lives in a lower-numbered house than the person who drinks milk.

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
