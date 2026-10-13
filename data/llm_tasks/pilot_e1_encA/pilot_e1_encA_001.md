# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/pilot_e1_encA/pilot_e1_encA_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- pet: rabbit, dog, cat, bird, fish
- color: red, yellow, blue, purple, green
- drink: juice, water, milk, tea, coffee

Clues:
1. The person who drinks coffee and the tea drinker live two houses apart.
2. The cat owner and the person in the purple house live in adjacent houses.
3. The owner of the cat lives in the fourth house.
4. The person who drinks tea lives somewhere to the right of the occupant of the blue house.
5. The fish owner lives in the leftmost house.
6. The occupant of the green house enjoys chess.
7. The occupant of the green house either drinks coffee or drinks milk.
8. The tennis enthusiast either keeps the cat or keeps the dog.
9. There is exactly one house between the person who enjoys golf and the person in the green house.
10. The person who drinks juice enjoys cooking.
11. The person who drinks juice keeps the rabbit.
12. The person who drinks milk either keeps the cat or keeps the dog.
13. The person in the red house lives directly to the left of the tea drinker.
14. The water drinker keeps the cat.

## Puzzle zebra-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- nationality: German, Brit, Norwegian, Swede, Spaniard
- hobby: chess, cooking, painting, tennis, golf
- color: red, purple, white, green, yellow

Clues:
1. The German lives somewhere to the left of whoever lives in the yellow house.
2. The painting enthusiast works as the doctor.
3. There is exactly one house between the cooking enthusiast and the occupant of the red house.
4. The occupant of the white house lives somewhere to the left of the person who enjoys tennis.
5. Whoever lives in the green house works as the baker.
6. The Spaniard lives next to the person who enjoys tennis.
7. The Brit and the Swede are neighbours.
8. There is exactly one house between the cooking enthusiast and the Spaniard.
9. The farmer either is the Norwegian or is the Swede.
10. The golf enthusiast and the teacher are neighbours.
11. The baker is the Brit.
12. The German and the person in the purple house live two houses apart.
13. The golf enthusiast lives directly to the left of the baker.

## Puzzle zebra-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- nationality: Dane, Norwegian, Brit, Spaniard, Swede
- pet: bird, fish, horse, rabbit, dog
- job: farmer, baker, doctor, lawyer, pilot

Clues:
1. The owner of the horse enjoys chess.
2. The Swede either works as the farmer or works as the lawyer.
3. The Swede lives in the third house.
4. The Spaniard lives immediately to the right of the pilot.
5. The owner of the fish and the person who enjoys golf live two houses apart.
6. The Dane is not the farmer.
7. The person who keeps the horse lives somewhere to the left of the hiking enthusiast.
8. The person who keeps the fish lives in a lower-numbered house than the person who enjoys hiking.
9. The person who enjoys cooking works as the pilot.
10. The Norwegian keeps the rabbit.
11. The chess enthusiast either works as the lawyer or works as the pilot.
12. The Brit lives in one of the two end houses.
13. The baker lives immediately to the right of the Norwegian.
14. The owner of the rabbit lives next to the tennis enthusiast.
15. There is exactly one house between the bird owner and the owner of the horse.

## Puzzle zebra-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, baker
- hobby: painting, tennis, cooking, hiking, chess
- color: purple, green, yellow, white, blue
- pet: fish, rabbit, bird, cat, dog

Clues:
1. The chess enthusiast lives in house 4.
2. The person who enjoys tennis lives in the house just left of the one where the person who enjoys hiking lives.
3. The hiking enthusiast lives directly to the left of the owner of the cat.
4. Whoever lives in the yellow house keeps the rabbit.
5. The person in the white house lives immediately to the right of the person in the green house.
6. The owner of the bird works as the baker.
7. The person in the blue house lives directly to the left of the teacher.
8. The lawyer lives in the white house.
9. The person who keeps the dog lives immediately to the right of the pilot.
10. The dog owner lives immediately to the right of the person who enjoys painting.
11. Whoever lives in the green house works as the farmer.

## Puzzle zebra-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Spaniard, Swede, Norwegian, Dane
- drink: milk, cocoa, coffee, tea, juice
- color: blue, purple, red, yellow, green
- pet: dog, bird, cat, horse, rabbit

Clues:
1. The person who drinks coffee lives in the middle house.
2. The horse owner lives in house 5.
3. The bird owner lives in the blue house.
4. The occupant of the green house keeps the cat.
5. The coffee drinker lives next to the juice drinker.
6. The cat owner and the person who drinks coffee are neighbours.
7. Whoever lives in the yellow house lives in house 5.
8. The milk drinker lives in the fourth house.
9. The Spaniard either keeps the horse or keeps the rabbit.
10. The coffee drinker and the Swede live two houses apart.
11. The occupant of the blue house does not live next to the German.
12. The Dane does not live next to the German.
13. The person who drinks tea lives in a lower-numbered house than whoever lives in the purple house.
14. The occupant of the blue house lives in the third house.
15. The rabbit owner lives directly to the left of the owner of the horse.
16. The juice drinker lives next to the Norwegian.

## Puzzle zebra-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, lawyer, farmer, pilot
- nationality: Norwegian, Brit, Swede, German, Spaniard
- drink: milk, cocoa, tea, water, coffee
- color: yellow, purple, red, white, green

Clues:
1. The cocoa drinker lives in the yellow house.
2. The German lives immediately to the right of whoever lives in the yellow house.
3. The person in the green house either is the Brit or is the Norwegian.
4. There is exactly one house between the Swede and the person in the white house.
5. The baker lives somewhere to the left of the pilot.
6. The doctor either drinks coffee or drinks tea.
7. The Swede lives in the second house.
8. The occupant of the purple house drinks tea.
9. The Brit works as the farmer.
10. The person who drinks cocoa lives directly to the left of the lawyer.
11. The cocoa drinker lives somewhere to the left of the Norwegian.
12. The Norwegian works as the doctor.
13. The farmer does not live in the green house.
14. The person who drinks milk is the German.
15. The baker lives next to the lawyer.

## Puzzle zebra-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, water, milk
- job: pilot, teacher, doctor, farmer, baker
- pet: fish, horse, cat, rabbit, dog
- hobby: hiking, cooking, painting, chess, tennis

Clues:
1. There is exactly one house between the baker and the person who drinks milk.
2. The pilot lives at one end of the row.
3. The person who drinks coffee enjoys tennis.
4. The juice drinker either keeps the horse or keeps the rabbit.
5. The person who drinks water works as the pilot.
6. The owner of the cat works as the baker.
7. The person who keeps the rabbit enjoys hiking.
8. The person who enjoys chess lives in one of the two end houses.
9. The coffee drinker lives at one end of the row.
10. The teacher lives in the third house.
11. The doctor lives immediately to the right of the person who keeps the rabbit.
12. The person who enjoys cooking does not live in the fourth house.
13. The person who enjoys tennis lives directly to the left of the dog owner.

## Puzzle zebra-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, bird, fish, rabbit
- job: farmer, teacher, baker, doctor, lawyer
- hobby: golf, tennis, chess, hiking, cooking
- nationality: Brit, German, Spaniard, Norwegian, Swede

Clues:
1. The Spaniard lives in the house just left of the one where the hiking enthusiast lives.
2. The German lives next to the teacher.
3. The baker keeps the rabbit.
4. The tennis enthusiast lives in house 4.
5. The Norwegian keeps the rabbit.
6. The person who keeps the bird and the person who enjoys golf are neighbours.
7. The cooking enthusiast and the German live two houses apart.
8. The lawyer lives directly to the left of the farmer.
9. The owner of the bird works as the teacher.
10. The cooking enthusiast and the person who keeps the dog are neighbours.
11. There is exactly one house between the farmer and the horse owner.
12. The Swede lives in the house just left of the one where the horse owner lives.

## Puzzle zebra-00004

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: purple, green, yellow, blue, white
- pet: rabbit, horse, bird, fish, dog
- job: baker, doctor, teacher, farmer, lawyer

Clues:
1. The farmer is the Brit.
2. The person in the purple house lives directly to the left of the owner of the rabbit.
3. The German lives in the house just left of the one where the dog owner lives.
4. Whoever lives in the yellow house either keeps the fish or keeps the horse.
5. Whoever lives in the green house lives in the fourth house.
6. The person in the blue house and the person who keeps the dog live two houses apart.
7. The baker does not live next to the German.
8. The person who keeps the dog works as the farmer.
9. The fish owner lives in the leftmost house.
10. The Norwegian and the Spaniard are neighbours.
11. The Norwegian does not live next to the person in the yellow house.
12. Whoever lives in the purple house works as the lawyer.
13. The teacher lives in the yellow house.
14. The horse owner lives directly to the left of the person in the green house.

## Puzzle zebra-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, doctor, teacher, lawyer, farmer
- nationality: Dane, Brit, Norwegian, German, Swede
- drink: juice, water, tea, coffee, cocoa
- hobby: golf, tennis, painting, chess, cooking

Clues:
1. The person who drinks water lives in one of the two end houses.
2. The golf enthusiast and the juice drinker are not neighbours.
3. The Brit and the Dane are not neighbours.
4. The coffee drinker and the cooking enthusiast live two houses apart.
5. The person who enjoys cooking works as the doctor.
6. The Norwegian lives somewhere to the right of the person who drinks cocoa.
7. The teacher is the Norwegian.
8. The person who drinks juice lives next to the Norwegian.
9. The teacher lives at one end of the row.
10. The person who enjoys painting lives directly to the left of the Swede.
11. The person who drinks tea works as the lawyer.
12. The Brit and the painting enthusiast live two houses apart.
13. The person who enjoys tennis lives in the house just left of the one where the Dane lives.
14. The farmer does not live in house 3.
15. There is exactly one house between the person who drinks juice and the pilot.
