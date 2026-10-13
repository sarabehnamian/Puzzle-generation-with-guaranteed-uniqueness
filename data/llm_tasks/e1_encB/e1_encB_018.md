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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_018.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00190

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: hiking, painting, cooking, chess, tennis
- drink: milk, juice, cocoa, tea, water
- pet: fish, dog, rabbit, horse, cat

Clues:
1. Whoever is into chess has the rabbit.
2. The cocoa drinker lives somewhere further left than the juice drinker.
3. The Dane's pet is either the dog or the fish.
4. The cooking enthusiast occupies house 1.
5. Exactly one house separates the cat owner from the painting enthusiast.
6. The German is the one who drinks tea.
7. House 4 belongs to the hiking enthusiast.
8. The cooking enthusiast and the milk drinker are two houses apart.
9. The tennis player lives right next door to the east of the chess player, immediately to the right.
10. The horse owner drinks either milk or water.
11. The Swede lives directly to the left of the water drinker.
12. The dog owner drinks either juice or water.
13. The Brit's house sits immediately to the right of the Norwegian's.

## Puzzle paraphrase:zebra-00185

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, lawyer, pilot, doctor, farmer
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- hobby: chess, cooking, hiking, tennis, painting
- drink: tea, juice, water, milk, coffee

Clues:
1. The farmer and the milk drinker have one house between them.
2. Water is drunk in the second house.
3. The doctor's drink is coffee.
4. The Brit lives immediately to the right of the tea drinker.
5. The pilot's hobby is hiking.
6. The Spaniard lives in one of the two end houses.
7. The tennis enthusiast is either the baker or the pilot.
8. The baker lives immediately to the left of the Brit.
9. Painting is the Spaniard's hobby.
10. The Dane drinks either juice or tea.
11. The lawyer lives immediately to the left of the milk drinker.
12. The doctor's hobby is either cooking or hiking.
13. The cooking enthusiast lives next door to the Swede.

## Puzzle hard:zebra_hard-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, farmer, lawyer, baker
- color: red, yellow, purple, green, white
- drink: juice, tea, milk, coffee, cocoa
- pet: fish, bird, horse, dog, rabbit

Clues:
1. The teacher lives further to the right than the person in the red house.
2. One of the neighbours of the person who drinks milk lives in the green house.
3. The lawyer lives two doors away from the person who drinks tea.
4. Whoever lives in the green house and the rabbit owner are one and the same person.
5. The cocoa drinker and the owner of the fish are one and the same person.
6. The person in the green house has only one neighbour.
7. The farmer lives in the second house from the right.
8. The dog owner does not live to the right of the person who keeps the fish.
9. The person who keeps the fish and whoever lives in the yellow house are one and the same person.
10. The person who keeps the bird lives in the fourth house from the right.
11. The tea drinker and the occupant of the white house are one and the same person.
12. The right-hand neighbour of the baker drinks cocoa.
13. If whoever lives in the red house does not drink cocoa, then that person drinks coffee.

## Puzzle plain:zebra-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, tea, milk
- job: farmer, pilot, teacher, baker, lawyer
- nationality: Dane, German, Brit, Swede, Spaniard
- color: green, purple, yellow, white, blue

Clues:
1. There is exactly one house between the Brit and the farmer.
2. The person who drinks coffee lives in a lower-numbered house than the Spaniard.
3. The coffee drinker and the pilot live in adjacent houses.
4. The milk drinker lives at one end of the row.
5. The person who drinks cocoa lives in the leftmost house.
6. The person who drinks tea lives directly to the left of the Dane.
7. The lawyer lives next to the occupant of the white house.
8. The occupant of the blue house lives at one end of the row.
9. Whoever lives in the yellow house lives in the house just left of the one where the occupant of the white house lives.
10. The baker drinks coffee.
11. The Swede lives in the white house.
12. The person who drinks milk and whoever lives in the purple house live two houses apart.
13. The person in the purple house works as the baker.
14. The farmer lives immediately to the right of the lawyer.

## Puzzle plain:zebra-00086

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, coffee, juice, tea
- pet: horse, cat, dog, rabbit, fish
- hobby: painting, cooking, hiking, chess, golf
- nationality: Brit, Norwegian, German, Swede, Spaniard

Clues:
1. The Norwegian lives in house 4.
2. The fish owner lives in a lower-numbered house than the person who drinks cocoa.
3. The juice drinker lives in house 2.
4. The golf enthusiast lives in the house just left of the one where the chess enthusiast lives.
5. The person who enjoys hiking either is the German or is the Spaniard.
6. The horse owner is the Spaniard.
7. The owner of the rabbit is the Swede.
8. The person who enjoys chess lives next to the person who drinks cocoa.
9. The Brit lives directly to the left of the owner of the fish.
10. The person who drinks coffee and the water drinker live two houses apart.
11. The Brit and the person who enjoys golf live in adjacent houses.
12. The Spaniard drinks water.
13. The person who keeps the dog enjoys cooking.
14. The water drinker lives in a lower-numbered house than the coffee drinker.

## Puzzle paraphrase:zebra-00122

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, purple, red
- drink: tea, cocoa, juice, milk, coffee
- hobby: cooking, tennis, hiking, golf, painting
- pet: rabbit, fish, bird, cat, horse

Clues:
1. The white house lies somewhere to the left of the blue house.
2. The occupant of the green house drinks tea.
3. The hiking enthusiast lives directly to the left of the painting enthusiast.
4. The cat keeper lives immediately to the right of the cocoa drinker.
5. One house separates the cocoa drinker from the cooking enthusiast.
6. The juice drinker lives at one end of the row.
7. The fish keeper and the person in the purple house are next-door neighbours.
8. Exactly one house lies between the blue house and the white house.
9. The horse owner and the rabbit owner live side by side.
10. The milk drinker lives immediately to the right of the juice drinker.
11. The cooking enthusiast drinks tea.
12. The occupant of the red house keeps either the fish or the horse.
13. The golf enthusiast keeps the fish.

## Puzzle hard:zebra_hard-00055

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, chess, hiking, tennis
- drink: tea, juice, cocoa, coffee, water
- job: baker, pilot, teacher, lawyer, farmer
- nationality: German, Spaniard, Swede, Dane, Norwegian

Clues:
1. The person who enjoys golf and the person who drinks juice are one and the same person.
2. Exactly one house separates the farmer from the person who enjoys painting.
3. The farmer and the person who drinks tea are one and the same person.
4. The right-hand neighbour of the teacher is the Spaniard.
5. The left-hand neighbour of the lawyer enjoys tennis.
6. The right-hand neighbour of the farmer is the Norwegian.
7. The person who drinks juice does not live to the right of the person who drinks water.
8. The person who enjoys chess is not the same person as the Spaniard.
9. The left-hand neighbour of the Spaniard is the Swede.
10. The person who drinks cocoa and the Dane are one and the same person.
11. The cocoa drinker and the tennis enthusiast are one and the same person.
12. One of the neighbours of the pilot enjoys painting.

## Puzzle hard:zebra_hard-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- color: blue, red, green, white, purple
- hobby: golf, cooking, painting, tennis, chess
- job: lawyer, pilot, teacher, doctor, farmer

Clues:
1. The golf enthusiast and the water drinker are one and the same person.
2. The person who enjoys painting lives two doors away from the pilot.
3. The person who enjoys chess and the occupant of the green house are one and the same person.
4. The person who enjoys tennis lives somewhere between the person who enjoys cooking and the teacher.
5. One of the neighbours of the cocoa drinker lives in the purple house.
6. The doctor lives two doors away from the tennis enthusiast.
7. At least one house separates the lawyer from the teacher.
8. The occupant of the blue house and the doctor are one and the same person.
9. The chess enthusiast and the lawyer are one and the same person.
10. The left-hand neighbour of the person who drinks cocoa enjoys tennis.
11. The doctor is not the same person as the person who enjoys golf.
12. Exactly 3 houses lie to the left of the home of the occupant of the red house.
13. The juice drinker and the person who enjoys tennis are one and the same person.
14. One of the neighbours of the person who drinks coffee enjoys golf.

## Puzzle paraphrase:zebra-00121

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, purple
- hobby: cooking, golf, chess, tennis, hiking
- pet: fish, bird, horse, cat, dog
- nationality: Spaniard, Dane, Brit, Swede, German

Clues:
1. The dog owner and the keeper of the fish live next door to each other.
2. The hiking enthusiast lives right beside the Swede.
3. The Brit and the golf enthusiast have exactly one house between them.
4. The horse owner lives in the fifth house.
5. The Dane and the person in the yellow house are next-door neighbours.
6. The Swede's home adjoins the white house.
7. The fish keeper and the golf enthusiast live side by side.
8. The person in the purple house is the golf enthusiast.
9. The chess enthusiast is either the German or the Swede.
10. The German lives immediately to the right of the yellow house's occupant.
11. The bird owner lives in the blue house.
12. The Spaniard is the one who enjoys cooking.
13. The cooking enthusiast lives in the white house.

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
