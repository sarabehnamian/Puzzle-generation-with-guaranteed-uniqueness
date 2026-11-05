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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_029.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00048

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Dane, German, Brit, Swede
- hobby: painting, chess, golf, hiking, tennis
- color: blue, red, white, purple, yellow
- job: farmer, pilot, doctor, baker, lawyer

Clues:
1. The Spaniard does not live in the fifth house.
2. The doctor lives in the second house.
3. The pilot lives somewhere to the right of the hiking enthusiast.
4. The person in the red house lives somewhere to the right of the person who enjoys tennis.
5. The German enjoys hiking.
6. The chess enthusiast lives in the white house.
7. The Swede works as the lawyer.
8. There is exactly one house between the person who enjoys chess and the German.
9. The farmer lives somewhere to the left of the occupant of the purple house.
10. The baker does not live in house 1.
11. The golf enthusiast is the Swede.
12. The Dane and the occupant of the yellow house live two houses apart.
13. The lawyer does not live in house 5.
14. The chess enthusiast lives in house 4.
15. The baker either lives in the blue house or lives in the purple house.
16. The person who enjoys chess is the Dane.

## Puzzle hard:zebra_hard-00050

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, hiking
- job: pilot, lawyer, farmer, doctor, teacher
- pet: bird, rabbit, fish, horse, dog
- drink: tea, cocoa, water, milk, coffee

Clues:
1. The left-hand neighbour of the horse owner works as the doctor.
2. If the tea drinker is not the doctor, then that person works as the lawyer.
3. The person who enjoys cooking lives in the rightmost house.
4. The lawyer lives somewhere between the owner of the bird and the person who keeps the rabbit.
5. The right-hand neighbour of the milk drinker enjoys hiking.
6. The person who enjoys cooking and the pilot are one and the same person.
7. Neither the farmer nor the person who drinks tea enjoys tennis.
8. The owner of the bird and the person who drinks tea are one and the same person.
9. The left-hand neighbour of the lawyer enjoys golf.
10. One of the neighbours of the owner of the bird keeps the fish.
11. The person who keeps the bird lives two doors away from the lawyer.
12. Exactly 0 houses lie to the left of the home of the person who drinks coffee.
13. The person who drinks cocoa and the teacher are one and the same person.

## Puzzle hard:zebra_hard-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, dog, horse, bird
- nationality: Brit, Norwegian, Swede, German, Spaniard
- hobby: painting, tennis, cooking, hiking, chess
- job: farmer, teacher, lawyer, pilot, doctor

Clues:
1. The right-hand neighbour of the Norwegian works as the lawyer.
2. Exactly 0 houses lie to the left of the home of the doctor.
3. Exactly 2 houses lie to the left of the home of the German.
4. The teacher has only one neighbour.
5. Exactly one house separates the owner of the dog from the Swede.
6. The cooking enthusiast and the Norwegian are one and the same person.
7. If the pilot does not enjoy hiking, then that person enjoys painting.
8. Exactly one house separates the doctor from the person who keeps the horse.
9. If the person who keeps the bird is not the Brit, then that person is the German.
10. The person who enjoys cooking lives in the fourth house from the right.
11. The painting enthusiast lives two doors away from the Spaniard.
12. The person who keeps the cat lives two doors away from the German.
13. The bird owner lives further to the right than the chess enthusiast.

## Puzzle plain:zebra-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, hiking, painting, chess
- pet: fish, rabbit, dog, cat, horse
- drink: milk, juice, coffee, tea, water
- color: blue, yellow, purple, green, white

Clues:
1. The owner of the horse either drinks tea or drinks water.
2. The occupant of the purple house keeps the fish.
3. Whoever lives in the green house lives next to the rabbit owner.
4. The tea drinker and the person who enjoys tennis live two houses apart.
5. The owner of the cat lives at one end of the row.
6. There is exactly one house between whoever lives in the blue house and the juice drinker.
7. The occupant of the blue house enjoys hiking.
8. The owner of the dog lives in the fourth house.
9. The person in the white house lives in a lower-numbered house than the person who enjoys painting.
10. The milk drinker lives in a lower-numbered house than whoever lives in the white house.
11. The water drinker lives in house 3.
12. The chess enthusiast and the person who drinks water live in adjacent houses.
13. The person in the yellow house lives in the house just left of the one where the person who enjoys tennis lives.

## Puzzle paraphrase:zebra-00177

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- job: baker, farmer, pilot, doctor, lawyer
- color: purple, yellow, green, red, white
- pet: horse, cat, fish, bird, dog

Clues:
1. The horse owner drinks tea.
2. The red house is the fifth house.
3. The juice drinker lives immediately to the left of the fish owner.
4. The coffee drinker's house has a lower number than the white house.
5. One house lies between the juice drinker and the yellow house.
6. The yellow house is at one end of the row.
7. The bird owner and the fish owner are two houses apart.
8. The baker lives in the second house.
9. The purple house's occupant drinks water.
10. One house separates the dog owner from the tea drinker.
11. The cocoa drinker is the lawyer.
12. The pilot lives immediately to the right of the white house.
13. The doctor lives next door to the white house.

## Puzzle paraphrase:zebra-00156

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, water, juice, coffee
- color: purple, red, yellow, green, blue
- hobby: golf, hiking, cooking, chess, tennis
- pet: fish, bird, dog, horse, rabbit

Clues:
1. The green house is directly to the left of the golfer's house.
2. The juice drinker lives next door to the yellow house's occupant.
3. The fish keeper lives immediately to the left of the juice drinker.
4. The yellow house's occupant lives immediately to the right of the bird keeper.
5. The rabbit keeper's hobby is cooking.
6. Exactly one house lies between the chess player and the coffee drinker.
7. The purple house is somewhere to the right of the hiker.
8. The cocoa drinker lives immediately to the left of the tea drinker.
9. One house separates the hiker from the red house's occupant.
10. The dog's owner lives in the fourth house.
11. The rabbit's owner lives immediately to the right of the yellow house's occupant.
12. The yellow house's occupant drinks either juice or tea.

## Puzzle plain:zebra-00054

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, water, tea, cocoa
- nationality: Spaniard, Dane, Norwegian, Swede, German
- pet: fish, cat, dog, horse, bird
- hobby: cooking, hiking, chess, painting, golf

Clues:
1. The Swede lives directly to the left of the water drinker.
2. The cat owner lives in the middle house.
3. The horse owner lives in the house just left of the one where the cocoa drinker lives.
4. The cocoa drinker lives directly to the left of the Norwegian.
5. The person who enjoys golf drinks tea.
6. There is exactly one house between the person who drinks coffee and the person who enjoys hiking.
7. The cocoa drinker keeps the bird.
8. The person who enjoys chess keeps the fish.
9. The hiking enthusiast lives in the house just left of the one where the person who drinks milk lives.
10. The fish owner and the Spaniard live two houses apart.
11. The owner of the fish lives directly to the left of the painting enthusiast.
12. The German lives in the last house.

## Puzzle paraphrase:zebra-00120

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, yellow, purple, red
- nationality: Brit, Dane, German, Spaniard, Swede
- job: baker, pilot, doctor, farmer, teacher
- drink: juice, tea, water, coffee, cocoa

Clues:
1. The green house and the Spaniard's home are next door to each other.
2. The Dane is a pilot by trade.
3. The white house stands immediately to the left of the Brit's house.
4. The German's drink is tea.
5. The white house is at one of the two ends of the row.
6. The coffee drinker is the farmer.
7. The teacher lives right next door to the German, on his right.
8. The water drinker's house is immediately to the left of the juice drinker's house.
9. The Brit is the one who drinks water.
10. The red house is somewhere to the left of the baker's house.
11. The occupant of the red house is either the baker or the doctor.
12. The purple house is not house 3.

## Puzzle paraphrase:zebra-00110

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, golf, tennis
- pet: horse, rabbit, fish, bird, dog
- drink: milk, cocoa, tea, coffee, juice
- nationality: Dane, Swede, Spaniard, Norwegian, Brit

Clues:
1. Whoever drinks juice is a golf enthusiast.
2. The Brit and the rabbit keeper live two houses apart.
3. The cocoa drinker's house is immediately to the left of the Dane's house.
4. The horse belongs to the cooking enthusiast.
5. The rabbit is kept in house 5.
6. The coffee drinker lives somewhere to the right of the Dane.
7. The tennis enthusiast lives directly to the left of the chess enthusiast.
8. The dog owner drinks juice.
9. The hiking enthusiast lives directly to the left of the dog owner.
10. The Swede occupies the leftmost house.
11. The Norwegian lives immediately to the right of the golf enthusiast.
12. The fish owner and the milk drinker are next-door neighbours.
