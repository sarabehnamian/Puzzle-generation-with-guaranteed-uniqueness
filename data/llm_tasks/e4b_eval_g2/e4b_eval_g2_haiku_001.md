# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g2/e4b_eval_g2_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-10

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. The cat owner is the Brit.
2. The Brit and the person who keeps the dog live two houses apart.
3. The person who keeps the bird and the farmer live two houses apart.
4. The person who keeps the rabbit and the tea drinker live two houses apart.
5. The person who drinks cocoa lives in the red house.
6. The person in the blue house lives immediately to the right of the German.
7. The Brit drinks water.
8. The doctor lives at one end of the row.
9. The person who keeps the dog lives directly to the left of the Spaniard.
10. Whoever lives in the purple house and the occupant of the red house live in adjacent houses.
11. The person who drinks juice enjoys chess.
12. The German and the person who enjoys tennis are neighbours.
13. The lawyer and the teacher are neighbours.
14. The cooking enthusiast lives in the first house.
15. The occupant of the white house lives directly to the left of the lawyer.
16. The bird owner enjoys painting.
17. The person who drinks water lives immediately to the right of the baker.
18. The person who drinks juice lives immediately to the right of the Norwegian.
19. The doctor does not live next to the pilot.
20. The owner of the fish lives directly to the left of the Dane.
21. Whoever lives in the red house is the Norwegian.
22. There is exactly one house between the German and the teacher.
23. The person who enjoys golf lives immediately to the right of the Brit.
24. Whoever lives in the green house lives at one end of the row.
25. There is exactly one house between the baker and the German.
26. The German lives somewhere to the left of the rabbit owner.
27. The milk drinker and the tea drinker live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. The dog owner lives in the house just left of the one where the Spaniard lives.
2. There is exactly one house between the Brit and the person who keeps the dog.
3. The baker and the German live two houses apart.
4. The pilot lives in the fourth house.
5. The Brit lives in the house just left of the one where the golf enthusiast lives.
6. There is exactly one house between the person who keeps the rabbit and the person who drinks tea.
7. The occupant of the green house lives at one end of the row.
8. The person who drinks milk and the person who drinks tea are neighbours.
9. Whoever lives in the purple house and the occupant of the red house are neighbours.
10. The cooking enthusiast lives in house 1.
11. The person who drinks cocoa lives in the red house.
12. Whoever lives in the blue house lives immediately to the right of the German.
13. The German lives in a lower-numbered house than the owner of the rabbit.
14. Whoever lives in the red house is the Norwegian.
15. The person in the white house lives in the house just left of the one where the lawyer lives.
16. The doctor lives in the first house.
17. The Brit keeps the cat.
18. The lawyer lives next to the teacher.
19. The water drinker is the Brit.
20. The person who drinks juice enjoys chess.
21. The juice drinker lives immediately to the right of the Norwegian.
22. There is exactly one house between the German and the teacher.
23. The bird owner enjoys painting.
24. The German and the tennis enthusiast are neighbours.
25. The fish owner lives directly to the left of the Dane.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, baker, pilot, doctor, teacher
- hobby: tennis, hiking, golf, chess, painting, cooking
- pet: rabbit, bird, fish, cat, dog, horse
- color: green, blue, white, yellow, red, purple
- drink: cocoa, juice, milk, tea, coffee, water
- nationality: Brit, Norwegian, German, Swede, Spaniard, Dane

Clues:
1. Whoever lives in the green house lives immediately to the right of the owner of the rabbit.
2. The tennis enthusiast lives in the house just left of the one where the teacher lives.
3. The juice drinker is the Norwegian.
4. The baker lives immediately to the right of the person who keeps the horse.
5. There is exactly one house between the farmer and the occupant of the white house.
6. The Dane lives next to the person who keeps the rabbit.
7. The person in the purple house either drinks juice or drinks tea.
8. The painting enthusiast drinks coffee.
9. The person who enjoys hiking is the Norwegian.
10. The occupant of the blue house and the occupant of the green house are not neighbours.
11. The cocoa drinker enjoys golf.
12. The person who keeps the cat and the German are neighbours.
13. The owner of the bird lives in house 6.
14. The bird owner lives next to whoever lives in the red house.
15. The baker lives immediately to the right of the farmer.
16. The owner of the fish works as the lawyer.
17. The person who drinks water lives at one end of the row.
18. The milk drinker lives immediately to the right of the dog owner.
19. The Brit keeps the rabbit.
20. The person who enjoys cooking lives in the house just left of the one where whoever lives in the green house lives.
21. The person who enjoys chess and the person in the green house live in adjacent houses.
22. The Norwegian and the rabbit owner are neighbours.
23. The person who enjoys painting works as the pilot.
24. Whoever lives in the green house enjoys golf.
25. Whoever lives in the yellow house lives somewhere to the left of the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The occupant of the green house lives somewhere to the right of whoever lives in the yellow house.
2. Whoever lives in the blue house lives in house 4.
3. The person who enjoys hiking lives in the house just left of the one where the owner of the cat lives.
4. The Spaniard lives directly to the left of whoever lives in the purple house.
5. The milk drinker lives in the third house.
6. The person who keeps the fish does not live next to the pilot.
7. The fish owner lives immediately to the right of the person who drinks juice.
8. The Brit lives in house 5.
9. The person who drinks cocoa and the teacher live two houses apart.
10. The cocoa drinker either lives in the blue house or lives in the yellow house.
11. The owner of the horse lives in the yellow house.
12. The doctor lives next to the person in the red house.
13. The occupant of the green house drinks tea.
14. The painting enthusiast and the pilot live two houses apart.
15. The Norwegian lives directly to the left of the tennis enthusiast.
16. The cocoa drinker lives somewhere to the left of the coffee drinker.
17. There is exactly one house between the teacher and the person who enjoys tennis.
18. The person who enjoys cooking works as the baker.
19. The owner of the bird lives somewhere to the left of the Swede.
20. The Swede lives in the third house.
21. The lawyer is the Swede.
22. The farmer lives in the house just left of the one where the person who enjoys chess lives.
23. The cat owner lives in house 6.
24. There is exactly one house between the Dane and the person who keeps the rabbit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
