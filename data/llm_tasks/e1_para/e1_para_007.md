# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_007.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00170

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, yellow, red
- nationality: Norwegian, German, Dane, Swede, Brit
- drink: tea, milk, water, cocoa, coffee
- hobby: hiking, chess, painting, tennis, golf

Clues:
1. The person who enjoys hiking either is the German or is the Swede.
2. The person who drinks tea and the tennis enthusiast are neighbours.
3. The Norwegian and whoever lives in the white house live two houses apart.
4. The person who enjoys hiking lives in the house just left of the one where the person who enjoys painting lives.
5. There is exactly one house between the person who enjoys tennis and the water drinker.
6. There is exactly one house between the person who enjoys hiking and the person who enjoys tennis.
7. The Swede lives somewhere to the right of the person in the white house.
8. The person in the red house either enjoys golf or enjoys hiking.
9. The Dane enjoys golf.
10. The Brit lives next to the German.
11. The milk drinker does not live next to the person who drinks tea.
12. The person who drinks coffee lives next to the Dane.
13. The Swede lives next to whoever lives in the yellow house.
14. Whoever lives in the green house lives in the house just left of the one where the person who enjoys chess lives.
15. The person who enjoys tennis lives somewhere to the right of the Brit.
16. The coffee drinker lives somewhere to the left of the person who drinks cocoa.

## Puzzle zebra-00171

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, German, Spaniard, Swede
- color: blue, purple, white, green, yellow
- drink: coffee, cocoa, tea, water, milk
- job: baker, farmer, lawyer, doctor, pilot

Clues:
1. The person who drinks tea is the Dane.
2. Whoever lives in the blue house either is the Dane or is the German.
3. The person who drinks milk lives next to the pilot.
4. The Dane and the Spaniard live in adjacent houses.
5. The Norwegian and the occupant of the purple house are neighbours.
6. Whoever lives in the yellow house either is the Dane or is the Swede.
7. The doctor either drinks coffee or drinks water.
8. The Swede lives in house 1.
9. The pilot and whoever lives in the green house are different people.
10. The farmer lives in a lower-numbered house than the person in the green house.
11. The Norwegian and the person who drinks water are neighbours.
12. The person who drinks milk lives in one of the two end houses.
13. The farmer lives somewhere to the left of the occupant of the yellow house.
14. The person in the green house does not drink cocoa.
15. The baker and whoever lives in the white house are neighbours.
16. The doctor and the Spaniard are neighbours.

## Puzzle zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The person in the yellow house works as the doctor.
2. The German does not live next to the pilot.
3. The person who keeps the cat either lives in the blue house or lives in the white house.
4. The person in the red house and the occupant of the yellow house live two houses apart.
5. The dog owner lives directly to the left of whoever lives in the yellow house.
6. The bird owner lives somewhere to the left of the Dane.
7. There is exactly one house between the lawyer and whoever lives in the white house.
8. The teacher lives directly to the left of the person who keeps the fish.
9. There is exactly one house between the Brit and the pilot.
10. There is exactly one house between the lawyer and the Norwegian.
11. The Brit and the Dane are not neighbours.
12. The rabbit owner lives in house 2.
13. The Norwegian lives in the house just left of the one where whoever lives in the purple house lives.

## Puzzle zebra-00173

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, lawyer, teacher
- pet: rabbit, bird, fish, cat, horse
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The Swede does not live in the fifth house.
2. The German lives in the house just left of the one where the coffee drinker lives.
3. The doctor and the person who drinks tea live two houses apart.
4. The farmer and the Spaniard are different people.
5. The Spaniard keeps the horse.
6. The doctor is the Brit.
7. The teacher lives in the house just left of the one where the Norwegian lives.
8. The person who drinks cocoa works as the lawyer.
9. The cat owner does not live next to the person who keeps the fish.
10. The Norwegian lives in the house just left of the one where the person who drinks water lives.
11. There is exactly one house between the owner of the bird and the owner of the cat.
12. The Norwegian keeps the rabbit.
13. The person who drinks tea lives in the fifth house.

## Puzzle zebra-00174

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, tea, water, coffee
- job: teacher, pilot, baker, farmer, doctor
- nationality: Dane, German, Swede, Norwegian, Brit
- color: blue, yellow, white, green, red

Clues:
1. The German lives in the house just left of the one where the person who drinks coffee lives.
2. There is exactly one house between the doctor and the person who drinks juice.
3. The teacher lives in the house just left of the one where whoever lives in the green house lives.
4. The person in the blue house and the person who drinks coffee live in adjacent houses.
5. The person who drinks water does not live in the first house.
6. The person who drinks tea lives directly to the left of the farmer.
7. The juice drinker is the Brit.
8. The person in the blue house and the Swede live two houses apart.
9. The teacher drinks coffee.
10. The Dane lives in the house just left of the one where the pilot lives.
11. The farmer lives in the white house.
12. The German either works as the baker or works as the pilot.
13. The person in the red house and whoever lives in the white house live in adjacent houses.

## Puzzle zebra-00175

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, golf, hiking, cooking
- job: pilot, baker, lawyer, teacher, doctor
- drink: water, tea, cocoa, coffee, milk
- color: purple, blue, white, yellow, red

Clues:
1. There is exactly one house between the cocoa drinker and the painting enthusiast.
2. The person who drinks milk lives in the blue house.
3. The teacher and the water drinker live two houses apart.
4. The lawyer lives in the last house.
5. The pilot lives in the house just left of the one where the person in the yellow house lives.
6. The golf enthusiast lives next to the tennis enthusiast.
7. The water drinker and the occupant of the yellow house live two houses apart.
8. The golf enthusiast drinks coffee.
9. The coffee drinker and the lawyer are neighbours.
10. The person who drinks milk enjoys hiking.
11. The person in the purple house lives in the house just left of the one where the tea drinker lives.
12. The cocoa drinker lives in house 1.
13. The baker lives directly to the left of the occupant of the red house.

## Puzzle zebra-00176

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, farmer, teacher, doctor, lawyer
- nationality: Swede, Spaniard, Dane, Brit, German
- color: red, green, yellow, white, blue
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The German lives somewhere to the right of the occupant of the blue house.
2. The Swede lives in house 3.
3. The Dane lives in house 4.
4. The occupant of the green house keeps the cat.
5. The owner of the bird either is the German or is the Spaniard.
6. The farmer is the Brit.
7. The Brit lives directly to the left of the teacher.
8. The doctor is the Dane.
9. The person who keeps the horse lives in the yellow house.
10. The occupant of the white house keeps the rabbit.
11. The owner of the dog and the occupant of the yellow house are not neighbours.
12. The baker and whoever lives in the blue house live two houses apart.
13. The baker and the teacher live two houses apart.
14. The person who keeps the bird lives next to whoever lives in the green house.
15. The person in the yellow house lives somewhere to the right of the baker.

## Puzzle zebra-00177

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- job: baker, farmer, pilot, doctor, lawyer
- color: purple, yellow, green, red, white
- pet: horse, cat, fish, bird, dog

Clues:
1. The owner of the horse drinks tea.
2. The person in the red house lives in the fifth house.
3. The juice drinker lives in the house just left of the one where the fish owner lives.
4. The person who drinks coffee lives in a lower-numbered house than the person in the white house.
5. There is exactly one house between the juice drinker and whoever lives in the yellow house.
6. The person in the yellow house lives at one end of the row.
7. The bird owner and the owner of the fish live two houses apart.
8. The baker lives in the second house.
9. The occupant of the purple house drinks water.
10. There is exactly one house between the dog owner and the tea drinker.
11. The person who drinks cocoa works as the lawyer.
12. The pilot lives immediately to the right of whoever lives in the white house.
13. The doctor and the person in the white house live in adjacent houses.

## Puzzle zebra-00178

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, green, purple, red
- job: farmer, doctor, baker, lawyer, teacher
- drink: juice, coffee, cocoa, milk, tea
- pet: cat, fish, rabbit, bird, horse

Clues:
1. The farmer lives directly to the left of the person who drinks cocoa.
2. The doctor lives in house 5.
3. The occupant of the green house keeps the horse.
4. The bird owner and the person who keeps the fish are neighbours.
5. The person in the red house either keeps the cat or keeps the horse.
6. The teacher lives immediately to the right of the person in the yellow house.
7. The person who keeps the bird lives somewhere to the right of the teacher.
8. The person who drinks juice does not live next to the teacher.
9. Whoever lives in the yellow house either drinks coffee or drinks milk.
10. Whoever lives in the yellow house lives directly to the left of the person who drinks coffee.
11. Whoever lives in the red house lives in house 5.
12. The lawyer lives directly to the left of the person who keeps the bird.
13. The cocoa drinker and the person in the purple house live two houses apart.

## Puzzle zebra-00179

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Swede, Spaniard, Brit
- color: yellow, blue, red, green, white
- drink: cocoa, tea, coffee, water, juice
- job: lawyer, doctor, baker, pilot, farmer

Clues:
1. The German does not live next to the person who drinks water.
2. The occupant of the red house lives immediately to the right of the tea drinker.
3. The Dane lives in the first house.
4. The baker lives at one end of the row.
5. The farmer and the German are neighbours.
6. The lawyer drinks tea.
7. The occupant of the green house and the person who drinks juice live two houses apart.
8. The pilot lives in the blue house.
9. There is exactly one house between the person in the red house and the occupant of the yellow house.
10. The farmer is the Brit.
11. The occupant of the white house lives in the house just left of the one where the Spaniard lives.
12. The Brit lives at one end of the row.
13. The Brit lives somewhere to the right of the cocoa drinker.
14. The person in the red house drinks coffee.
