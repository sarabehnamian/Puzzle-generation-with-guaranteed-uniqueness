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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/pilot_e1_encB/pilot_e1_encB_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra-00001

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Dane, Spaniard, Brit
- pet: fish, dog, bird, cat, rabbit
- job: teacher, doctor, farmer, lawyer, baker
- drink: cocoa, juice, coffee, milk, water

Clues:
1. The baker and the Brit live two houses apart.
2. The person who keeps the bird lives in the third house.
3. The Spaniard does not live in house 2.
4. The person who drinks coffee lives in the leftmost house.
5. The teacher lives directly to the left of the cocoa drinker.
6. The farmer drinks water.
7. The doctor lives in the first house.
8. The German drinks water.
9. The dog owner lives in the first house.
10. The person who keeps the cat lives directly to the left of the Dane.
11. The juice drinker is the Brit.
12. The juice drinker either keeps the dog or keeps the fish.

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

## Puzzle zebra-00013

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, fish, bird
- job: doctor, baker, pilot, teacher, lawyer
- drink: milk, juice, cocoa, water, tea
- color: white, red, blue, yellow, green

Clues:
1. The baker lives in the last house.
2. The juice drinker either keeps the bird or keeps the fish.
3. The owner of the fish lives immediately to the right of the rabbit owner.
4. Whoever lives in the green house lives in house 3.
5. Whoever lives in the yellow house drinks juice.
6. The water drinker does not live next to whoever lives in the white house.
7. The teacher keeps the rabbit.
8. The owner of the bird lives somewhere to the right of the horse owner.
9. The person who drinks cocoa does not live in the blue house.
10. The person in the blue house lives in house 1.
11. The bird owner and the water drinker live two houses apart.
12. The person who drinks milk and the person in the white house live two houses apart.
13. The person who keeps the horse works as the lawyer.
14. The doctor and the person in the yellow house live in adjacent houses.

## Puzzle zebra-00016

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, baker, doctor, farmer
- hobby: cooking, chess, hiking, painting, tennis
- drink: cocoa, milk, juice, water, coffee
- color: red, blue, yellow, purple, green

Clues:
1. The person who enjoys chess and the doctor are not neighbours.
2. The person in the blue house lives immediately to the right of the person who enjoys hiking.
3. There is exactly one house between the occupant of the blue house and the person in the yellow house.
4. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
5. The pilot lives in the fifth house.
6. The person who drinks coffee works as the pilot.
7. Whoever lives in the red house either works as the doctor or works as the lawyer.
8. The occupant of the green house drinks water.
9. The person who drinks cocoa either works as the farmer or works as the pilot.
10. The person in the purple house lives immediately to the right of the baker.
11. The person who drinks milk enjoys painting.
12. Whoever lives in the red house lives in a lower-numbered house than the juice drinker.
13. There is exactly one house between the person in the green house and the pilot.

## Puzzle zebra-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, farmer, pilot, teacher
- drink: cocoa, milk, tea, water, coffee
- pet: bird, fish, horse, rabbit, dog
- nationality: German, Brit, Swede, Dane, Norwegian

Clues:
1. The Dane and the German live two houses apart.
2. There is exactly one house between the Norwegian and the teacher.
3. The owner of the fish lives next to the German.
4. The farmer lives next to the Norwegian.
5. The owner of the rabbit either works as the farmer or works as the pilot.
6. The owner of the horse lives directly to the left of the person who keeps the fish.
7. The bird owner works as the doctor.
8. The teacher lives in the house just left of the one where the coffee drinker lives.
9. The German lives next to the person who drinks tea.
10. The tea drinker either is the Brit or is the Norwegian.
11. The person who keeps the fish drinks cocoa.
12. The Brit lives next to the person who drinks milk.
13. The Swede is not the doctor.
14. The pilot lives directly to the left of the owner of the bird.
15. The milk drinker lives in house 2.

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

## Puzzle zebra-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, rabbit, fish
- color: purple, green, yellow, blue, white
- drink: coffee, milk, water, juice, tea
- hobby: chess, hiking, tennis, painting, cooking

Clues:
1. The juice drinker lives in the purple house.
2. There is exactly one house between the fish owner and the person in the green house.
3. The rabbit owner lives in the white house.
4. The person who drinks coffee lives in the blue house.
5. The person who enjoys tennis lives directly to the left of the person who drinks milk.
6. The person who enjoys painting lives in the house just left of the one where the person who enjoys hiking lives.
7. The person who keeps the horse and the person in the white house live two houses apart.
8. Whoever lives in the white house drinks milk.
9. The person in the blue house and whoever lives in the purple house live two houses apart.
10. The painting enthusiast lives next to the tea drinker.
11. The person who enjoys hiking lives somewhere to the right of the person in the white house.
12. The person who drinks juice keeps the cat.
13. The painting enthusiast lives somewhere to the left of the person who keeps the dog.
14. The person who enjoys cooking and the hiking enthusiast are neighbours.

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
