# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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

## Puzzle e4b-g2-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The pilot lives in the yellow house.
2. The dog owner drinks water.
3. The owner of the bird and the lawyer live two houses apart.
4. The rabbit owner lives somewhere to the right of whoever lives in the red house.
5. The juice drinker either keeps the horse or keeps the rabbit.
6. The Dane and the Brit live two houses apart.
7. The person who keeps the fish lives immediately to the right of the Norwegian.
8. The Brit enjoys chess.
9. The fish owner and the horse owner live in adjacent houses.
10. Whoever lives in the blue house lives immediately to the right of the teacher.
11. The German enjoys cooking.
12. The occupant of the white house is the Brit.
13. The coffee drinker lives next to the person who drinks cocoa.
14. The lawyer either drinks milk or drinks water.
15. The lawyer and the milk drinker live two houses apart.
16. The person who drinks cocoa lives in the fifth house.
17. The person who enjoys golf is the Spaniard.
18. The Brit lives immediately to the right of the occupant of the blue house.
19. The Brit and whoever lives in the purple house live in adjacent houses.
20. The baker drinks tea.
21. The owner of the cat lives somewhere to the left of the fish owner.
22. The painting enthusiast drinks water.
23. The tennis enthusiast drinks milk.
24. The baker lives directly to the left of the person who drinks milk.
25. The Spaniard lives somewhere to the right of whoever lives in the red house.
26. The chess enthusiast and the doctor live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
