# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. The Norwegian lives directly to the left of the German.
2. The cocoa drinker either works as the doctor or works as the pilot.
3. The lawyer enjoys golf.
4. The owner of the fish works as the pilot.
5. The farmer keeps the bird.
6. The golf enthusiast and the tea drinker live in adjacent houses.
7. There is exactly one house between whoever lives in the blue house and the doctor.
8. The Norwegian and whoever lives in the yellow house are neighbours.
9. The person who enjoys chess and the lawyer live two houses apart.
10. The occupant of the yellow house lives in the house just left of the one where the owner of the horse lives.
11. The person in the green house lives immediately to the right of the tea drinker.
12. The owner of the rabbit either is the Dane or is the German.
13. Whoever lives in the blue house drinks juice.
14. The tennis enthusiast lives in the white house.
15. Whoever lives in the white house is the Brit.
16. The baker either keeps the horse or keeps the rabbit.
17. The person in the purple house and the coffee drinker are different people.
18. Whoever lives in the green house and the person who enjoys tennis live in adjacent houses.
19. The cat owner lives next to the person in the purple house.
20. The person who drinks coffee enjoys painting.
21. The farmer and the person in the red house live two houses apart.
22. The person who keeps the dog either works as the lawyer or works as the teacher.
23. The owner of the fish enjoys cooking.
24. The owner of the horse lives immediately to the right of the rabbit owner.
25. The water drinker lives in a lower-numbered house than the Swede.
26. The occupant of the yellow house enjoys chess.
27. The German lives in one of the two end houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The person who enjoys golf is the Spaniard.
2. The person who drinks cocoa lives somewhere to the right of the milk drinker.
3. The person who enjoys golf drinks coffee.
4. The pilot lives in the yellow house.
5. The tennis enthusiast drinks milk.
6. The person who drinks juice either keeps the horse or keeps the rabbit.
7. The person who enjoys chess and the doctor are neighbours.
8. Whoever lives in the blue house lives directly to the left of the Brit.
9. The teacher lives in the house just left of the one where the occupant of the blue house lives.
10. The person who keeps the rabbit lives somewhere to the right of whoever lives in the red house.
11. The person who drinks coffee lives next to the cocoa drinker.
12. The owner of the fish and the owner of the horse live in adjacent houses.
13. The baker drinks tea.
14. The German enjoys cooking.
15. The water drinker enjoys painting.
16. The baker lives directly to the left of the milk drinker.
17. There is exactly one house between the owner of the bird and the lawyer.
18. The owner of the dog drinks water.
19. The Brit and the person in the purple house are neighbours.
20. The person who keeps the cat lives in a lower-numbered house than the person who keeps the fish.
21. The Dane lives in the third house.
22. The lawyer either drinks milk or drinks water.
23. The Spaniard lives somewhere to the right of whoever lives in the red house.
24. There is exactly one house between the lawyer and the milk drinker.
25. The Norwegian lives directly to the left of the fish owner.
26. The person in the white house is the Brit.

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
