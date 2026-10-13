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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_025.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live next door to the painting enthusiast.
2. The chess enthusiast and the Spaniard live two houses apart.
3. The dog belongs to the Spaniard.
4. Painting is the hobby of the juice drinker.
5. The cooking enthusiast lives in one of the two end houses.
6. One house sits between the fish owner and the juice drinker.
7. Cocoa is what the dog owner drinks.
8. The Swede drinks tea.
9. The juice drinker and the tennis enthusiast have exactly one house between them.
10. The bird lives in house 2.
11. The German lives in one of the two end houses.
12. The milk drinker lives immediately to the left of the juice drinker.
13. The Dane and the tennis enthusiast live two houses apart.
14. The rabbit owner lives in a house with a lower number than the Swede's.
15. The chess enthusiast lives somewhere to the right of the Dane.

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

## Puzzle paraphrase:zebra-00106

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, painting, golf, tennis, chess
- color: yellow, red, green, blue, purple
- job: pilot, doctor, baker, lawyer, teacher
- nationality: Dane, Norwegian, German, Spaniard, Swede

Clues:
1. The Spaniard's home is the second house.
2. The cooking enthusiast is either the lawyer or the pilot.
3. The Swede lives immediately to the right of the green house's occupant.
4. The golf enthusiast and the pilot have exactly one house between them.
5. The doctor lives immediately to the right of the Norwegian.
6. The lawyer lives immediately to the left of the tennis enthusiast.
7. The teacher lives in house 2.
8. The Dane lives immediately to the left of the red house's occupant.
9. The golf enthusiast lives in the purple house.
10. The chess enthusiast lives in the blue house.
11. The Norwegian lives somewhere to the left of the yellow house's occupant.
12. The tennis enthusiast lives in the fourth house.

## Puzzle hard:zebra_hard-00082

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, lawyer, doctor, farmer, pilot
- color: yellow, blue, white, green, purple
- pet: dog, bird, fish, cat, horse
- drink: cocoa, water, coffee, milk, tea

Clues:
1. If the person who keeps the fish does not drink cocoa, then that person drinks coffee.
2. The cocoa drinker lives further to the right than the pilot.
3. The right-hand neighbour of the farmer drinks water.
4. The person who keeps the horse lives in the third house from the right.
5. The farmer and whoever lives in the purple house are one and the same person.
6. The doctor has only one neighbour.
7. The doctor and the occupant of the green house are one and the same person.
8. Exactly 0 houses lie to the left of the home of whoever lives in the blue house.
9. The left-hand neighbour of the teacher keeps the bird.
10. The cocoa drinker and the farmer are one and the same person.
11. The cat owner and the person in the white house are one and the same person.
12. None of the neighbours of the farmer keeps the dog.
13. The occupant of the blue house and the person who drinks tea are one and the same person.

## Puzzle paraphrase:zebra-00119

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, farmer
- color: green, white, blue, red, yellow
- hobby: cooking, tennis, chess, hiking, painting
- pet: horse, dog, cat, bird, rabbit

Clues:
1. The white house is somewhere to the left of the bird owner.
2. The yellow house is house 5.
3. The tennis enthusiast is the lawyer.
4. The rabbit is kept in the leftmost house.
5. The cooking enthusiast and the lawyer are two houses apart.
6. The blue house's occupant is the chess enthusiast.
7. Exactly one house lies between the horse owner and the red house.
8. The blue house's occupant is not the doctor.
9. The cooking enthusiast and the white house's occupant are two houses apart.
10. The horse owner is the hiking enthusiast.
11. The baker lives in house 2.
12. The pilot's hobby is either painting or tennis.
13. The chess enthusiast and the white house's occupant are not neighbours.
14. The dog owner is the pilot.

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

## Puzzle hard:zebra_hard-00054

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, cocoa, tea, juice
- pet: fish, horse, rabbit, cat, bird
- hobby: chess, cooking, painting, golf, tennis
- nationality: Dane, Brit, Spaniard, German, Swede

Clues:
1. The German lives in the fourth house from the right.
2. Exactly 0 houses lie to the left of the home of the person who drinks cocoa.
3. The left-hand neighbour of the owner of the fish is the Spaniard.
4. The person who enjoys golf and the Swede are one and the same person.
5. The person who enjoys chess and the person who keeps the fish are one and the same person.
6. One of the neighbours of the person who keeps the cat keeps the fish.
7. None of the neighbours of the owner of the rabbit keeps the fish.
8. The owner of the cat and the Dane are one and the same person.
9. The right-hand neighbour of the cooking enthusiast drinks tea.
10. Exactly one house separates the person who enjoys golf from the painting enthusiast.
11. One of the neighbours of the coffee drinker is the Dane.
12. The right-hand neighbour of the person who keeps the cat keeps the horse.
13. Exactly 4 houses lie to the left of the home of the person who drinks juice.

## Puzzle hard:zebra_hard-00038

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, white, yellow, red
- drink: water, coffee, cocoa, tea, juice
- pet: horse, bird, dog, rabbit, fish
- hobby: hiking, cooking, golf, tennis, painting

Clues:
1. If the person in the white house does not drink cocoa, then that person drinks tea.
2. The right-hand neighbour of the cooking enthusiast drinks tea.
3. One of the neighbours of the golf enthusiast drinks juice.
4. The person who keeps the bird and the coffee drinker are one and the same person.
5. The horse owner and the person who drinks tea are one and the same person.
6. The person who enjoys painting and the person who drinks tea are one and the same person.
7. If whoever lives in the yellow house does not keep the fish, then that person keeps the horse.
8. Whoever lives in the red house has only one neighbour.
9. If the occupant of the red house does not keep the horse, then that person keeps the rabbit.
10. Whoever lives in the white house lives further to the right than the owner of the horse.
11. The left-hand neighbour of whoever lives in the yellow house enjoys hiking.
12. The juice drinker lives somewhere between the occupant of the purple house and the person in the white house.
13. One of the neighbours of whoever lives in the red house lives in the purple house.
