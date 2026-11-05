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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_008.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00041

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, fish, dog
- color: purple, white, red, blue, green
- hobby: chess, painting, tennis, golf, hiking
- drink: water, tea, coffee, cocoa, juice

Clues:
1. The chess enthusiast lives in the first house.
2. The owner of the cat lives in a lower-numbered house than the person who enjoys hiking.
3. The occupant of the red house lives immediately to the right of the golf enthusiast.
4. The bird owner and the owner of the horse live two houses apart.
5. The person who drinks coffee lives in the white house.
6. The water drinker lives in the house just left of the one where the person in the green house lives.
7. The occupant of the blue house drinks water.
8. The cocoa drinker lives immediately to the right of the juice drinker.
9. The person who enjoys hiking lives in the house just left of the one where the owner of the horse lives.
10. Whoever lives in the white house lives somewhere to the left of the hiking enthusiast.
11. The owner of the dog lives in house 5.
12. The person who enjoys tennis lives in the fourth house.

## Puzzle paraphrase:zebra-00106

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, painting, golf, tennis, chess
- color: yellow, red, green, blue, purple
- job: pilot, doctor, baker, lawyer, teacher
- nationality: Dane, Norwegian, German, Spaniard, Swede

Clues:
1. The Spaniard lives in house 2.
2. The cooking enthusiast is either the lawyer or the pilot.
3. The Swede lives directly to the right of the green house's occupant.
4. One house separates the golf enthusiast from the pilot.
5. The doctor lives immediately to the right of the Norwegian.
6. The lawyer lives immediately to the left of the tennis enthusiast.
7. The teacher lives in house 2.
8. The Dane lives immediately to the left of the red house's occupant.
9. The golf enthusiast lives in the purple house.
10. The chess enthusiast lives in the blue house.
11. The Norwegian lives somewhere to the left of the yellow house's occupant.
12. The tennis enthusiast lives in the fourth house.

## Puzzle paraphrase:zebra-00143

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, chess, tennis, painting
- color: yellow, blue, green, red, white
- job: doctor, baker, pilot, farmer, lawyer
- drink: tea, coffee, water, juice, milk

Clues:
1. The juice drinker and the tennis enthusiast live two houses apart.
2. The chess enthusiast lives next door to the hiking enthusiast.
3. The red house is immediately left of the blue house.
4. The coffee drinker lives directly right of the pilot.
5. The juice drinker lives in the middle house, number 3.
6. The baker lives in house 2.
7. The chess enthusiast lives directly right of the pilot.
8. Two houses separate the chess enthusiast from the water drinker.
9. The green house's occupant lives next to the tea drinker.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot lives in either the green house or the white house.
12. The milk drinker enjoys hiking.
13. The painting enthusiast lives immediately left of the farmer.

## Puzzle paraphrase:zebra-00197

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, horse, dog, cat
- drink: tea, cocoa, juice, milk, coffee
- nationality: Swede, German, Norwegian, Brit, Spaniard
- color: blue, red, purple, yellow, green

Clues:
1. The milk drinker lives in the house immediately left of the bird keeper's.
2. The horse keeper and the milk drinker have exactly one house between them.
3. The cocoa drinker is either the German or the Spaniard.
4. The German is the horse owner.
5. The Brit lives next door to the yellow house's occupant.
6. The cat owner lives immediately to the right of the fish owner.
7. The coffee drinker lives next door to the red house's occupant.
8. The yellow house's occupant drinks juice.
9. The tea drinker lives in house 3.
10. The fish owner lives in the purple house.
11. The tea drinker is either the Brit or the German.
12. The cat owner lives in the green house.
13. The fish owner and the Swede live two houses apart.

## Puzzle plain:zebra-00024

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, yellow, red, blue
- job: doctor, lawyer, baker, farmer, teacher
- nationality: German, Norwegian, Brit, Dane, Spaniard
- pet: rabbit, dog, cat, horse, fish

Clues:
1. The person in the blue house works as the lawyer.
2. The occupant of the purple house works as the teacher.
3. There is exactly one house between the person in the blue house and the occupant of the red house.
4. The doctor and the Norwegian live two houses apart.
5. The Dane either keeps the dog or keeps the horse.
6. The Brit keeps the rabbit.
7. The horse owner and the occupant of the purple house live in adjacent houses.
8. The Dane lives in one of the two end houses.
9. The Spaniard lives in the third house.
10. The Brit lives next to the occupant of the yellow house.
11. The owner of the cat lives next to the person who keeps the rabbit.
12. The person who keeps the horse lives somewhere to the right of the owner of the cat.
13. The person in the blue house lives in the leftmost house.
14. The baker lives somewhere to the right of the German.
15. The Norwegian lives somewhere to the right of the fish owner.
16. The German lives in a lower-numbered house than the Brit.

## Puzzle paraphrase:zebra-00124

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- pet: rabbit, horse, fish, bird, cat
- drink: juice, cocoa, milk, coffee, tea
- job: farmer, pilot, lawyer, teacher, doctor

Clues:
1. The purple house's occupant and the teacher are next-door neighbours.
2. The cat owner lives directly to the right of the fish owner.
3. The bird owner lives somewhere to the right of the farmer.
4. The pilot keeps either the cat or the fish.
5. The rabbit owner drinks either coffee or tea.
6. The juice drinker lives next door to the purple house.
7. The pilot and the yellow house's occupant are neighbours.
8. The farmer lives directly to the right of the cat owner.
9. The coffee drinker lives in house 1.
10. The farmer and the rabbit owner live in adjacent houses.
11. One house separates the blue house from the pilot.
12. The doctor lives somewhere to the right of the cocoa drinker.
13. The bird owner and the purple house's occupant are not neighbours.
14. The red house's occupant is the pilot.

## Puzzle plain:zebra-00068

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, horse, fish, cat, rabbit
- drink: milk, tea, juice, water, cocoa
- job: teacher, baker, farmer, pilot, lawyer
- nationality: Norwegian, Dane, German, Brit, Spaniard

Clues:
1. The bird owner lives in the first house.
2. The baker and the German live two houses apart.
3. The owner of the fish drinks water.
4. The person who keeps the bird either is the Dane or is the Norwegian.
5. The lawyer drinks tea.
6. The Spaniard lives somewhere to the right of the farmer.
7. The cat owner does not live next to the juice drinker.
8. The Norwegian is not the pilot.
9. The baker lives directly to the left of the owner of the horse.
10. The pilot lives directly to the left of the person who drinks milk.
11. There is exactly one house between the horse owner and the teacher.
12. The milk drinker lives in the house just left of the one where the person who drinks cocoa lives.
13. The person who drinks water lives in one of the two end houses.
14. The Norwegian lives next to the person who keeps the rabbit.

## Puzzle hard:zebra_hard-00026

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, blue, white, purple, yellow
- job: lawyer, teacher, doctor, farmer, pilot
- drink: coffee, tea, cocoa, milk, water
- hobby: cooking, chess, hiking, tennis, golf

Clues:
1. If the occupant of the yellow house does not enjoy golf, then that person enjoys hiking.
2. Whoever lives in the green house lives somewhere between the coffee drinker and the golf enthusiast.
3. The milk drinker lives somewhere between the coffee drinker and the lawyer.
4. The left-hand neighbour of the lawyer drinks water.
5. One of the neighbours of the pilot lives in the blue house.
6. Whoever lives in the blue house and the cocoa drinker are one and the same person.
7. The pilot and the occupant of the purple house are one and the same person.
8. The chess enthusiast and whoever lives in the green house are one and the same person.
9. The person in the blue house and the golf enthusiast are one and the same person.
10. None of the neighbours of the person who drinks cocoa enjoys cooking.
11. The milk drinker lives somewhere between the farmer and the lawyer.
12. The teacher and whoever lives in the white house are one and the same person.
13. One of the neighbours of the occupant of the purple house lives in the yellow house.

## Puzzle paraphrase:zebra-00142

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, golf, tennis, painting
- job: farmer, pilot, lawyer, teacher, baker
- pet: bird, rabbit, cat, horse, fish
- color: yellow, purple, blue, green, red

Clues:
1. The golf enthusiast lives immediately left of the blue house's occupant.
2. One house lies between the pilot and the rabbit owner.
3. The painting enthusiast lives in the fourth house.
4. House 2 belongs to the cooking enthusiast.
5. The bird owner lives directly left of the purple house's occupant.
6. The red house's occupant is the teacher.
7. The baker lives in the second house.
8. The blue house's occupant lives next door to the tennis enthusiast.
9. The farmer does not live next to the rabbit owner.
10. The fish keeper and the rabbit owner are neighbours.
11. Exactly one house separates the blue house from the green house.
12. The tennis enthusiast is either the farmer or the lawyer.
13. The blue house's occupant lives next to the fish owner.
14. The bird keeper lives next door to the horse owner.
15. The teacher lives in the middle house.

## Puzzle paraphrase:zebra-00119

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, farmer
- color: green, white, blue, red, yellow
- hobby: cooking, tennis, chess, hiking, painting
- pet: horse, dog, cat, bird, rabbit

Clues:
1. The white house's occupant lives somewhere to the left of the bird owner.
2. The yellow house's occupant lives in house 5.
3. The tennis enthusiast is the lawyer.
4. The rabbit keeper lives in the leftmost house.
5. The cooking enthusiast and the lawyer live two houses apart.
6. The blue house's occupant enjoys chess.
7. Exactly one house lies between the horse owner and the red house's occupant.
8. The blue house's occupant is not the doctor.
9. The cooking enthusiast and the white house's occupant live two houses apart.
10. The horse owner enjoys hiking.
11. The baker lives in house 2.
12. The pilot's hobby is either painting or tennis.
13. The chess enthusiast and the white house's occupant are not neighbours.
14. The dog owner is the pilot.
