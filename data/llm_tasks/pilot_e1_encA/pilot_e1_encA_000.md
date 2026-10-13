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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/pilot_e1_encA/pilot_e1_encA_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra-00007

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Swede, Norwegian
- color: blue, purple, red, white, yellow
- drink: milk, cocoa, juice, coffee, tea
- pet: dog, fish, cat, bird, horse

Clues:
1. The owner of the cat lives in the house just left of the one where the Dane lives.
2. The Norwegian lives in the blue house.
3. The owner of the cat lives directly to the left of the person who keeps the dog.
4. The occupant of the white house either is the Brit or is the Dane.
5. The person who drinks coffee lives in the house just left of the one where the occupant of the blue house lives.
6. The Swede either keeps the bird or keeps the dog.
7. The occupant of the purple house lives directly to the left of the Brit.
8. The person who drinks milk lives in the leftmost house.
9. The person who drinks tea either lives in the blue house or lives in the red house.
10. The milk drinker and the Swede live in adjacent houses.
11. The Brit and the person who drinks coffee live in adjacent houses.
12. The cocoa drinker and the Dane are not neighbours.
13. The owner of the fish lives next to the person in the red house.

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

## Puzzle zebra-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, tennis, hiking, painting, cooking
- drink: cocoa, milk, coffee, water, juice
- pet: cat, fish, bird, rabbit, dog
- job: farmer, lawyer, doctor, pilot, baker

Clues:
1. The dog owner does not live in the first house.
2. The golf enthusiast lives directly to the left of the pilot.
3. The farmer lives directly to the left of the cocoa drinker.
4. The dog owner drinks coffee.
5. The person who drinks milk does not enjoy hiking.
6. The farmer lives directly to the left of the cooking enthusiast.
7. The cocoa drinker and the lawyer are neighbours.
8. The baker keeps the cat.
9. There is exactly one house between the juice drinker and the person who enjoys tennis.
10. The bird owner drinks juice.
11. The owner of the rabbit drinks cocoa.
12. The rabbit owner lives somewhere to the left of the baker.
13. The milk drinker works as the pilot.

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

## Puzzle zebra-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, rabbit, dog
- job: teacher, farmer, pilot, lawyer, baker
- color: purple, green, blue, white, yellow
- nationality: Dane, Brit, Norwegian, Spaniard, German

Clues:
1. The occupant of the white house is the Spaniard.
2. Whoever lives in the blue house and the German live in adjacent houses.
3. The person who keeps the rabbit either lives in the purple house or lives in the white house.
4. The person who keeps the fish and whoever lives in the green house live in adjacent houses.
5. The person who keeps the fish lives somewhere to the right of the Norwegian.
6. The teacher lives somewhere to the left of the person who keeps the horse.
7. The farmer lives next to the Norwegian.
8. The occupant of the white house lives in the house just left of the one where the Dane lives.
9. The person who keeps the horse lives in the house just left of the one where the occupant of the yellow house lives.
10. There is exactly one house between the occupant of the blue house and the Spaniard.
11. The owner of the horse either works as the lawyer or works as the pilot.
12. The farmer keeps the cat.
13. The person in the blue house and the pilot live in adjacent houses.
14. The baker and the Brit live two houses apart.

## Puzzle zebra-00012

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, coffee, milk, juice
- hobby: cooking, tennis, painting, hiking, chess
- job: lawyer, pilot, farmer, doctor, teacher
- color: green, blue, white, yellow, purple

Clues:
1. The chess enthusiast lives in the second house.
2. The person in the green house and the person in the purple house live in adjacent houses.
3. The farmer drinks cocoa.
4. The farmer lives in the house just left of the one where the lawyer lives.
5. The tennis enthusiast works as the farmer.
6. The person who drinks coffee lives next to the hiking enthusiast.
7. There is exactly one house between whoever lives in the blue house and the person who drinks juice.
8. The teacher lives in the third house.
9. The person who drinks tea and the tennis enthusiast live two houses apart.
10. Whoever lives in the green house does not live in house 4.
11. The person who enjoys chess lives in the white house.
12. The person who enjoys painting and whoever lives in the white house live in adjacent houses.
13. The person who drinks tea lives directly to the left of the pilot.

## Puzzle zebra-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, dog, fish, bird
- nationality: Spaniard, German, Norwegian, Dane, Swede
- job: baker, doctor, farmer, pilot, lawyer
- color: yellow, blue, white, green, red

Clues:
1. The horse owner either is the German or is the Spaniard.
2. The owner of the fish lives in the house just left of the one where the dog owner lives.
3. The doctor lives in house 4.
4. The bird owner does not live in the fifth house.
5. Whoever lives in the blue house works as the doctor.
6. The rabbit owner lives directly to the left of the farmer.
7. The lawyer lives in the green house.
8. There is exactly one house between the occupant of the green house and the occupant of the yellow house.
9. The occupant of the red house is not the German.
10. The German lives in the second house.
11. The Norwegian does not live in the third house.
12. The pilot lives next to the Spaniard.
13. The Swede lives in the green house.
14. The baker and the owner of the dog live two houses apart.

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
