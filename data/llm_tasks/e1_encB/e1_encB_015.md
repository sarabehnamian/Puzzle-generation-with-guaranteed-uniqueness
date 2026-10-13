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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_015.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- nationality: German, Brit, Norwegian, Swede, Spaniard
- hobby: chess, cooking, painting, tennis, golf
- color: red, purple, white, green, yellow

Clues:
1. The German lives somewhere to the left of whoever lives in the yellow house.
2. The painting enthusiast works as the doctor.
3. There is exactly one house between the cooking enthusiast and the occupant of the red house.
4. The occupant of the white house lives somewhere to the left of the person who enjoys tennis.
5. Whoever lives in the green house works as the baker.
6. The Spaniard lives next to the person who enjoys tennis.
7. The Brit and the Swede are neighbours.
8. There is exactly one house between the cooking enthusiast and the Spaniard.
9. The farmer either is the Norwegian or is the Swede.
10. The golf enthusiast and the teacher are neighbours.
11. The baker is the Brit.
12. The German and the person in the purple house live two houses apart.
13. The golf enthusiast lives directly to the left of the baker.

## Puzzle paraphrase:zebra-00166

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, painting, hiking
- job: pilot, farmer, teacher, doctor, baker
- pet: dog, cat, fish, rabbit, horse
- color: yellow, purple, red, blue, green

Clues:
1. The hiker lives right beside the rabbit's owner.
2. The cat lives in the red house.
3. The fish is kept by the doctor.
4. The golfer and the horse owner live in adjacent houses.
5. The baker is the occupant of the yellow house.
6. Exactly one house stands between the horse owner and the rabbit owner.
7. Cooking is the baker's hobby.
8. The blue house's occupant and the fish owner are next-door neighbours.
9. The fish owner lives in one of the two end houses.
10. One house separates the horse owner from the yellow house's occupant.
11. The farmer lives further left than the teacher.
12. The green house stands immediately to the right of the blue house.
13. The pilot and the purple house's occupant have exactly one house between them.
14. The horse owner and the painter live two houses apart.

## Puzzle paraphrase:zebra-00105

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, bird, cat
- job: lawyer, farmer, teacher, pilot, doctor
- drink: juice, tea, milk, water, coffee
- color: green, blue, white, red, purple

Clues:
1. The green house belongs to the lawyer.
2. House 4 is where the coffee drinker lives.
3. Somewhere to the right of the blue house's occupant lives the occupant of the red house.
4. The cat owner lives immediately to the right of the dog owner.
5. The bird owner and the doctor live in neighbouring houses.
6. The tea drinker lives immediately to the right of the rabbit owner.
7. The farmer lives in the red house.
8. The juice drinker lives immediately to the left of the purple house's occupant.
9. The coffee drinker and the doctor have exactly one house between them.
10. The coffee drinker and the pilot live next door to each other.
11. The horse is kept by the occupant of the blue house.
12. The water drinker lives immediately to the left of the lawyer.

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

## Puzzle paraphrase:zebra-00177

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- job: baker, farmer, pilot, doctor, lawyer
- color: purple, yellow, green, red, white
- pet: horse, cat, fish, bird, dog

Clues:
1. The horse owner drinks tea.
2. The red house is house 5.
3. The fish owner lives immediately to the right of the juice drinker.
4. The coffee drinker lives in a lower-numbered house than the white house's occupant.
5. The juice drinker and the occupant of the yellow house have exactly one house between them.
6. The yellow house is at one end of the row.
7. The bird owner and the fish owner are two houses apart.
8. The baker lives in house 2.
9. The purple house's occupant drinks water.
10. One house stands between the dog owner and the tea drinker.
11. The cocoa drinker is the lawyer.
12. The white house is immediately to the left of the pilot's.
13. The doctor and the occupant of the white house live in adjacent houses.

## Puzzle hard:zebra_hard-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, cooking, painting
- pet: bird, rabbit, dog, cat, fish
- color: blue, red, yellow, white, green
- job: lawyer, farmer, pilot, baker, teacher

Clues:
1. The bird owner and the pilot are one and the same person.
2. The right-hand neighbour of the painting enthusiast enjoys cooking.
3. If the person in the green house is not the lawyer, then that person works as the pilot.
4. The person who enjoys chess has only one neighbour.
5. Neither the owner of the bird nor the chess enthusiast lives in the blue house.
6. The right-hand neighbour of the person who enjoys cooking lives in the white house.
7. The occupant of the green house and the person who enjoys tennis are one and the same person.
8. Exactly 1 house lies to the left of the home of whoever lives in the yellow house.
9. The baker lives further to the right than the bird owner.
10. The owner of the fish lives further to the right than the farmer.
11. At least one house separates the cooking enthusiast from the owner of the cat.
12. The person who keeps the cat lives two doors away from the person who keeps the dog.
13. Exactly 1 house lies to the left of the home of the person who keeps the dog.
14. The person who enjoys painting and the teacher are one and the same person.
15. The golf enthusiast lives somewhere between whoever lives in the blue house and whoever lives in the red house.

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

## Puzzle hard:zebra_hard-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, juice, cocoa, water, coffee
- job: teacher, lawyer, baker, farmer, doctor
- nationality: Dane, Swede, Brit, German, Spaniard
- hobby: chess, golf, cooking, hiking, painting

Clues:
1. One of the neighbours of the painting enthusiast enjoys hiking.
2. If the lawyer does not drink cocoa, then that person drinks coffee.
3. Exactly 3 houses lie to the left of the home of the teacher.
4. The right-hand neighbour of the person who drinks cocoa is the Brit.
5. The Dane has only one neighbour.
6. If the German is not the doctor, then that person works as the farmer.
7. The right-hand neighbour of the doctor enjoys cooking.
8. The person who enjoys hiking has only one neighbour.
9. Exactly 1 house lies to the left of the home of the person who drinks water.
10. One of the neighbours of the Spaniard works as the teacher.
11. The chess enthusiast and the Spaniard are one and the same person.
12. The doctor lives somewhere between the Brit and the farmer.
13. The left-hand neighbour of the doctor drinks milk.
14. The Brit is not the same person as the juice drinker.

## Puzzle paraphrase:zebra-00123

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, juice, milk, tea
- job: pilot, teacher, baker, farmer, lawyer
- nationality: Norwegian, Brit, Swede, German, Spaniard
- pet: cat, dog, bird, horse, rabbit

Clues:
1. The dog owner is the teacher.
2. The Norwegian lives in the fifth house.
3. The Swede drinks either juice or milk.
4. The Swede is the pilot.
5. The tea drinker keeps the rabbit.
6. The dog owner lives next door to the Norwegian.
7. The Spaniard is a milk drinker.
8. The milk drinker and the water drinker have exactly one house between them.
9. The farmer lives in the house immediately to the right of the dog owner.
10. The baker's house adjoins the cat keeper's.
11. The farmer and the horse owner live two houses apart.
12. The German lives directly to the right of the rabbit keeper.
