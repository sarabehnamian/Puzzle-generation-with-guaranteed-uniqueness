# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_005.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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

## Puzzle e4b-g1-09

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Clues:
1. The milk drinker lives in a lower-numbered house than the person who enjoys hiking.
2. The Brit lives in the house just left of the one where the rabbit owner lives.
3. The pilot and the lawyer are neighbours.
4. The person who drinks milk keeps the bird.
5. The Brit and the person who drinks tea live two houses apart.
6. The chess enthusiast is the Norwegian.
7. The Dane works as the pilot.
8. The occupant of the blue house is the Spaniard.
9. The person who drinks cocoa either enjoys chess or enjoys painting.
10. There is exactly one house between the Brit and whoever lives in the purple house.
11. The person in the red house lives in house 1.
12. The lawyer is the Swede.
13. The person in the yellow house keeps the dog.
14. The cat owner does not live next to the person who drinks coffee.
15. Whoever lives in the white house drinks juice.
16. The person who drinks water lives in house 1.
17. The Dane and the Norwegian live two houses apart.
18. The person who keeps the horse enjoys chess.
19. The person who enjoys cooking either works as the baker or works as the lawyer.
20. The farmer either lives in the purple house or lives in the red house.
21. The baker and the person who drinks tea live two houses apart.
22. The Spaniard lives immediately to the right of the German.
23. The German lives somewhere to the left of the person who enjoys hiking.
24. The person in the white house lives in the house just left of the one where the person who enjoys golf lives.
25. The owner of the fish either is the Spaniard or is the Swede.
26. The person who enjoys chess lives in the green house.
27. The person in the yellow house and the golf enthusiast are different people.
28. The tennis enthusiast lives directly to the left of the doctor.
29. The person who drinks cocoa does not live in house 3.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The teacher lives directly to the left of the Norwegian.
2. The person in the red house lives in a lower-numbered house than the owner of the rabbit.
3. The milk drinker enjoys tennis.
4. The Spaniard enjoys golf.
5. The chess enthusiast lives next to the doctor.
6. The Brit lives immediately to the right of whoever lives in the blue house.
7. The fish owner and the horse owner are neighbours.
8. Whoever lives in the red house lives somewhere to the left of the Spaniard.
9. The teacher lives in the house just left of the one where the person in the blue house lives.
10. The occupant of the white house is the Brit.
11. The fish owner lives immediately to the right of the Norwegian.
12. The Dane and the German are not neighbours.
13. The juice drinker either keeps the horse or keeps the rabbit.
14. The lawyer either drinks milk or drinks water.
15. The baker drinks tea.
16. The cooking enthusiast drinks tea.
17. The person who enjoys cooking is the German.
18. The cooking enthusiast keeps the cat.
19. The Brit lives next to whoever lives in the purple house.
20. The person who drinks milk lives immediately to the right of the baker.
21. There is exactly one house between the cocoa drinker and the juice drinker.
22. The person who drinks water enjoys painting.
23. The water drinker keeps the dog.
24. The person who drinks coffee enjoys golf.
25. The pilot lives in the yellow house.
26. There is exactly one house between the lawyer and the milk drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
