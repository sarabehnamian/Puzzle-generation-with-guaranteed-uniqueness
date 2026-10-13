# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e3_solve/e3_zebra_sonnet_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00478

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, German, Brit, Swede
- drink: cocoa, tea, juice, milk, coffee
- pet: rabbit, cat, horse, bird, fish
- job: teacher, pilot, baker, farmer, lawyer

Clues:
1. The Spaniard lives in house 5.
2. The Brit and the pilot are not neighbours.
3. The person who drinks juice lives in house 4.
4. The person who keeps the bird lives somewhere to the right of the Swede.
5. The Swede and the tea drinker live two houses apart.
6. The Brit either drinks cocoa or drinks milk.
7. The Brit does not keep the horse.
8. The bird owner works as the baker.
9. The owner of the fish lives in the house just left of the one where the horse owner lives.
10. The German lives immediately to the right of the lawyer.
11. The pilot drinks cocoa.
12. The person who keeps the cat works as the teacher.
13. The juice drinker and the milk drinker live two houses apart.
14. The horse owner and the teacher live two houses apart.
15. The person who drinks juice and the German are different people.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01103-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, yellow, blue, red, purple
- drink: coffee, juice, milk, water, tea
- job: teacher, pilot, baker, doctor, lawyer
- nationality: Brit, Spaniard, Swede, Dane, German

Clues:
1. The baker lives directly to the left of the doctor.
2. The person in the blue house lives in the fourth house.
3. The person who drinks milk lives next to the pilot.
4. The occupant of the white house works as the baker.
5. The Spaniard lives in the house just left of the one where the baker lives.
6. The doctor lives in the fourth house.
7. Whoever lives in the red house is the Brit.
8. Whoever lives in the purple house lives directly to the left of the Swede.
9. There is exactly one house between the German and the person who drinks water.
10. The Brit lives immediately to the right of the Dane.
11. The baker and whoever lives in the purple house are neighbours.
12. The person in the yellow house lives in a lower-numbered house than the Swede.
13. There is exactly one house between the Swede and the teacher.
14. The coffee drinker lives in the blue house.
15. Whoever lives in the blue house is not the Swede.
16. The Brit works as the lawyer.
17. The juice drinker lives in the second house.
18. Whoever lives in the white house is not the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00704-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Norwegian
- color: red, yellow, green, white, purple
- drink: coffee, cocoa, tea, milk, water
- pet: dog, bird, cat, horse, fish

Clues:
1. The tea drinker and whoever lives in the white house are not neighbours.
2. The coffee drinker lives in house 3.
3. The occupant of the purple house does not keep the horse.
4. The Norwegian and whoever lives in the red house are not neighbours.
5. The horse owner lives somewhere to the right of the Dane.
6. The person who keeps the dog lives in the red house.
7. The dog owner and the person who keeps the fish live in adjacent houses.
8. The cat owner lives in the second house.
9. The Norwegian lives in the purple house.
10. The person who keeps the fish drinks coffee.
11. The person in the purple house does not drink water.
12. The person who drinks tea is the German.
13. The person in the yellow house either drinks cocoa or drinks water.
14. The cocoa drinker lives directly to the left of whoever lives in the green house.
15. The person who drinks coffee and the person in the yellow house are neighbours.
16. There is exactly one house between the fish owner and the person who drinks milk.
17. Whoever lives in the white house does not keep the cat.
18. The occupant of the purple house is not the Spaniard.
19. Whoever lives in the green house does not live next to the person who drinks water.
20. The owner of the fish lives in the white house.
21. The water drinker lives in a lower-numbered house than the person who keeps the dog.
22. The occupant of the yellow house lives in a lower-numbered house than the Brit.
23. Whoever lives in the red house lives in the fourth house.
24. The cocoa drinker is the Brit.
25. The Spaniard drinks water.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00369

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, cooking, painting, golf, tennis
- drink: cocoa, coffee, juice, milk, tea
- color: yellow, purple, blue, red, white
- pet: horse, bird, fish, rabbit, dog

Clues:
1. The occupant of the white house lives directly to the left of the owner of the horse.
2. The person in the blue house lives in a lower-numbered house than the person who keeps the dog.
3. The person who enjoys chess lives in the first house.
4. The person who drinks cocoa keeps the dog.
5. The juice drinker lives in the yellow house.
6. The person who keeps the fish lives in a lower-numbered house than the milk drinker.
7. The person who keeps the bird drinks juice.
8. The person in the yellow house lives in the house just left of the one where whoever lives in the red house lives.
9. The person who keeps the dog enjoys cooking.
10. The occupant of the red house lives in the house just left of the one where the person who drinks coffee lives.
11. The owner of the rabbit lives directly to the left of the person who enjoys painting.
12. The golf enthusiast lives in the yellow house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00829

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, white, purple, green, blue
- drink: coffee, juice, cocoa, milk, water
- nationality: Spaniard, Norwegian, Dane, German, Swede
- hobby: hiking, cooking, chess, painting, golf

Clues:
1. The Norwegian lives in the green house.
2. The person who drinks milk lives at one end of the row.
3. The painting enthusiast and whoever lives in the white house are neighbours.
4. The Dane and the hiking enthusiast are neighbours.
5. The person who drinks cocoa lives in the house just left of the one where the person who enjoys golf lives.
6. The Spaniard either drinks cocoa or drinks milk.
7. The person in the green house lives next to the Spaniard.
8. The person in the purple house lives somewhere to the right of the Dane.
9. The person in the red house lives directly to the left of the coffee drinker.
10. The person who drinks water lives in the house just left of the one where whoever lives in the green house lives.
11. The cooking enthusiast lives immediately to the right of the German.
12. The German and whoever lives in the white house live two houses apart.
13. Whoever lives in the red house lives somewhere to the right of the person who enjoys hiking.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
