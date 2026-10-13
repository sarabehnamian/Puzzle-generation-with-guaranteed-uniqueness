# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g2/e4b_eval_g2_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The doctor lives next to the person in the red house.
2. The cocoa drinker and the Norwegian live in adjacent houses.
3. The Dane lives in the green house.
4. The Dane lives somewhere to the left of the person who enjoys chess.
5. The tennis enthusiast works as the teacher.
6. The rabbit owner lives in the house just left of the one where the painting enthusiast lives.
7. The occupant of the green house enjoys hiking.
8. There is exactly one house between the person who drinks tea and the tennis enthusiast.
9. The occupant of the green house and the person in the red house live in adjacent houses.
10. Whoever lives in the purple house and the Spaniard are neighbours.
11. The dog owner lives in a lower-numbered house than the tea drinker.
12. The occupant of the blue house and whoever lives in the red house are neighbours.
13. The Dane keeps the bird.
14. The rabbit owner lives immediately to the right of the farmer.
15. The water drinker lives in the fifth house.
16. The pilot keeps the horse.
17. The owner of the cat lives immediately to the right of the person who drinks juice.
18. The baker and the cocoa drinker are neighbours.
19. Whoever lives in the yellow house enjoys chess.
20. There is exactly one house between the cat owner and the lawyer.
21. The person who drinks coffee lives in the sixth house.
22. There is exactly one house between the Swede and the occupant of the white house.
23. The person who drinks coffee enjoys golf.
24. The person who drinks juice either is the Norwegian or is the Spaniard.
25. The tea drinker is the Brit.

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

## Puzzle e4b-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. The bird owner lives in the house just left of the one where the baker lives.
2. The person who drinks milk lives directly to the left of the Norwegian.
3. The person who enjoys chess either keeps the cat or keeps the rabbit.
4. The person in the blue house is the Norwegian.
5. The Brit lives in the fifth house.
6. The person who keeps the rabbit enjoys golf.
7. The Spaniard works as the pilot.
8. The tennis enthusiast lives immediately to the right of the Norwegian.
9. The person who keeps the horse and the painting enthusiast are neighbours.
10. The cocoa drinker and the person who keeps the rabbit live in adjacent houses.
11. The person who drinks coffee lives next to the occupant of the white house.
12. There is exactly one house between the person in the purple house and whoever lives in the white house.
13. The owner of the rabbit drinks juice.
14. The Dane lives in the sixth house.
15. The cooking enthusiast either lives in the green house or lives in the purple house.
16. The teacher drinks tea.
17. The doctor lives in house 3.
18. The person who enjoys chess lives in house 4.
19. The person who drinks tea keeps the fish.
20. The bird owner is the German.
21. The owner of the rabbit lives immediately to the right of the occupant of the yellow house.
22. The German lives somewhere to the right of the person in the yellow house.
23. Whoever lives in the green house either works as the doctor or works as the farmer.
24. The person who drinks tea lives in the red house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The juice drinker lives in the red house.
2. The Swede works as the doctor.
3. The rabbit owner lives somewhere to the right of the owner of the fish.
4. The person in the green house and the occupant of the yellow house live in adjacent houses.
5. The baker and the dog owner live in adjacent houses.
6. Whoever lives in the red house keeps the horse.
7. The Swede lives in the white house.
8. The person who enjoys cooking lives directly to the left of the Norwegian.
9. The dog owner works as the teacher.
10. The baker lives in the fourth house.
11. The person who enjoys hiking lives in the sixth house.
12. The person who keeps the fish lives in the house just left of the one where the person who enjoys painting lives.
13. The occupant of the blue house does not live next to the occupant of the red house.
14. There is exactly one house between the person who drinks milk and the occupant of the yellow house.
15. The farmer lives in a lower-numbered house than whoever lives in the purple house.
16. The occupant of the green house works as the lawyer.
17. The fish owner and the Spaniard are different people.
18. The person who drinks water does not live in house 2.
19. The owner of the bird and the German live in adjacent houses.
20. The person who drinks coffee and the person who drinks juice are neighbours.
21. The person who enjoys tennis lives in the house just left of the one where the person who enjoys hiking lives.
22. The person in the red house lives immediately to the right of the tennis enthusiast.
23. The tea drinker enjoys golf.
24. The person who drinks milk lives directly to the left of the cocoa drinker.
25. There is exactly one house between the Brit and whoever lives in the red house.
26. The coffee drinker and the Dane live in adjacent houses.
27. Whoever lives in the blue house lives in the house just left of the one where whoever lives in the green house lives.
28. The Spaniard drinks milk.
29. The person who keeps the cat lives in the house just left of the one where the person in the red house lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
