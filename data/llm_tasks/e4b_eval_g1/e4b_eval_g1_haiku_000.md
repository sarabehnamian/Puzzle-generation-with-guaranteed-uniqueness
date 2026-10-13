# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g1/e4b_eval_g1_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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

## Puzzle e4b-g1-11

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, Dane, Norwegian, Brit, German
- drink: tea, water, coffee, juice, milk, cocoa
- job: lawyer, farmer, doctor, baker, pilot, teacher
- color: red, purple, green, blue, yellow, white
- hobby: chess, painting, tennis, golf, hiking, cooking
- pet: bird, cat, fish, rabbit, horse, dog

Clues:
1. Whoever lives in the green house either is the Norwegian or is the Swede.
2. The person who drinks juice lives somewhere to the right of the person in the blue house.
3. The Spaniard lives in the house just left of the one where the bird owner lives.
4. The person in the purple house works as the baker.
5. The person who drinks juice keeps the dog.
6. The person who enjoys cooking lives somewhere to the left of the tea drinker.
7. The person in the purple house lives in one of the two end houses.
8. The bird owner lives immediately to the right of the person who keeps the rabbit.
9. The rabbit owner enjoys tennis.
10. The Brit enjoys chess.
11. The doctor is the Swede.
12. Whoever lives in the blue house does not live in the first house.
13. The person who drinks cocoa lives next to the owner of the horse.
14. There is exactly one house between the golf enthusiast and the teacher.
15. The occupant of the blue house and the person who drinks water are neighbours.
16. The coffee drinker lives in the house just left of the one where the doctor lives.
17. The Swede lives somewhere to the right of the person who keeps the cat.
18. The Swede either drinks coffee or drinks tea.
19. The golf enthusiast lives directly to the left of the person who enjoys painting.
20. The chess enthusiast and the person who enjoys tennis are neighbours.
21. The Dane and the person in the green house live in adjacent houses.
22. The lawyer lives somewhere to the right of the doctor.
23. Whoever lives in the red house works as the pilot.
24. The person who keeps the cat either is the Brit or is the Dane.
25. The painting enthusiast lives next to the person in the white house.
26. The cooking enthusiast and the occupant of the yellow house live two houses apart.
27. The farmer lives immediately to the right of the Brit.
28. Whoever lives in the green house lives at one end of the row.
29. The person who drinks milk is the Dane.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The Swede lives in the white house.
2. The person in the red house keeps the horse.
3. The person who enjoys hiking lives in one of the two end houses.
4. The teacher keeps the dog.
5. The person who drinks coffee lives next to the person who drinks juice.
6. The lawyer lives in the green house.
7. The baker and the dog owner live in adjacent houses.
8. The milk drinker and whoever lives in the yellow house live two houses apart.
9. The person who drinks coffee lives next to the Dane.
10. The tennis enthusiast lives in the house just left of the one where the person in the red house lives.
11. The hiking enthusiast lives next to whoever lives in the white house.
12. The owner of the bird and the German are neighbours.
13. The tea drinker and the teacher are neighbours.
14. The Swede works as the doctor.
15. The milk drinker is the Spaniard.
16. The tea drinker enjoys golf.
17. Whoever lives in the red house lives immediately to the right of the cat owner.
18. Whoever lives in the red house drinks juice.
19. The person who enjoys painting drinks water.
20. Whoever lives in the green house lives immediately to the right of the occupant of the blue house.
21. The person who keeps the fish lives directly to the left of the person who enjoys painting.
22. The person who keeps the cat and the cocoa drinker are not neighbours.
23. The teacher either is the Norwegian or is the Swede.
24. The Brit and whoever lives in the red house live two houses apart.
25. The owner of the cat lives somewhere to the right of the person in the yellow house.
26. The Spaniard and the owner of the fish are different people.
27. Whoever lives in the green house and the occupant of the yellow house are neighbours.
28. The rabbit owner does not live in the fifth house.
29. The water drinker does not live in the second house.
30. The farmer lives in a lower-numbered house than the person in the purple house.
31. The cooking enthusiast keeps the fish.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The Dane and the person who keeps the rabbit live two houses apart.
2. The cocoa drinker lives in a lower-numbered house than the person who drinks coffee.
3. The person who enjoys hiking lives directly to the left of the cat owner.
4. The milk drinker lives in house 3.
5. The doctor and the person in the red house live in adjacent houses.
6. The Swede lives somewhere to the right of the person who keeps the bird.
7. The Swede lives somewhere to the left of the Brit.
8. The tea drinker lives in the green house.
9. The farmer lives directly to the left of the chess enthusiast.
10. The owner of the horse lives in the yellow house.
11. The person who drinks cocoa and the teacher live two houses apart.
12. The teacher and the person who enjoys tennis live two houses apart.
13. The doctor lives in one of the two end houses.
14. Whoever lives in the green house lives somewhere to the right of the occupant of the yellow house.
15. The tennis enthusiast lives immediately to the right of the Norwegian.
16. The person in the blue house lives in house 4.
17. The cocoa drinker either lives in the blue house or lives in the yellow house.
18. The Brit lives in the fifth house.
19. The person who keeps the cat lives in one of the two end houses.
20. The person who drinks water lives in the house just left of the one where the pilot lives.
21. The person who drinks juice lives in the house just left of the one where the owner of the fish lives.
22. The baker enjoys cooking.
23. The person who keeps the fish and the pilot are not neighbours.
24. The painting enthusiast and the pilot live two houses apart.
25. The Spaniard lives directly to the left of whoever lives in the purple house.
26. The lawyer is the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
