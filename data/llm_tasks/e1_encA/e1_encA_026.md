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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_026.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, white, purple, green
- hobby: cooking, hiking, tennis, golf, chess
- nationality: Brit, German, Swede, Dane, Norwegian
- drink: coffee, water, cocoa, milk, tea

Clues:
1. If the person who enjoys chess does not live in the purple house, then that person lives in the yellow house.
2. The tea drinker lives somewhere between the cocoa drinker and whoever lives in the purple house.
3. One of the neighbours of the person who drinks coffee lives in the blue house.
4. One of the neighbours of the Norwegian enjoys cooking.
5. Exactly 2 houses lie to the left of the home of the golf enthusiast.
6. The person who drinks cocoa and the Dane are one and the same person.
7. At least one house separates the cooking enthusiast from the occupant of the yellow house.
8. The person who enjoys hiking and the Swede are one and the same person.
9. The Brit lives two doors away from the person who enjoys hiking.
10. The person who drinks milk and the Norwegian are one and the same person.
11. The occupant of the blue house lives somewhere between the person who enjoys golf and the person who drinks water.
12. Exactly 1 house lies to the left of the home of whoever lives in the white house.

## Puzzle hard:zebra_hard-00034

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, pilot, teacher, baker
- hobby: hiking, chess, golf, cooking, painting
- color: white, purple, blue, yellow, red
- pet: dog, fish, bird, cat, horse

Clues:
1. The baker lives two doors away from the person who enjoys painting.
2. At least one house separates the person who enjoys cooking from the farmer.
3. The person who enjoys golf and the pilot are one and the same person.
4. The right-hand neighbour of the person who keeps the fish keeps the horse.
5. One of the neighbours of the occupant of the blue house lives in the purple house.
6. One of the neighbours of the owner of the bird lives in the purple house.
7. The owner of the cat and the person in the red house are one and the same person.
8. The person who enjoys hiking has only one neighbour.
9. The horse owner is not the same person as the person in the purple house.
10. One of the neighbours of the person who enjoys hiking enjoys golf.
11. The right-hand neighbour of the cooking enthusiast lives in the white house.
12. One of the neighbours of the person who enjoys chess works as the lawyer.
13. The person who enjoys chess does not live in the third house from the right.
14. The right-hand neighbour of the occupant of the white house lives in the red house.
15. If the pilot does not live in the red house, then that person lives in the yellow house.

## Puzzle plain:zebra-00047

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Spaniard, Swede
- drink: tea, cocoa, juice, water, coffee
- pet: cat, rabbit, fish, horse, dog
- color: red, green, blue, white, yellow

Clues:
1. Whoever lives in the blue house lives in a lower-numbered house than the owner of the rabbit.
2. The Norwegian lives in the house just left of the one where the fish owner lives.
3. The Spaniard does not live next to whoever lives in the white house.
4. The person in the white house lives in house 3.
5. The owner of the dog either is the Dane or is the Swede.
6. The person in the blue house lives in the leftmost house.
7. The person who drinks tea does not live in house 5.
8. The Brit keeps the fish.
9. The person who drinks juice and the occupant of the red house live two houses apart.
10. The person who drinks coffee lives in the house just left of the one where the cat owner lives.
11. The horse owner lives in the white house.
12. The person who drinks tea lives in the yellow house.
13. The cocoa drinker keeps the cat.
14. The Dane either lives in the green house or lives in the red house.
15. The fish owner and whoever lives in the red house live in adjacent houses.

## Puzzle plain:zebra-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, Dane
- drink: juice, coffee, cocoa, water, tea
- hobby: tennis, hiking, painting, cooking, chess
- job: farmer, teacher, doctor, baker, lawyer

Clues:
1. The person who enjoys hiking and the tennis enthusiast live two houses apart.
2. The person who drinks cocoa is the Norwegian.
3. The chess enthusiast either is the Norwegian or is the Spaniard.
4. The water drinker is the Dane.
5. The farmer drinks juice.
6. The tennis enthusiast works as the teacher.
7. The baker and the painting enthusiast live in adjacent houses.
8. There is exactly one house between the hiking enthusiast and the juice drinker.
9. The chess enthusiast lives directly to the left of the coffee drinker.
10. The juice drinker lives immediately to the right of the Brit.
11. The Spaniard lives at one end of the row.
12. The baker does not live next to the lawyer.

## Puzzle hard:zebra_hard-00037

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Swede, Spaniard, Dane, Norwegian
- hobby: tennis, cooking, chess, golf, hiking
- pet: fish, horse, cat, bird, rabbit
- drink: tea, coffee, water, milk, juice

Clues:
1. The juice drinker and the person who keeps the rabbit are one and the same person.
2. The right-hand neighbour of the Spaniard is the Swede.
3. If the person who drinks coffee does not enjoy golf, then that person enjoys hiking.
4. The left-hand neighbour of the owner of the horse keeps the cat.
5. The person who drinks juice and the Spaniard are one and the same person.
6. The owner of the cat and the person who enjoys cooking are one and the same person.
7. The left-hand neighbour of the bird owner is the Spaniard.
8. The left-hand neighbour of the Norwegian drinks tea.
9. The chess enthusiast and the tea drinker are one and the same person.
10. The tennis enthusiast has only one neighbour.
11. The Spaniard lives somewhere between the coffee drinker and the water drinker.
12. The German and the water drinker are one and the same person.
13. The person who enjoys golf lives further to the right than the Spaniard.

## Puzzle hard:zebra_hard-00013

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, dog, cat, rabbit
- job: farmer, pilot, teacher, doctor, baker
- drink: juice, coffee, milk, tea, cocoa
- color: green, blue, yellow, white, purple

Clues:
1. The doctor lives somewhere between the coffee drinker and the person who keeps the dog.
2. The fish owner lives somewhere between the dog owner and the person who keeps the rabbit.
3. One of the neighbours of the doctor lives in the green house.
4. If the person who drinks juice is not the baker, then that person works as the teacher.
5. The cat owner lives further to the right than the coffee drinker.
6. The teacher lives somewhere between the farmer and the juice drinker.
7. Exactly one house separates the cocoa drinker from whoever lives in the yellow house.
8. At least one house separates the fish owner from the person in the white house.
9. The baker lives in the fourth house from the right.
10. The person who drinks cocoa lives somewhere between the farmer and the occupant of the green house.
11. The left-hand neighbour of the occupant of the blue house drinks milk.
12. The owner of the bird lives in the fourth house from the right.
13. The pilot and whoever lives in the purple house are one and the same person.

## Puzzle hard:zebra_hard-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, teacher, doctor, pilot
- pet: bird, fish, horse, cat, rabbit
- drink: cocoa, coffee, juice, tea, water
- color: red, yellow, purple, white, blue

Clues:
1. At least one house separates the teacher from the fish owner.
2. The person who drinks cocoa lives further to the right than the rabbit owner.
3. The doctor and the juice drinker are one and the same person.
4. The pilot lives somewhere between the owner of the rabbit and the occupant of the white house.
5. The water drinker lives further to the right than the pilot.
6. If the person in the purple house does not keep the fish, then that person keeps the horse.
7. One of the neighbours of the bird owner lives in the red house.
8. The right-hand neighbour of the person who keeps the horse drinks tea.
9. One of the neighbours of the fish owner lives in the red house.
10. Whoever lives in the white house does not live to the right of the occupant of the blue house.
11. The right-hand neighbour of the fish owner drinks cocoa.
12. The baker and whoever lives in the white house are one and the same person.
13. The person in the white house lives two doors away from the person in the yellow house.

## Puzzle paraphrase:zebra-00116

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, red, green, white, yellow
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, tennis, chess, cooking, hiking
- job: baker, lawyer, pilot, doctor, teacher

Clues:
1. The golf enthusiast is either the Brit or the Spaniard.
2. The doctor lives next door to the golf enthusiast.
3. The cooking enthusiast lives right beside the purple house.
4. The Swede lives somewhere to the right of the tennis enthusiast.
5. The Swede is the teacher.
6. The white house and the yellow house are two houses apart.
7. The baker and the pilot are next-door neighbours.
8. The lawyer and the yellow house's occupant live in adjacent houses.
9. The chess enthusiast lives in the red house.
10. The Brit is the lawyer.
11. The Dane does not live in the fourth house.
12. The purple house is directly to the left of the pilot.
13. The German lives in the purple house.
14. The hiking enthusiast lives immediately to the right of the red house.

## Puzzle paraphrase:zebra-00146

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Dane, Spaniard, Norwegian
- job: teacher, baker, pilot, doctor, lawyer
- hobby: cooking, hiking, golf, chess, tennis
- drink: cocoa, coffee, tea, juice, water

Clues:
1. The Dane occupies the leftmost house.
2. The cooking enthusiast is either the Brit or the Dane.
3. Golf is the Dane's hobby.
4. The baker lives next to the chess enthusiast.
5. The hiking enthusiast lives in house 2.
6. The doctor is a coffee drinker.
7. The coffee drinker and the Spaniard live side by side.
8. The baker lives next door to the water drinker.
9. The coffee drinker and the tea drinker live two houses apart.
10. The Norwegian lives next door to the tennis enthusiast.
11. The hiking enthusiast and the lawyer have exactly one house between them.
12. The tennis enthusiast is the pilot.
13. The Norwegian drinks cocoa.

## Puzzle paraphrase:zebra-00187

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, water, coffee
- pet: dog, bird, rabbit, horse, fish
- hobby: painting, chess, tennis, cooking, golf
- color: green, red, yellow, blue, purple

Clues:
1. The green house is immediately to the left of the bird's house.
2. Juice is drunk in the yellow house.
3. The tea drinker's hobby is painting.
4. The rabbit owner and the tea drinker are not neighbours.
5. The tennis enthusiast lives in house 1.
6. The milk drinker and the rabbit owner have exactly one house between them.
7. The yellow house is immediately to the left of the horse's house.
8. The painting enthusiast lives immediately to the left of the blue house.
9. The golf enthusiast lives immediately to the right of the yellow house.
10. The fish is kept somewhere to the right of the green house.
11. The cooking enthusiast keeps either the dog or the rabbit.
12. The red house is the second house.
13. The juice drinker lives immediately to the left of the water drinker.
