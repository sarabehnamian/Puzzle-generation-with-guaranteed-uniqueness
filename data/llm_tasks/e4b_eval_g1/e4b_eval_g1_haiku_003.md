# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g1/e4b_eval_g1_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. The golf enthusiast keeps the rabbit.
2. The horse owner and the painting enthusiast are neighbours.
3. The Norwegian lives in the blue house.
4. The Brit does not live next to the Swede.
5. The Dane lives in the sixth house.
6. The rabbit owner drinks juice.
7. Whoever lives in the green house either works as the doctor or works as the farmer.
8. The occupant of the purple house and the person in the white house live two houses apart.
9. The Norwegian lives immediately to the right of the milk drinker.
10. The Norwegian lives in the house just left of the one where the tennis enthusiast lives.
11. The cooking enthusiast either lives in the green house or lives in the purple house.
12. The teacher drinks tea.
13. The chess enthusiast lives in house 4.
14. The person who drinks tea keeps the fish.
15. Whoever lives in the yellow house lives directly to the left of the rabbit owner.
16. The coffee drinker and whoever lives in the white house live in adjacent houses.
17. The person who keeps the bird lives in the house just left of the one where the baker lives.
18. The German lives somewhere to the right of the person in the yellow house.
19. The Swede lives in the house just left of the one where the German lives.
20. The doctor and the Dane are not neighbours.
21. The doctor lives in the third house.
22. The pilot is the Spaniard.
23. The cocoa drinker and the rabbit owner live in adjacent houses.
24. The German keeps the bird.
25. The tea drinker lives in the red house.
26. The chess enthusiast either keeps the cat or keeps the rabbit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The person who enjoys hiking lives in the last house.
2. The person who keeps the rabbit and the owner of the bird are not neighbours.
3. The person in the green house and the person in the yellow house are neighbours.
4. The baker and the dog owner live in adjacent houses.
5. The person who keeps the dog works as the teacher.
6. The person who enjoys tennis lives in the house just left of the one where the occupant of the red house lives.
7. The person who enjoys painting lives immediately to the right of the owner of the fish.
8. The German enjoys cooking.
9. Whoever lives in the green house lives immediately to the right of the person in the blue house.
10. The Brit and the person in the red house live two houses apart.
11. The person who keeps the bird and the German live in adjacent houses.
12. The person who keeps the fish is not the Spaniard.
13. The person who drinks coffee lives next to the person who drinks juice.
14. The juice drinker lives in the red house.
15. The person who drinks water does not live in house 2.
16. The Swede works as the doctor.
17. The person in the green house works as the lawyer.
18. The person who enjoys cooking lives in a lower-numbered house than the person who enjoys painting.
19. The Swede lives in the white house.
20. The person who drinks tea enjoys golf.
21. The person who drinks milk is the Spaniard.
22. The owner of the cat lives directly to the left of the occupant of the red house.
23. The person in the purple house lives somewhere to the right of the farmer.
24. The teacher lives in house 3.
25. The person who keeps the horse lives in the red house.
26. The person who drinks milk and the occupant of the yellow house live two houses apart.
27. The person who drinks coffee and the Dane live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, baker, pilot, doctor, teacher
- hobby: tennis, hiking, golf, chess, painting, cooking
- pet: rabbit, bird, fish, cat, dog, horse
- color: green, blue, white, yellow, red, purple
- drink: cocoa, juice, milk, tea, coffee, water
- nationality: Brit, Norwegian, German, Swede, Spaniard, Dane

Clues:
1. The owner of the bird and whoever lives in the red house are neighbours.
2. The person who enjoys golf lives somewhere to the right of the person in the blue house.
3. The lawyer keeps the fish.
4. The person who drinks coffee lives in house 6.
5. The Dane and the owner of the rabbit are neighbours.
6. The person who enjoys golf lives in the green house.
7. The farmer lives in the house just left of the one where the baker lives.
8. The rabbit owner is the Brit.
9. The pilot enjoys painting.
10. The Norwegian drinks juice.
11. The person who keeps the bird lives in the last house.
12. The person who enjoys golf drinks cocoa.
13. The owner of the rabbit lives in the house just left of the one where the occupant of the green house lives.
14. The person in the purple house either drinks juice or drinks tea.
15. The Norwegian and the owner of the rabbit are neighbours.
16. The person who keeps the dog lives directly to the left of the milk drinker.
17. The person in the yellow house lives somewhere to the left of the Swede.
18. The water drinker lives in a lower-numbered house than the occupant of the white house.
19. The person who drinks tea does not live in house 1.
20. The person who enjoys cooking lives directly to the left of whoever lives in the green house.
21. The person who enjoys tennis lives directly to the left of the teacher.
22. The owner of the cat lives next to the German.
23. The person who enjoys painting drinks coffee.
24. Whoever lives in the blue house and the rabbit owner live two houses apart.
25. Whoever lives in the blue house and the person who keeps the rabbit are not neighbours.
26. The Norwegian enjoys hiking.
27. The baker lives immediately to the right of the owner of the horse.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-12

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, Dane, Norwegian, Brit, German
- drink: tea, water, coffee, juice, milk, cocoa
- job: lawyer, farmer, doctor, baker, pilot, teacher
- color: red, purple, green, blue, yellow, white
- hobby: chess, painting, tennis, golf, hiking, cooking
- pet: bird, cat, fish, rabbit, horse, dog

Clues:
1. The person who keeps the bird and the person in the red house are neighbours.
2. The person in the green house lives at one end of the row.
3. The bird owner lives immediately to the right of the Spaniard.
4. The coffee drinker lives in the house just left of the one where the doctor lives.
5. The Swede works as the doctor.
6. The occupant of the red house works as the pilot.
7. The doctor lives somewhere to the left of the lawyer.
8. The person who drinks water lives directly to the left of the occupant of the blue house.
9. The rabbit owner enjoys tennis.
10. The bird owner lives in the white house.
11. The golf enthusiast lives directly to the left of the painting enthusiast.
12. There is exactly one house between the golf enthusiast and the teacher.
13. The Swede lives somewhere to the right of the cat owner.
14. The Swede either drinks coffee or drinks tea.
15. The cocoa drinker and the person who keeps the horse live in adjacent houses.
16. The dog owner works as the lawyer.
17. Whoever lives in the purple house does not live in house 3.
18. The Dane drinks milk.
19. The person who keeps the cat either is the Brit or is the Dane.
20. The juice drinker keeps the dog.
21. Whoever lives in the blue house lives somewhere to the left of the person who drinks juice.
22. The person who enjoys chess lives next to the person who enjoys tennis.
23. The rabbit owner lives directly to the left of the owner of the bird.
24. The cooking enthusiast lives somewhere to the left of the tea drinker.
25. The Dane lives next to whoever lives in the green house.
26. Whoever lives in the green house either is the Norwegian or is the Swede.
27. The person who enjoys cooking and whoever lives in the yellow house live two houses apart.
28. Whoever lives in the blue house and the occupant of the white house live two houses apart.
29. The farmer lives immediately to the right of the Brit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
