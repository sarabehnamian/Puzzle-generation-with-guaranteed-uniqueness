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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_010.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00071

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, purple, red, yellow, blue
- job: pilot, teacher, farmer, lawyer, baker
- nationality: Swede, Spaniard, Dane, Norwegian, German
- drink: water, cocoa, milk, juice, tea

Clues:
1. The Spaniard lives in the house just left of the one where the occupant of the red house lives.
2. Whoever lives in the white house drinks juice.
3. The person in the blue house lives somewhere to the right of the Dane.
4. The German lives in house 5.
5. The baker lives in the purple house.
6. The farmer lives directly to the left of the Spaniard.
7. The Spaniard lives in the middle house.
8. The person who drinks cocoa is the Swede.
9. The pilot and the Swede live in adjacent houses.
10. The person who drinks tea lives in the house just left of the one where the teacher lives.
11. The Dane either drinks cocoa or drinks milk.
12. The Norwegian lives in the house just left of the one where the baker lives.
13. The farmer either drinks cocoa or drinks juice.

## Puzzle hard:zebra_hard-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, juice, cocoa, water, coffee
- job: teacher, lawyer, baker, farmer, doctor
- nationality: Dane, Swede, Brit, German, Spaniard
- hobby: chess, golf, cooking, hiking, painting

Clues:
1. One of the neighbours of the painting enthusiast enjoys hiking.
2. If the lawyer does not drink cocoa, then that person drinks coffee.
3. Exactly 3 houses lie to the left of the home of the teacher.
4. The right-hand neighbour of the person who drinks cocoa is the Brit.
5. The Dane has only one neighbour.
6. If the German is not the doctor, then that person works as the farmer.
7. The right-hand neighbour of the doctor enjoys cooking.
8. The person who enjoys hiking has only one neighbour.
9. Exactly 1 house lies to the left of the home of the person who drinks water.
10. One of the neighbours of the Spaniard works as the teacher.
11. The chess enthusiast and the Spaniard are one and the same person.
12. The doctor lives somewhere between the Brit and the farmer.
13. The left-hand neighbour of the doctor drinks milk.
14. The Brit is not the same person as the juice drinker.

## Puzzle paraphrase:zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. The milk drinker lives in house 4.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker are neighbours.
6. The pilot is the one who keeps the cat.
7. The dog keeper does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The horse is kept by the painting enthusiast.
10. The coffee drinker lives next door to the painting enthusiast.
11. The horse owner lives in the third house.
12. The bird owner lives in the house immediately left of the teacher's.
13. The chess enthusiast and the water drinker live two houses apart.
14. The hiking enthusiast lives in a lower-numbered house than the tennis enthusiast.

## Puzzle plain:zebra-00046

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Norwegian, Spaniard, Swede
- color: yellow, blue, green, purple, white
- drink: milk, tea, water, cocoa, coffee
- hobby: golf, tennis, hiking, chess, painting

Clues:
1. The German and the person who enjoys painting are neighbours.
2. The Norwegian either enjoys painting or enjoys tennis.
3. The Dane either lives in the blue house or lives in the white house.
4. The Norwegian lives in the white house.
5. The person in the yellow house lives in a lower-numbered house than whoever lives in the white house.
6. Whoever lives in the green house lives next to the milk drinker.
7. The Spaniard lives in the yellow house.
8. The person who enjoys golf lives in the house just left of the one where the hiking enthusiast lives.
9. The tennis enthusiast lives in a lower-numbered house than the person who drinks milk.
10. The person who enjoys golf is the Swede.
11. The tennis enthusiast drinks coffee.
12. The water drinker lives at one end of the row.
13. The person who drinks cocoa lives immediately to the right of the person who enjoys tennis.
14. The occupant of the purple house lives somewhere to the right of the golf enthusiast.
15. The Dane and the person in the white house live two houses apart.

## Puzzle hard:zebra_hard-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, juice, cocoa
- pet: fish, rabbit, dog, bird, horse
- hobby: chess, tennis, cooking, hiking, golf
- color: red, blue, green, purple, white

Clues:
1. Whoever lives in the white house lives somewhere between the bird owner and the occupant of the purple house.
2. Exactly one house separates the person who keeps the bird from the juice drinker.
3. If the person in the purple house does not keep the bird, then that person keeps the dog.
4. Exactly 3 houses lie to the left of the home of the milk drinker.
5. The cocoa drinker is not the same person as the cooking enthusiast.
6. None of the neighbours of the fish owner drinks juice.
7. The person in the green house lives two doors away from whoever lives in the white house.
8. The person who keeps the bird lives somewhere between the coffee drinker and the juice drinker.
9. The occupant of the white house lives somewhere between the person who drinks cocoa and the golf enthusiast.
10. Exactly 3 houses lie to the left of the home of the tennis enthusiast.
11. The person who enjoys chess lives in the fourth house from the right.
12. One of the neighbours of the person who drinks water lives in the red house.
13. The left-hand neighbour of the owner of the fish lives in the purple house.
14. One of the neighbours of the owner of the horse lives in the green house.

## Puzzle paraphrase:zebra-00174

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, tea, water, coffee
- job: teacher, pilot, baker, farmer, doctor
- nationality: Dane, German, Swede, Norwegian, Brit
- color: blue, yellow, white, green, red

Clues:
1. The German lives immediately to the left of the coffee drinker.
2. The doctor and the juice drinker have exactly one house between them.
3. The teacher lives immediately to the left of the green house.
4. The blue house and the coffee drinker are in adjacent houses.
5. The water drinker does not live in the first house.
6. The tea drinker lives immediately to the left of the farmer.
7. The Brit is the juice drinker.
8. The blue house and the Swede are two houses apart.
9. The teacher is the coffee drinker.
10. The Dane lives immediately to the left of the pilot.
11. The farmer lives in the white house.
12. The German works as either the baker or the pilot.
13. The red house and the white house are next to each other.

## Puzzle paraphrase:zebra-00184

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, dog, cat, bird
- color: purple, green, blue, white, red
- nationality: German, Dane, Norwegian, Spaniard, Brit
- drink: milk, water, coffee, cocoa, juice

Clues:
1. The Norwegian is the one who drinks water.
2. The cocoa drinker lives at one end of the row.
3. The Dane lives immediately to the left of the Spaniard.
4. The fish owner lives somewhere to the right of the horse owner.
5. The blue house is immediately to the left of the coffee drinker's house.
6. The Spaniard lives immediately to the left of the milk drinker.
7. One house lies between the coffee drinker and the white house.
8. The bird owner is either the Brit or the Dane.
9. The German drinks either coffee or juice.
10. The fish owner drinks coffee.
11. The red house is house 5.
12. One house separates the cat owner from the purple house.
13. The green house and the Spaniard are two houses apart.

## Puzzle paraphrase:zebra-00100

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, horse, cat, fish
- drink: tea, water, juice, coffee, milk
- hobby: chess, tennis, painting, cooking, hiking
- job: lawyer, pilot, doctor, baker, farmer

Clues:
1. The doctor and the farmer live next door to each other.
2. The milk drinker lives in house 3.
3. Somewhere to the left of the chess enthusiast lives the cat owner.
4. The juice drinker lives directly to the left of the cooking enthusiast.
5. One house separates the coffee drinker from the farmer.
6. The cooking enthusiast lives right next to the horse keeper, on the left side.
7. The doctor's house has a lower number than the lawyer's.
8. The dog owner lives immediately to the left of the tennis enthusiast.
9. The fish owner and the tea drinker are neighbours.
10. Two houses separate the cooking enthusiast's home from the hiker's... that is, they live two houses apart.
11. The doctor and the lawyer live two houses apart.
12. The baker occupies house 2.
13. The person who keeps the bird loves hiking.

## Puzzle plain:zebra-00006

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

## Puzzle paraphrase:zebra-00149

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, painting
- job: teacher, baker, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Spaniard, German
- drink: juice, water, tea, cocoa, milk

Clues:
1. Cooking is the pilot's hobby.
2. The golf enthusiast lives directly right of the Swede.
3. The Dane is the farmer.
4. The water drinker is not the farmer.
5. The Spaniard is the tea drinker.
6. The painting enthusiast drinks milk.
7. Golf is the teacher's hobby.
8. The German lives in house 5.
9. The hiking enthusiast lives next to the milk drinker.
10. The doctor is not the milk drinker.
11. The second house belongs to the water drinker.
12. The doctor lives somewhere right of the tennis enthusiast.
13. The farmer lives immediately left of the doctor.
14. The juice drinker lives immediately left of the baker.
