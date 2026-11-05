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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_024.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00165

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, doctor
- drink: tea, juice, milk, cocoa, coffee
- nationality: Norwegian, German, Swede, Brit, Spaniard
- hobby: chess, hiking, cooking, golf, tennis

Clues:
1. The Norwegian lives in house 1.
2. The tea drinker lives immediately to the left of the lawyer.
3. The German lives immediately to the left of the farmer.
4. The milk drinker does not enjoy chess.
5. The golfer is the lawyer.
6. The farmer lives immediately to the left of the coffee drinker.
7. One house separates the Brit from the pilot.
8. The cocoa drinker lives immediately to the left of the cooking enthusiast.
9. The farmer and the Spaniard live in adjacent houses.
10. The doctor drinks either cocoa or juice.
11. The milk drinker lives immediately to the left of the tennis enthusiast.
12. The cooking enthusiast and the milk drinker live two houses apart.
13. The cocoa drinker lives next door to the doctor.

## Puzzle paraphrase:zebra-00147

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, chess
- nationality: German, Swede, Norwegian, Spaniard, Dane
- pet: horse, fish, dog, bird, cat
- color: purple, green, yellow, blue, white

Clues:
1. The fish owner lives in the yellow house.
2. Chess is the hobby of the bird owner.
3. The Dane lives immediately left of the horse owner.
4. The Norwegian lives somewhere to the right of the green house.
5. The cooking enthusiast lives somewhere right of the bird owner.
6. The cat owner is not the Norwegian.
7. The dog owner lives immediately left of the Swede.
8. The horse owner and the white house's occupant are neighbours.
9. The Norwegian and the yellow house's occupant are next-door neighbours.
10. The hiking enthusiast lives next to the purple house.
11. The German lives directly left of the fish owner.
12. Cooking is the Spaniard's hobby.
13. The tennis enthusiast lives in the third house.

## Puzzle hard:zebra_hard-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, bird, cat
- color: green, white, red, purple, blue
- job: pilot, baker, farmer, teacher, lawyer
- hobby: painting, cooking, hiking, tennis, chess

Clues:
1. Exactly 0 houses lie to the left of the home of the hiking enthusiast.
2. The pilot and the person in the white house are one and the same person.
3. One of the neighbours of the hiking enthusiast keeps the bird.
4. If the occupant of the green house is not the farmer, then that person works as the pilot.
5. The person who enjoys chess lives further to the right than whoever lives in the green house.
6. The person who keeps the cat lives somewhere between the baker and the fish owner.
7. None of the neighbours of the occupant of the white house lives in the red house.
8. The person who keeps the fish and the teacher are one and the same person.
9. The person who enjoys painting and the person in the white house are one and the same person.
10. One of the neighbours of the teacher keeps the dog.
11. The bird owner and the person in the green house are one and the same person.
12. If the occupant of the blue house is not the baker, then that person works as the farmer.
13. One of the neighbours of the cooking enthusiast keeps the dog.
14. The cooking enthusiast does not live in the second house from the right.

## Puzzle plain:zebra-00028

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Spaniard, German, Dane
- hobby: cooking, golf, painting, chess, hiking
- color: yellow, red, blue, purple, white
- drink: juice, water, milk, coffee, tea

Clues:
1. The person who drinks coffee and the German are not neighbours.
2. The Norwegian either drinks milk or drinks water.
3. The Norwegian lives in a lower-numbered house than the person who drinks milk.
4. There is exactly one house between the German and the juice drinker.
5. The Brit and the cooking enthusiast live two houses apart.
6. The person who enjoys chess and whoever lives in the yellow house live in adjacent houses.
7. The person who enjoys chess lives in the red house.
8. The person who enjoys hiking lives in the house just left of the one where the golf enthusiast lives.
9. The Spaniard enjoys painting.
10. The occupant of the blue house does not live next to the milk drinker.
11. The tea drinker is the German.
12. Whoever lives in the blue house lives directly to the left of the person in the red house.
13. The Brit lives next to the Norwegian.
14. The Norwegian either lives in the white house or lives in the yellow house.

## Puzzle paraphrase:zebra-00109

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, Spaniard, German
- job: doctor, baker, lawyer, farmer, pilot
- hobby: golf, hiking, painting, cooking, chess
- pet: fish, dog, cat, rabbit, horse

Clues:
1. The chess enthusiast lives in house 4.
2. The doctor's hobby is cooking.
3. The painting enthusiast lives immediately to the left of the hiker.
4. The Brit and the Spaniard live next door to each other.
5. The rabbit owner is the farmer.
6. The pilot lives immediately to the right of the baker.
7. One house lies between the farmer and the Norwegian.
8. The baker lives somewhere to the left of the horse owner.
9. The hiker keeps the dog.
10. The fish owner lives immediately to the left of the baker.
11. The lawyer lives immediately to the left of the German.
12. The fish owner is not the Spaniard.

## Puzzle plain:zebra-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, coffee
- job: teacher, doctor, pilot, baker, farmer
- nationality: Swede, Dane, Norwegian, German, Spaniard
- hobby: tennis, golf, cooking, painting, chess

Clues:
1. The teacher and the person who enjoys chess are different people.
2. The baker lives immediately to the right of the person who enjoys cooking.
3. The milk drinker lives immediately to the right of the water drinker.
4. The German and the Spaniard live two houses apart.
5. The doctor either drinks coffee or drinks milk.
6. The Swede lives in house 5.
7. The Dane and the person who drinks milk live in adjacent houses.
8. The person who enjoys golf lives somewhere to the left of the juice drinker.
9. The person who enjoys painting lives in one of the two end houses.
10. The German lives immediately to the right of the chess enthusiast.
11. The Dane and the doctor live two houses apart.
12. The pilot lives in the middle house.
13. The person who drinks juice is the Spaniard.
14. The baker lives in the fourth house.

## Puzzle hard:zebra_hard-00062

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, German, Brit, Norwegian, Dane
- color: white, blue, purple, red, yellow
- drink: juice, water, coffee, cocoa, tea
- hobby: cooking, golf, painting, hiking, tennis

Clues:
1. The coffee drinker lives somewhere between the cooking enthusiast and the person who enjoys tennis.
2. Whoever lives in the blue house lives somewhere between the German and the Spaniard.
3. Neither the Dane nor the person who enjoys golf lives in the red house.
4. Exactly one house separates the person who enjoys painting from the occupant of the yellow house.
5. If the person who drinks juice does not enjoy painting, then that person enjoys tennis.
6. The left-hand neighbour of the Norwegian enjoys cooking.
7. The person who enjoys cooking lives further to the right than the German.
8. The occupant of the red house and the tea drinker are one and the same person.
9. The juice drinker lives somewhere between the cocoa drinker and whoever lives in the white house.
10. The occupant of the white house lives somewhere between the person in the blue house and the German.
11. The occupant of the blue house does not live to the right of the person in the red house.
12. The right-hand neighbour of the Dane drinks cocoa.

## Puzzle paraphrase:zebra-00115

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Dane, Swede, Norwegian
- drink: coffee, tea, cocoa, water, milk
- color: blue, yellow, purple, red, green
- job: doctor, teacher, pilot, lawyer, farmer

Clues:
1. The Norwegian lives directly to the left of the milk drinker.
2. The red house is immediately to the left of the blue house.
3. The farmer drinks coffee.
4. The Brit lives in either the green house or the red house.
5. The Dane lives in the fifth house.
6. Exactly one house lies between the cocoa drinker and the purple house's occupant.
7. The Brit and the Norwegian live two houses apart.
8. The Spaniard lives immediately to the right of the green house.
9. The farmer lives next door to the teacher.
10. The yellow house is immediately to the right of the Spaniard's.
11. The doctor drinks water.
12. The farmer lives in the yellow house.
13. The farmer and the pilot live two houses apart.

## Puzzle hard:zebra_hard-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, German
- color: yellow, white, green, blue, purple
- hobby: golf, chess, tennis, hiking, cooking
- drink: water, cocoa, tea, juice, milk

Clues:
1. The left-hand neighbour of the golf enthusiast drinks tea.
2. Exactly 2 houses lie to the left of the home of the Brit.
3. The occupant of the blue house and the hiking enthusiast are one and the same person.
4. At least one house separates the person who drinks juice from the German.
5. The person who enjoys chess and the person who drinks tea are one and the same person.
6. Exactly one house separates whoever lives in the purple house from the person who enjoys tennis.
7. The Spaniard lives somewhere between whoever lives in the green house and the person in the yellow house.
8. Exactly one house separates the Swede from the person in the yellow house.
9. The right-hand neighbour of the person in the purple house drinks cocoa.
10. One of the neighbours of the occupant of the white house enjoys cooking.
11. The person who drinks water lives somewhere between whoever lives in the blue house and the person who enjoys golf.
12. The juice drinker and the Norwegian are one and the same person.

## Puzzle paraphrase:zebra-00133

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Swede, German, Dane
- drink: tea, water, juice, milk, cocoa
- pet: horse, rabbit, dog, cat, bird
- job: doctor, lawyer, farmer, teacher, baker

Clues:
1. The Swede keeps the dog.
2. The baker lives directly to the left of the horse owner.
3. The Swede is the milk drinker.
4. The bird owner lives right next to the Swede.
5. The bird owner is the lawyer.
6. The doctor is either the Dane or the Swede.
7. The farmer lives immediately to the left of the dog owner.
8. The lawyer lives somewhere to the left of the cocoa drinker.
9. The German lives immediately to the left of the juice drinker.
10. One house separates the Norwegian from the Swede.
11. The doctor lives in the fifth house.
12. The farmer drinks water.
13. The cat's owner is the baker.
