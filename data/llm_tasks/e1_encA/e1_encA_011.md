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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_011.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, cat, horse, rabbit, bird
- color: yellow, purple, white, red, blue
- hobby: tennis, chess, cooking, golf, hiking
- nationality: Dane, Norwegian, Brit, Spaniard, Swede

Clues:
1. The Swede enjoys golf.
2. The Dane lives somewhere to the left of the person who keeps the cat.
3. The person in the yellow house lives in the fourth house.
4. The hiking enthusiast does not live in the fourth house.
5. The owner of the rabbit lives somewhere to the right of the person in the purple house.
6. The dog owner lives directly to the left of the owner of the rabbit.
7. The hiking enthusiast lives somewhere to the left of the person in the red house.
8. The Spaniard lives in the house just left of the one where the occupant of the blue house lives.
9. The person who enjoys chess lives in the second house.
10. The Spaniard lives at one end of the row.
11. The hiking enthusiast lives directly to the left of the Brit.
12. The Dane lives next to the occupant of the purple house.
13. The horse owner and the person in the red house live in adjacent houses.
14. The person who enjoys cooking lives directly to the left of the person who keeps the dog.

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

## Puzzle paraphrase:zebra-00162

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, yellow, red, green
- hobby: hiking, cooking, painting, golf, tennis
- pet: horse, dog, bird, cat, rabbit
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The hiker and the juice drinker live in adjacent houses.
2. The tennis enthusiast lives immediately to the right of the green house's occupant.
3. The white house is the last house.
4. The hiker lives in the purple house.
5. The hiker lives immediately to the right of the cooking enthusiast.
6. The rabbit owner lives in the white house.
7. The dog owner and the juice drinker are next-door neighbours.
8. The green house's occupant and the water drinker are neighbours.
9. The occupant of the green house lives next to the milk drinker.
10. The hiker keeps either the bird or the cat.
11. The tennis enthusiast lives immediately to the right of the cat owner.
12. The golfer lives in house 5.
13. The milk drinker lives in a lower-numbered house than the water drinker.
14. The cocoa drinker lives next door to the hiker.
15. Exactly one house separates the green house from the yellow house.

## Puzzle paraphrase:zebra-00180

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, water, milk
- pet: dog, bird, horse, fish, rabbit
- color: yellow, red, green, blue, white
- job: farmer, doctor, lawyer, baker, pilot

Clues:
1. Whoever drinks tea is the pilot.
2. The green house stands somewhere to the right of the doctor's house.
3. The dog's owner drinks water.
4. The horse owner lives right next door to the left of the rabbit owner.
5. The tea drinker is in house 4.
6. The cocoa drinker is not the one who keeps the rabbit.
7. The baker lives next to the white house.
8. The cocoa drinker and the lawyer live two houses apart.
9. The fish owner lives immediately to the left of the red house.
10. The bird is kept in house 2.
11. Exactly one house separates the white house from the yellow house.
12. The yellow house's occupant drinks coffee.
13. The dog owner does not live in house 5.
14. The farmer lives in house 5.

## Puzzle plain:zebra-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, baker, teacher, farmer
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: white, blue, yellow, purple, green
- drink: coffee, water, tea, cocoa, milk

Clues:
1. The Swede lives in a lower-numbered house than the Norwegian.
2. The water drinker is the Norwegian.
3. The person in the green house lives next to the teacher.
4. The German lives next to the Swede.
5. The Swede either works as the doctor or works as the farmer.
6. There is exactly one house between the person who drinks coffee and whoever lives in the yellow house.
7. Whoever lives in the yellow house works as the doctor.
8. The baker lives next to the person in the blue house.
9. The baker and the milk drinker are neighbours.
10. There is exactly one house between the Spaniard and the Swede.
11. The person in the purple house works as the baker.
12. There is exactly one house between the baker and the tea drinker.
13. There is exactly one house between whoever lives in the purple house and the Spaniard.

## Puzzle paraphrase:zebra-00105

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, bird, cat
- job: lawyer, farmer, teacher, pilot, doctor
- drink: juice, tea, milk, water, coffee
- color: green, blue, white, red, purple

Clues:
1. The green house's occupant is the lawyer.
2. The coffee drinker lives in house 4.
3. The red house lies somewhere to the right of the blue house.
4. The cat owner lives immediately to the right of the dog owner.
5. The bird owner and the doctor live next door to each other.
6. The tea drinker lives right after the rabbit owner, immediately to its right.
7. The farmer lives in the red house.
8. The juice drinker lives immediately to the left of the purple house's occupant.
9. One house lies between the coffee drinker and the doctor.
10. The coffee drinker and the pilot live in adjacent houses.
11. The blue house's occupant keeps the horse.
12. The lawyer lives immediately to the right of the water drinker.

## Puzzle hard:zebra_hard-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, hiking, chess, tennis
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, yellow, green, white, purple
- drink: juice, tea, coffee, milk, cocoa

Clues:
1. One of the neighbours of the Swede enjoys painting.
2. If the person who enjoys chess does not drink coffee, then that person drinks tea.
3. The person in the white house lives somewhere between the occupant of the purple house and the Spaniard.
4. The left-hand neighbour of the hiking enthusiast lives in the purple house.
5. The Dane lives somewhere between the person who drinks juice and whoever lives in the white house.
6. One of the neighbours of the occupant of the green house drinks milk.
7. None of the neighbours of the occupant of the yellow house drinks milk.
8. None of the neighbours of the juice drinker drinks tea.
9. The Swede is not the same person as the occupant of the white house.
10. The Brit and the tennis enthusiast are one and the same person.
11. The right-hand neighbour of whoever lives in the yellow house enjoys tennis.
12. One of the neighbours of the cocoa drinker is the Swede.
13. The person in the yellow house lives somewhere between the milk drinker and whoever lives in the purple house.

## Puzzle hard:zebra_hard-00069

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Swede, Spaniard, Brit, German
- pet: horse, bird, rabbit, fish, cat
- hobby: golf, hiking, tennis, cooking, chess
- drink: milk, tea, coffee, cocoa, water

Clues:
1. The chess enthusiast lives somewhere between the person who enjoys cooking and the Spaniard.
2. The horse owner lives somewhere between the cooking enthusiast and the Swede.
3. If the Swede does not keep the bird, then that person keeps the fish.
4. The left-hand neighbour of the person who drinks milk drinks tea.
5. One of the neighbours of the person who enjoys tennis is the Norwegian.
6. The chess enthusiast lives two doors away from the milk drinker.
7. The person who enjoys golf and the Swede are one and the same person.
8. The left-hand neighbour of the person who enjoys cooking drinks water.
9. The left-hand neighbour of the cooking enthusiast is the Norwegian.
10. The rabbit owner has only one neighbour.
11. If the Brit does not drink milk, then that person drinks water.
12. The hiking enthusiast lives further to the right than the person who drinks coffee.
13. If the tea drinker does not keep the bird, then that person keeps the rabbit.
14. The person who enjoys hiking is not the same person as the person who keeps the rabbit.

## Puzzle plain:zebra-00038

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, farmer, baker, doctor
- nationality: Swede, Brit, Dane, German, Norwegian
- color: green, blue, purple, yellow, white
- drink: cocoa, tea, milk, juice, coffee

Clues:
1. The Norwegian lives in house 1.
2. The occupant of the purple house is the Dane.
3. The lawyer and the tea drinker live in adjacent houses.
4. Whoever lives in the purple house drinks milk.
5. The farmer lives in the first house.
6. The German lives next to the Swede.
7. The doctor drinks milk.
8. The occupant of the white house lives immediately to the right of the baker.
9. The coffee drinker lives in a lower-numbered house than whoever lives in the white house.
10. The tea drinker lives in house 2.
11. The cocoa drinker either is the Dane or is the German.
12. Whoever lives in the blue house drinks cocoa.
13. Whoever lives in the yellow house lives in the leftmost house.

## Puzzle hard:zebra_hard-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Dane, Swede, Brit
- color: red, white, blue, green, purple
- drink: coffee, water, juice, cocoa, tea
- job: baker, pilot, doctor, farmer, lawyer

Clues:
1. The occupant of the green house and the lawyer are one and the same person.
2. The person who drinks coffee lives somewhere between the German and the juice drinker.
3. The left-hand neighbour of the pilot is the Norwegian.
4. The person in the purple house lives in the third house from the right.
5. The occupant of the green house lives somewhere between the person who drinks cocoa and the German.
6. The person in the blue house and the farmer are one and the same person.
7. Whoever lives in the blue house lives further to the right than the Norwegian.
8. The pilot lives somewhere between the doctor and the farmer.
9. The cocoa drinker and the Swede are one and the same person.
10. The right-hand neighbour of the person who drinks cocoa drinks tea.
11. The right-hand neighbour of the person who drinks juice is the Dane.
12. Exactly one house separates the person in the red house from the Swede.
