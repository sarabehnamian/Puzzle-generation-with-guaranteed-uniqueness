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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, farmer, baker, pilot
- nationality: Spaniard, Norwegian, Swede, German, Brit
- drink: milk, tea, water, juice, coffee
- color: green, purple, blue, white, red

Clues:
1. The milk drinker lives in the house just left of the one where the tea drinker lives.
2. The occupant of the blue house lives immediately to the right of the Swede.
3. The baker lives in the blue house.
4. The Swede and the tea drinker live in adjacent houses.
5. Whoever lives in the white house either drinks milk or drinks water.
6. Whoever lives in the purple house lives immediately to the right of the milk drinker.
7. The Brit lives in the red house.
8. The farmer and the milk drinker live two houses apart.
9. The German lives in the last house.
10. The lawyer is the Norwegian.
11. The person who drinks coffee and the Swede are neighbours.
12. The Brit lives directly to the left of the occupant of the green house.
13. The doctor either is the Brit or is the German.
14. There is exactly one house between the Norwegian and the water drinker.

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

## Puzzle plain:zebra-00081

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, tennis, cooking, chess, golf
- job: pilot, teacher, doctor, baker, lawyer
- color: white, yellow, red, purple, green
- drink: water, cocoa, tea, coffee, juice

Clues:
1. The cocoa drinker lives in the leftmost house.
2. The golf enthusiast lives in the middle house.
3. The hiking enthusiast works as the baker.
4. The tea drinker lives in house 4.
5. The teacher lives immediately to the right of the person who enjoys hiking.
6. The person who enjoys cooking either drinks coffee or drinks tea.
7. The doctor either lives in the green house or lives in the yellow house.
8. Whoever lives in the purple house works as the pilot.
9. Whoever lives in the yellow house lives in the house just left of the one where the person who enjoys tennis lives.
10. Whoever lives in the white house enjoys cooking.
11. Whoever lives in the green house lives directly to the left of the person in the yellow house.
12. The doctor enjoys chess.
13. The person who drinks juice and the pilot live two houses apart.

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

## Puzzle plain:zebra-00029

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, bird, cat
- drink: tea, water, coffee, milk, cocoa
- color: purple, white, green, blue, red
- job: lawyer, farmer, pilot, doctor, teacher

Clues:
1. The cocoa drinker lives in house 1.
2. Whoever lives in the purple house keeps the cat.
3. The farmer lives in the blue house.
4. The lawyer lives in the house just left of the one where the horse owner lives.
5. The person in the blue house and the owner of the fish live two houses apart.
6. The pilot either lives in the blue house or lives in the red house.
7. The person who keeps the horse lives immediately to the right of the person in the white house.
8. The person in the purple house lives directly to the left of the person who drinks milk.
9. The person who keeps the horse and the person who drinks tea are neighbours.
10. The tea drinker lives somewhere to the left of the doctor.
11. The owner of the rabbit either lives in the purple house or lives in the white house.
12. The lawyer lives in house 3.
13. The person in the blue house and the person who drinks water are neighbours.

## Puzzle hard:zebra_hard-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, yellow, green, white
- nationality: Dane, Brit, Spaniard, Swede, German
- hobby: tennis, painting, golf, chess, hiking
- pet: cat, fish, rabbit, dog, bird

Clues:
1. The dog owner is not the same person as the occupant of the yellow house.
2. The German lives somewhere between the golf enthusiast and the person who enjoys hiking.
3. The tennis enthusiast is not the same person as the occupant of the white house.
4. The occupant of the blue house has only one neighbour.
5. The right-hand neighbour of the owner of the bird is the Brit.
6. If the person who keeps the bird does not enjoy hiking, then that person enjoys tennis.
7. Whoever lives in the green house lives two doors away from the Spaniard.
8. One of the neighbours of the person who keeps the bird keeps the fish.
9. One of the neighbours of the Swede enjoys hiking.
10. The left-hand neighbour of the person who enjoys tennis enjoys hiking.
11. The person who enjoys painting lives somewhere between the owner of the rabbit and the occupant of the yellow house.
12. None of the neighbours of the owner of the fish enjoys chess.
13. One of the neighbours of the occupant of the green house keeps the bird.
14. Whoever lives in the blue house and the Swede are one and the same person.
15. The right-hand neighbour of the person in the yellow house keeps the bird.

## Puzzle hard:zebra_hard-00012

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, hiking, painting, chess, tennis
- job: lawyer, doctor, baker, teacher, pilot
- color: blue, red, yellow, green, white
- pet: cat, dog, fish, rabbit, horse

Clues:
1. The person who keeps the horse is not the same person as the tennis enthusiast.
2. The left-hand neighbour of the fish owner keeps the rabbit.
3. If the doctor does not keep the dog, then that person keeps the horse.
4. If the occupant of the white house does not enjoy painting, then that person enjoys tennis.
5. The left-hand neighbour of the person who keeps the fish works as the teacher.
6. The occupant of the white house lives somewhere between the baker and the person who keeps the dog.
7. The left-hand neighbour of the person who enjoys chess keeps the cat.
8. If the occupant of the yellow house does not keep the fish, then that person keeps the rabbit.
9. At least one house separates the person who enjoys tennis from the person who keeps the fish.
10. The person who enjoys tennis does not live to the right of the person who enjoys painting.
11. One of the neighbours of the lawyer lives in the blue house.
12. The person in the green house and the teacher are one and the same person.
13. The person who keeps the fish and the person who enjoys golf are one and the same person.
14. The chess enthusiast has only one neighbour.

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

## Puzzle plain:zebra-00039

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, coffee, tea
- nationality: German, Spaniard, Brit, Norwegian, Dane
- job: lawyer, baker, pilot, teacher, doctor
- color: yellow, red, blue, white, green

Clues:
1. The juice drinker either is the German or is the Spaniard.
2. The cocoa drinker is the Brit.
3. The occupant of the red house lives at one end of the row.
4. The occupant of the white house lives in the house just left of the one where the doctor lives.
5. The teacher and the person who drinks water are neighbours.
6. The Norwegian drinks tea.
7. The Brit and whoever lives in the red house live two houses apart.
8. The lawyer lives in the white house.
9. The person in the red house is not the baker.
10. There is exactly one house between the Brit and the Dane.
11. The Spaniard lives in the blue house.
12. The teacher drinks juice.
13. The Dane lives in a lower-numbered house than the Norwegian.
14. The person in the green house and the person who drinks juice are not neighbours.
15. The German either lives in the blue house or lives in the white house.
