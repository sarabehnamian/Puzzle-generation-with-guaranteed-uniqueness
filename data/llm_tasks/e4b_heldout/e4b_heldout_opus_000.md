# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_heldout/e4b_heldout_opus_000.out.json with this exact structure
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

## Puzzle e4b-g0-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, baker, pilot, doctor, teacher
- hobby: tennis, hiking, golf, chess, painting, cooking
- pet: rabbit, bird, fish, cat, dog, horse
- color: green, blue, white, yellow, red, purple
- drink: cocoa, juice, milk, tea, coffee, water
- nationality: Brit, Norwegian, German, Swede, Spaniard, Dane

Clues:
1. The Norwegian drinks juice.
2. The person who enjoys hiking is the Norwegian.
3. The person who drinks cocoa enjoys golf.
4. The water drinker lives in the first house.
5. The person who keeps the fish works as the lawyer.
6. The person who keeps the bird and the person in the red house live in adjacent houses.
7. The person in the blue house lives in house 1.
8. The teacher lives immediately to the right of the person who enjoys tennis.
9. The person in the yellow house lives in a lower-numbered house than the Swede.
10. The owner of the horse lives directly to the left of the baker.
11. The person in the purple house either drinks juice or drinks tea.
12. The painting enthusiast works as the pilot.
13. The Norwegian and the owner of the rabbit live in adjacent houses.
14. The coffee drinker enjoys painting.
15. The Dane lives next to the person who keeps the rabbit.
16. The person who keeps the rabbit is the Brit.
17. The bird owner lives in the sixth house.
18. The cat owner and the German are neighbours.
19. Whoever lives in the green house lives immediately to the right of the person who enjoys cooking.
20. The occupant of the green house enjoys golf.
21. The person who keeps the rabbit lives directly to the left of whoever lives in the green house.
22. The farmer lives directly to the left of the baker.
23. The person who drinks milk lives immediately to the right of the dog owner.

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
