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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_017.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, red, blue, purple, green
- pet: rabbit, dog, horse, bird, fish
- hobby: painting, cooking, golf, chess, hiking
- job: baker, doctor, farmer, pilot, teacher

Clues:
1. The right-hand neighbour of the farmer lives in the blue house.
2. The farmer lives two doors away from the person who enjoys golf.
3. Exactly 3 houses lie to the left of the home of the person who enjoys cooking.
4. The person who keeps the bird and the person who enjoys hiking are one and the same person.
5. The occupant of the green house lives two doors away from the owner of the horse.
6. One of the neighbours of the baker enjoys chess.
7. One of the neighbours of the hiking enthusiast works as the doctor.
8. The farmer does not live in the third house from the right.
9. Exactly 2 houses lie to the left of the home of the person in the purple house.
10. The owner of the dog does not live in the rightmost house.
11. The left-hand neighbour of the person who enjoys painting works as the pilot.
12. The occupant of the yellow house does not live to the right of the occupant of the green house.
13. If the owner of the dog does not live in the green house, then that person lives in the red house.
14. The right-hand neighbour of the person who keeps the fish lives in the purple house.

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

## Puzzle plain:zebra-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, juice
- job: farmer, teacher, pilot, lawyer, doctor
- color: white, green, yellow, red, purple
- pet: dog, cat, horse, rabbit, fish

Clues:
1. The person who drinks cocoa either lives in the green house or lives in the purple house.
2. The tea drinker either lives in the white house or lives in the yellow house.
3. The person who drinks water lives immediately to the right of the farmer.
4. The pilot and the tea drinker live in adjacent houses.
5. The occupant of the green house and the teacher live in adjacent houses.
6. The person who keeps the horse either works as the farmer or works as the teacher.
7. The owner of the fish works as the doctor.
8. The owner of the fish lives in the yellow house.
9. The person who drinks juice and the person in the white house are neighbours.
10. The person who keeps the rabbit and the tea drinker live two houses apart.
11. The person in the purple house lives somewhere to the left of the owner of the dog.
12. Whoever lives in the white house lives directly to the left of the farmer.
13. The person who keeps the horse lives immediately to the right of the doctor.

## Puzzle paraphrase:zebra-00194

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, teacher, lawyer
- pet: horse, dog, cat, bird, rabbit
- nationality: Dane, German, Norwegian, Brit, Swede
- color: green, white, red, blue, yellow

Clues:
1. The farmer lives in one of the two end houses.
2. The lawyer is the horse keeper.
3. The yellow house stands immediately to the left of the cat owner's house.
4. The bird keeper and the lawyer live next door to each other.
5. The baker and the Swede have exactly one house between them.
6. The Swede lives in either the blue house or the green house.
7. The horse owner lives in either the blue house or the white house.
8. The occupant of the red house is either the lawyer or the teacher.
9. The baker lives next door to the Brit.
10. The German lives in the leftmost house.
11. The Norwegian keeps the rabbit.
12. The Dane lives next door to the teacher.
13. The red house's occupant keeps the dog.
14. The green house and the red house are not next to each other.

## Puzzle plain:zebra-00001

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

## Puzzle hard:zebra_hard-00081

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, tea, juice, water
- nationality: Swede, Dane, Brit, Norwegian, Spaniard
- hobby: painting, tennis, hiking, cooking, chess
- job: teacher, lawyer, doctor, pilot, farmer

Clues:
1. The person who drinks coffee lives further to the right than the Norwegian.
2. The tea drinker does not live to the right of the juice drinker.
3. The left-hand neighbour of the person who drinks water enjoys painting.
4. Neither the person who enjoys chess nor the doctor is the Dane.
5. Exactly one house separates the farmer from the lawyer.
6. The Spaniard and the person who enjoys tennis are one and the same person.
7. The person who enjoys chess lives in the third house from the right.
8. The farmer and the Norwegian are one and the same person.
9. The person who enjoys cooking lives in the fourth house from the right.
10. Exactly one house separates the person who enjoys chess from the Dane.
11. One of the neighbours of the farmer drinks juice.
12. The Swede lives two doors away from the teacher.
13. Exactly one house separates the chess enthusiast from the person who drinks milk.
14. If the Swede does not drink coffee, then that person drinks milk.

## Puzzle hard:zebra_hard-00007

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, dog, fish, horse
- nationality: Norwegian, Spaniard, Brit, Swede, Dane
- hobby: golf, tennis, cooking, painting, hiking
- drink: milk, juice, coffee, tea, cocoa

Clues:
1. One of the neighbours of the person who enjoys hiking is the Swede.
2. The left-hand neighbour of the Dane keeps the dog.
3. The right-hand neighbour of the owner of the cat drinks coffee.
4. At least one house separates the dog owner from the person who enjoys cooking.
5. One of the neighbours of the coffee drinker keeps the dog.
6. The fish owner and the tennis enthusiast are one and the same person.
7. The cocoa drinker and the person who enjoys painting are one and the same person.
8. Neither the person who keeps the cat nor the tennis enthusiast drinks milk.
9. The tea drinker lives further to the right than the person who keeps the cat.
10. At least one house separates the Spaniard from the Norwegian.
11. One of the neighbours of the Spaniard keeps the dog.
12. The person who drinks milk and the Swede are one and the same person.
13. The cooking enthusiast and the person who drinks tea are one and the same person.
14. One of the neighbours of the horse owner is the Norwegian.

## Puzzle hard:zebra_hard-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, red, purple, yellow
- pet: fish, dog, bird, horse, rabbit
- nationality: Norwegian, Dane, German, Brit, Swede
- job: teacher, farmer, baker, doctor, lawyer

Clues:
1. The right-hand neighbour of the person who keeps the dog is the German.
2. Exactly 1 house lies to the left of the home of the occupant of the red house.
3. Neither the person who keeps the rabbit nor the occupant of the white house works as the teacher.
4. One of the neighbours of the occupant of the yellow house keeps the bird.
5. The person who keeps the bird and whoever lives in the white house are one and the same person.
6. Exactly one house separates the doctor from the person in the white house.
7. If the Brit is not the doctor, then that person works as the lawyer.
8. The Swede lives further to the right than the fish owner.
9. One of the neighbours of the farmer keeps the fish.
10. The Dane lives somewhere between the German and whoever lives in the green house.
11. The baker and the person who keeps the rabbit are one and the same person.
12. The German and whoever lives in the red house are one and the same person.
13. One of the neighbours of the German keeps the rabbit.

## Puzzle paraphrase:zebra-00122

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, purple, red
- drink: tea, cocoa, juice, milk, coffee
- hobby: cooking, tennis, hiking, golf, painting
- pet: rabbit, fish, bird, cat, horse

Clues:
1. The white house is somewhere to the left of the blue house.
2. The green house's occupant drinks tea.
3. The hiker lives immediately to the left of the painter.
4. The cat owner lives directly right of the cocoa drinker.
5. One house separates the cocoa drinker from the cooking enthusiast.
6. The juice drinker lives in one of the end houses.
7. The fish keeper is a neighbour of the purple house's occupant.
8. The horse owner and the rabbit owner live next door to each other.
9. The milk drinker lives right next to the juice drinker, on its right.
10. The cooking enthusiast drinks tea.
11. The red house's occupant keeps either the fish or the horse.
12. The golfer is the one who keeps the fish.
13. There is one house between the blue house and the white house.

## Puzzle hard:zebra_hard-00025

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, painting, hiking, cooking
- color: white, yellow, purple, red, green
- nationality: Spaniard, Brit, German, Swede, Dane
- drink: water, tea, juice, cocoa, milk

Clues:
1. If the Swede does not enjoy hiking, then that person enjoys tennis.
2. One of the neighbours of the person who drinks milk is the Spaniard.
3. If the person who enjoys cooking is not the Dane, then that person is the German.
4. The person who enjoys tennis lives somewhere between the Brit and the person in the yellow house.
5. The Spaniard lives somewhere between the chess enthusiast and the person who enjoys cooking.
6. The right-hand neighbour of the person who enjoys cooking lives in the purple house.
7. The cocoa drinker and whoever lives in the green house are one and the same person.
8. Exactly 3 houses lie to the left of the home of whoever lives in the green house.
9. Neither the chess enthusiast nor the tennis enthusiast lives in the yellow house.
10. The person who drinks water lives somewhere between the cooking enthusiast and the person who enjoys hiking.
11. The cooking enthusiast lives further to the right than the Spaniard.
12. The person who drinks cocoa lives somewhere between the juice drinker and the person who drinks milk.
13. Neither the Dane nor the Spaniard lives in the red house.
14. The cooking enthusiast is not the same person as the Dane.
