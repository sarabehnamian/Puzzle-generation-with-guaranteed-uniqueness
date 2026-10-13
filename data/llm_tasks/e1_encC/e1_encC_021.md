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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_021.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00096

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Norwegian, Brit, Dane, Spaniard
- pet: fish, bird, cat, dog, rabbit
- drink: juice, tea, cocoa, water, coffee
- color: green, purple, white, yellow, blue

Clues:
1. The person who drinks cocoa lives next to the person who keeps the fish.
2. The person in the blue house and the owner of the cat live two houses apart.
3. The owner of the bird lives directly to the left of the person in the blue house.
4. The Swede does not live in the white house.
5. The person in the blue house and the Spaniard are neighbours.
6. The Norwegian lives in a lower-numbered house than the owner of the cat.
7. The rabbit owner lives next to the person who drinks tea.
8. The cocoa drinker and the juice drinker live in adjacent houses.
9. The bird owner and whoever lives in the green house are different people.
10. The person in the green house lives next to the Norwegian.
11. The person who keeps the fish does not live next to whoever lives in the yellow house.
12. The coffee drinker lives at one end of the row.
13. The rabbit owner lives in the last house.
14. The tea drinker lives in the house just left of the one where the occupant of the white house lives.
15. The cat owner either is the Dane or is the Spaniard.
16. The bird owner lives somewhere to the left of the person in the yellow house.
17. The cocoa drinker lives somewhere to the left of the Swede.

## Puzzle paraphrase:zebra-00111

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, water, juice, milk
- hobby: tennis, cooking, hiking, painting, golf
- color: white, blue, purple, green, red
- job: doctor, pilot, farmer, teacher, baker

Clues:
1. The farmer and the pilot live next door to each other.
2. The tea drinker lives in the green house.
3. The resident of the white house is into either cooking or tennis.
4. The coffee drinker lives in the purple house.
5. The baker's home is either the blue house or the purple house.
6. The hiking enthusiast does not live in the fourth house.
7. The farmer lives right beside the painting enthusiast.
8. The baker and the purple house's occupant are neighbours.
9. The milk drinker and the teacher live with exactly one house between them.
10. The tennis fan lives in the third house.
11. The cooking enthusiast lives in one of the two end houses.
12. The red house's occupant drinks water.
13. The hiking enthusiast lives immediately to the right of the pilot.
14. The cooking enthusiast lives directly to the left of the green house's occupant.
15. The farmer's hobby is either golf or hiking.

## Puzzle hard:zebra_hard-00066

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, bird, fish, cat
- color: red, yellow, purple, green, white
- drink: juice, coffee, water, milk, cocoa
- job: farmer, teacher, doctor, lawyer, baker

Clues:
1. The person who keeps the horse lives in the third house from the right.
2. One of the neighbours of the farmer works as the doctor.
3. The owner of the bird and the person who drinks cocoa are one and the same person.
4. Exactly 4 houses lie to the left of the home of the person who drinks water.
5. The right-hand neighbour of the person who keeps the horse keeps the rabbit.
6. The baker and the bird owner are one and the same person.
7. The person who keeps the cat lives further to the right than the lawyer.
8. The owner of the cat lives two doors away from the occupant of the yellow house.
9. One of the neighbours of the person who drinks milk drinks juice.
10. If the fish owner does not live in the purple house, then that person lives in the white house.
11. Neither the doctor nor whoever lives in the white house drinks milk.
12. Whoever lives in the purple house lives somewhere between the owner of the bird and whoever lives in the red house.
13. None of the neighbours of the person who drinks juice keeps the fish.
14. The person who drinks milk lives in the second house from the right.
15. The teacher and the occupant of the yellow house are one and the same person.

## Puzzle paraphrase:zebra-00165

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, doctor
- drink: tea, juice, milk, cocoa, coffee
- nationality: Norwegian, German, Swede, Brit, Spaniard
- hobby: chess, hiking, cooking, golf, tennis

Clues:
1. The Norwegian occupies house 1.
2. The tea drinker lives immediately to the left of the lawyer.
3. The German lives right before the farmer, directly to his left.
4. The milk drinker is not a chess player.
5. The golfer is the lawyer.
6. The farmer lives immediately to the left of the coffee drinker.
7. The Brit and the pilot have exactly one house between them.
8. The cocoa drinker lives directly to the left of the cooking enthusiast.
9. The farmer and the Spaniard live in neighbouring houses.
10. The doctor drinks either cocoa or juice.
11. The milk drinker lives immediately to the left of the tennis player.
12. The cooking enthusiast and the milk drinker live two houses apart.
13. The cocoa drinker lives right next door to the doctor.

## Puzzle hard:zebra_hard-00028

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, farmer, lawyer, baker
- drink: tea, juice, water, cocoa, milk
- pet: cat, dog, rabbit, fish, bird
- nationality: Norwegian, German, Brit, Spaniard, Dane

Clues:
1. The Brit lives two doors away from the owner of the rabbit.
2. Neither the person who keeps the rabbit nor the person who drinks tea works as the farmer.
3. At least one house separates the fish owner from the water drinker.
4. One of the neighbours of the person who drinks juice is the Dane.
5. The water drinker does not live in the third house from the right.
6. The juice drinker and the Spaniard are one and the same person.
7. The person who drinks cocoa has only one neighbour.
8. If the farmer does not drink milk, then that person drinks tea.
9. The owner of the dog lives further to the right than the doctor.
10. One of the neighbours of the Brit keeps the dog.
11. The bird owner lives further to the right than the cocoa drinker.
12. Exactly one house separates the Spaniard from the tea drinker.
13. The baker and the person who drinks juice are one and the same person.
14. The German lives somewhere between the owner of the bird and the person who drinks juice.
15. The left-hand neighbour of the lawyer is the German.
16. One of the neighbours of the lawyer keeps the bird.

## Puzzle plain:zebra-00053

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, dog, fish, horse
- nationality: Dane, Norwegian, Spaniard, Brit, Swede
- hobby: painting, tennis, golf, hiking, chess
- drink: cocoa, tea, coffee, milk, juice

Clues:
1. The juice drinker enjoys painting.
2. The person who keeps the dog is the Spaniard.
3. The chess enthusiast is the Brit.
4. The person who enjoys hiking lives immediately to the right of the person who enjoys golf.
5. The person who drinks milk lives in the third house.
6. The person who drinks juice lives in house 1.
7. The Brit keeps the cat.
8. There is exactly one house between the person who enjoys chess and the Norwegian.
9. The horse owner drinks tea.
10. The chess enthusiast lives in the house just left of the one where the owner of the rabbit lives.
11. The Dane lives immediately to the right of the owner of the rabbit.
12. The person who drinks coffee either enjoys painting or enjoys tennis.

## Puzzle plain:zebra-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, yellow, purple, blue, green
- hobby: cooking, tennis, golf, hiking, painting
- pet: bird, cat, fish, rabbit, horse
- job: baker, doctor, teacher, pilot, farmer

Clues:
1. The doctor enjoys hiking.
2. The owner of the rabbit lives somewhere to the left of whoever lives in the purple house.
3. The person who enjoys cooking lives next to the person who keeps the horse.
4. The cat owner lives directly to the left of the baker.
5. Whoever lives in the blue house lives immediately to the right of the tennis enthusiast.
6. The person who enjoys painting lives directly to the left of whoever lives in the green house.
7. The cooking enthusiast and the teacher live in adjacent houses.
8. Whoever lives in the red house lives directly to the left of the pilot.
9. The hiking enthusiast and whoever lives in the purple house live in adjacent houses.
10. The person who enjoys hiking lives in the third house.
11. The teacher either lives in the green house or lives in the red house.
12. The occupant of the blue house does not live next to the teacher.
13. The person who keeps the bird lives in house 1.

## Puzzle paraphrase:zebra-00184

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, dog, cat, bird
- color: purple, green, blue, white, red
- nationality: German, Dane, Norwegian, Spaniard, Brit
- drink: milk, water, coffee, cocoa, juice

Clues:
1. The Norwegian is the one who drinks water.
2. Cocoa is drunk at one end of the row.
3. The Dane lives immediately to the left of the Spaniard.
4. The fish is kept somewhere to the right of the horse.
5. The blue house is immediately to the left of the coffee drinker's house.
6. The Spaniard's house is immediately to the left of the milk drinker's house.
7. One house lies between the coffee drinker and the white house.
8. The bird's owner is either the Brit or the Dane.
9. The German drinks either coffee or juice.
10. Coffee is what the fish owner drinks.
11. The red house is house 5.
12. The cat owner and the purple house have exactly one house between them.
13. The green house and the Spaniard are two houses apart.

## Puzzle plain:zebra-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, rabbit, dog, horse, cat
- nationality: Swede, German, Spaniard, Norwegian, Dane
- hobby: chess, hiking, golf, tennis, cooking
- job: pilot, teacher, lawyer, doctor, baker

Clues:
1. The pilot lives next to the Swede.
2. The teacher lives in the first house.
3. The owner of the dog either enjoys chess or enjoys golf.
4. The cooking enthusiast lives somewhere to the right of the person who enjoys tennis.
5. The person who keeps the cat enjoys cooking.
6. The person who enjoys chess either keeps the horse or keeps the rabbit.
7. The owner of the rabbit lives directly to the left of the horse owner.
8. The doctor lives in the house just left of the one where the rabbit owner lives.
9. The chess enthusiast lives in the house just left of the one where the Dane lives.
10. The baker and the person who keeps the rabbit live two houses apart.
11. The Dane and the German live two houses apart.
12. There is exactly one house between the person who enjoys hiking and the rabbit owner.
13. The Spaniard lives immediately to the right of the owner of the rabbit.

## Puzzle paraphrase:zebra-00101

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, doctor, baker, teacher
- drink: water, tea, coffee, juice, milk
- hobby: golf, painting, chess, tennis, cooking
- color: red, white, purple, green, blue

Clues:
1. House 1 is where the teacher lives.
2. The baker lives next door to the water drinker.
3. The resident of the purple house drinks water.
4. The farmer's hobby is either cooking or painting.
5. The teacher's hobby is either chess or golf.
6. The painting enthusiast lives immediately to the left of the chess enthusiast.
7. The tennis enthusiast lives in the white house.
8. The pilot occupies house 4.
9. Exactly one house lies between the coffee drinker and the person in the green house.
10. The milk drinker does not live next door to the pilot.
11. The baker lives in either the green house or the purple house.
12. The doctor and the farmer have exactly one house between them.
13. The juice drinker and the occupant of the red house live in neighbouring houses.
14. The cooking enthusiast lives next door to the tennis enthusiast.
