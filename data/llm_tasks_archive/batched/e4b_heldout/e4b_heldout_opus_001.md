# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_opus_001.out.json with this exact structure
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

## Puzzle e4b-g0-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Clues:
1. The Dane and the Norwegian live two houses apart.
2. The person who enjoys golf does not live in the yellow house.
3. There is exactly one house between the baker and the tea drinker.
4. The water drinker lives in the first house.
5. The German lives somewhere to the left of the hiking enthusiast.
6. The Brit and the person in the purple house live two houses apart.
7. The person in the blue house is the Spaniard.
8. The person who enjoys tennis lives directly to the left of the doctor.
9. The cooking enthusiast either works as the baker or works as the lawyer.
10. The person who drinks milk lives somewhere to the left of the hiking enthusiast.
11. The farmer either lives in the purple house or lives in the red house.
12. The person who keeps the horse enjoys chess.
13. The cocoa drinker either enjoys chess or enjoys painting.
14. The lawyer is the Swede.
15. The pilot lives in house 4.
16. The occupant of the white house lives directly to the left of the golf enthusiast.
17. The occupant of the red house lives in house 1.
18. The occupant of the green house enjoys chess.
19. The juice drinker lives in the white house.
20. The owner of the fish either is the Spaniard or is the Swede.
21. The Spaniard lives in house 2.
22. The owner of the dog lives in the yellow house.
23. The pilot is the Dane.
24. The owner of the cat and the person who drinks coffee are not neighbours.
25. The person who keeps the bird drinks milk.

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
