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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_009.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00170

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, yellow, red
- nationality: Norwegian, German, Dane, Swede, Brit
- drink: tea, milk, water, cocoa, coffee
- hobby: hiking, chess, painting, tennis, golf

Clues:
1. The hiker is either the German or the Swede.
2. The tea drinker lives right next to the tennis enthusiast.
3. The Norwegian and the resident of the white house are separated by exactly one house.
4. The painting enthusiast lives immediately to the right of the hiker.
5. One house separates the tennis enthusiast from the water drinker.
6. The hiker and the tennis enthusiast have exactly one house between them.
7. The Swede's house lies somewhere to the right of the white house.
8. Whoever is in the red house is either the golf enthusiast or the hiker.
9. The Dane's hobby is golf.
10. The Brit's house is adjacent to the German's.
11. The milk drinker is not next door to the tea drinker.
12. The coffee drinker lives next door to the Dane.
13. The Swede lives right beside the yellow house.
14. The chess enthusiast lives immediately to the right of the green house.
15. The tennis enthusiast lives somewhere to the right of the Brit.
16. The coffee drinker lives somewhere to the left of the cocoa drinker.

## Puzzle paraphrase:zebra-00135

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, painting, chess, tennis
- color: blue, red, green, white, yellow
- pet: cat, rabbit, dog, horse, bird
- job: lawyer, farmer, doctor, teacher, baker

Clues:
1. The yellow house is the fourth house.
2. The dog owner lives immediately to the left of the rabbit owner.
3. The baker's hobby is cooking.
4. The bird owner does not live in the first house.
5. The white house is directly to the left of the green house.
6. The farmer keeps the dog.
7. The bird owner is the lawyer.
8. The cat owner lives somewhere to the right of the baker.
9. One house lies between the blue house and the rabbit owner.
10. The occupant of the blue house is either the doctor or the farmer.
11. The green house lies somewhere to the left of the farmer.
12. The painting enthusiast lives in the fourth house.
13. The chess enthusiast lives in one of the two end houses.
14. The tennis enthusiast lives directly to the left of the painting enthusiast.

## Puzzle paraphrase:zebra-00181

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Swede, Spaniard
- color: white, green, yellow, blue, purple
- job: doctor, baker, farmer, teacher, lawyer
- pet: cat, dog, rabbit, horse, fish

Clues:
1. The blue house and the dog owner are next-door neighbours.
2. The doctor lives in the yellow house.
3. The Norwegian has the rabbit.
4. The doctor is not in house 5.
5. The Dane lives in house 2.
6. The green house belongs to the horse owner.
7. The farmer lives next door to the Norwegian.
8. The purple house's occupant keeps the dog.
9. The horse owner lives in house 3.
10. The lawyer lives right after the blue house, immediately to its right.
11. The Spaniard lives in house 4.
12. The Swede lives immediately to the left of the baker.
13. The fish owner is a neighbour of the Norwegian.

## Puzzle hard:zebra_hard-00080

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, horse, dog
- nationality: Brit, German, Swede, Norwegian, Dane
- drink: tea, coffee, juice, water, milk
- hobby: cooking, painting, chess, tennis, hiking

Clues:
1. If the person who drinks water does not keep the dog, then that person keeps the horse.
2. One of the neighbours of the person who drinks juice keeps the dog.
3. If the Swede does not enjoy cooking, then that person enjoys painting.
4. The right-hand neighbour of the Norwegian keeps the dog.
5. If the German does not drink milk, then that person drinks water.
6. The Brit lives two doors away from the rabbit owner.
7. The person who enjoys hiking has only one neighbour.
8. One of the neighbours of the owner of the horse enjoys tennis.
9. The tea drinker lives in the fourth house from the right.
10. One of the neighbours of the person who enjoys cooking drinks milk.
11. Exactly 0 houses lie to the left of the home of the person who drinks milk.
12. The left-hand neighbour of the owner of the cat is the Swede.
13. Exactly 4 houses lie to the left of the home of the Brit.
14. Exactly 4 houses lie to the left of the home of the owner of the dog.

## Puzzle hard:zebra_hard-00041

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, German, Dane, Swede
- color: yellow, blue, green, purple, red
- hobby: cooking, painting, hiking, golf, tennis
- drink: cocoa, tea, milk, juice, water

Clues:
1. The occupant of the red house lives further to the right than the hiking enthusiast.
2. The right-hand neighbour of the German drinks tea.
3. Neither the occupant of the blue house nor the person who enjoys golf drinks juice.
4. The person who enjoys golf and the tea drinker are one and the same person.
5. Whoever lives in the blue house and the Dane are one and the same person.
6. The cocoa drinker and the German are one and the same person.
7. One of the neighbours of the person who enjoys painting lives in the green house.
8. Exactly 1 house lies to the left of the home of the person who enjoys cooking.
9. Exactly one house separates the person who enjoys hiking from the Swede.
10. None of the neighbours of the hiking enthusiast lives in the yellow house.
11. The water drinker lives in the second house from the right.
12. One of the neighbours of the Swede is the Norwegian.
13. The person in the green house does not live in the third house from the right.
14. The left-hand neighbour of the person in the red house is the Norwegian.

## Puzzle paraphrase:zebra-00134

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- hobby: golf, chess, cooking, painting, tennis
- job: doctor, farmer, baker, lawyer, teacher
- pet: cat, rabbit, horse, bird, fish

Clues:
1. The painting enthusiast lives directly to the right of the golf enthusiast.
2. The cat owner and the teacher live in adjacent houses.
3. The Brit keeps the rabbit.
4. The Dane is the farmer.
5. The baker and the cat owner live two houses apart.
6. The cooking enthusiast lives immediately to the left of the bird owner.
7. The baker lives directly to the right of the farmer.
8. The Spaniard lives directly to the right of the Dane.
9. The rabbit owner's hobby is tennis.
10. The Swede keeps the horse.
11. The rabbit owner lives immediately to the left of the lawyer.
12. The Swede is the cooking enthusiast.

## Puzzle plain:zebra-00016

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

## Puzzle plain:zebra-00058

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, tennis, painting, cooking
- job: teacher, lawyer, farmer, doctor, baker
- pet: fish, dog, cat, horse, bird
- color: purple, red, yellow, green, white

Clues:
1. The occupant of the purple house lives directly to the left of the bird owner.
2. The bird owner and the farmer are not neighbours.
3. The farmer and the person who keeps the horse live two houses apart.
4. The person in the red house and the person who enjoys tennis live two houses apart.
5. The painting enthusiast either lives in the white house or lives in the yellow house.
6. The doctor and whoever lives in the green house live two houses apart.
7. The occupant of the white house enjoys hiking.
8. The owner of the fish lives in the second house.
9. There is exactly one house between the baker and the farmer.
10. The person who keeps the cat enjoys chess.
11. The baker either enjoys hiking or enjoys tennis.
12. The teacher lives in the green house.
13. Whoever lives in the white house lives in house 2.
14. The person in the red house lives in a lower-numbered house than the owner of the bird.

## Puzzle hard:zebra_hard-00036

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, tea, water
- job: teacher, lawyer, pilot, farmer, baker
- color: purple, blue, green, red, white
- pet: dog, fish, bird, cat, rabbit

Clues:
1. The baker lives somewhere between the person who keeps the cat and the lawyer.
2. Neither the fish owner nor the person who drinks water lives in the green house.
3. The person who keeps the dog lives in the second house from the right.
4. The teacher and the water drinker are one and the same person.
5. Exactly one house separates the person who drinks juice from whoever lives in the red house.
6. If the person in the white house does not keep the bird, then that person keeps the rabbit.
7. The bird owner lives two doors away from the farmer.
8. The bird owner and the teacher are one and the same person.
9. Exactly one house separates the person who keeps the cat from whoever lives in the red house.
10. Exactly one house separates the coffee drinker from the person in the white house.
11. The owner of the fish and the person who drinks juice are one and the same person.
12. Whoever lives in the purple house lives two doors away from the teacher.
13. The person who keeps the bird lives in the fourth house from the right.
14. The person who drinks tea lives further to the right than whoever lives in the red house.

## Puzzle hard:zebra_hard-00079

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, teacher
- pet: fish, bird, rabbit, horse, cat
- hobby: tennis, chess, painting, cooking, hiking
- color: red, yellow, white, purple, blue

Clues:
1. If the occupant of the yellow house does not enjoy cooking, then that person enjoys tennis.
2. Exactly one house separates the person who keeps the rabbit from whoever lives in the yellow house.
3. If the cat owner is not the baker, then that person works as the lawyer.
4. The occupant of the yellow house lives in the fourth house from the right.
5. One of the neighbours of the person who keeps the horse lives in the purple house.
6. The person who enjoys tennis lives somewhere between the owner of the bird and whoever lives in the blue house.
7. The person who enjoys painting and whoever lives in the red house are one and the same person.
8. The teacher lives further to the right than the owner of the fish.
9. One of the neighbours of the person who enjoys chess keeps the fish.
10. The right-hand neighbour of whoever lives in the yellow house enjoys painting.
11. The doctor and whoever lives in the white house are one and the same person.
12. The owner of the cat and the cooking enthusiast are one and the same person.
13. The baker and the painting enthusiast are one and the same person.
