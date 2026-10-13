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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00024

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, green, red, purple, white
- hobby: golf, cooking, tennis, painting, chess
- nationality: Spaniard, Swede, Norwegian, German, Brit
- job: farmer, pilot, doctor, teacher, lawyer

Clues:
1. The farmer and the tennis enthusiast are one and the same person.
2. None of the neighbours of the farmer is the Swede.
3. The person who enjoys cooking and the person in the green house are one and the same person.
4. Exactly 1 house lies to the left of the home of the tennis enthusiast.
5. The German lives somewhere between the Brit and whoever lives in the green house.
6. Exactly one house separates the doctor from the person who enjoys golf.
7. If the tennis enthusiast is not the Brit, then that person is the Norwegian.
8. The chess enthusiast is not the same person as the lawyer.
9. The pilot does not live to the right of the lawyer.
10. The right-hand neighbour of whoever lives in the white house works as the pilot.
11. The German and whoever lives in the red house are one and the same person.
12. Whoever lives in the purple house and the Swede are one and the same person.
13. The person who enjoys chess lives further to the right than the Spaniard.
14. Exactly 4 houses lie to the left of the home of whoever lives in the green house.

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

## Puzzle plain:zebra-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, coffee
- job: teacher, doctor, pilot, baker, farmer
- nationality: Swede, Dane, Norwegian, German, Spaniard
- hobby: tennis, golf, cooking, painting, chess

Clues:
1. The teacher and the person who enjoys chess are different people.
2. The baker lives immediately to the right of the person who enjoys cooking.
3. The milk drinker lives immediately to the right of the water drinker.
4. The German and the Spaniard live two houses apart.
5. The doctor either drinks coffee or drinks milk.
6. The Swede lives in house 5.
7. The Dane and the person who drinks milk live in adjacent houses.
8. The person who enjoys golf lives somewhere to the left of the juice drinker.
9. The person who enjoys painting lives in one of the two end houses.
10. The German lives immediately to the right of the chess enthusiast.
11. The Dane and the doctor live two houses apart.
12. The pilot lives in the middle house.
13. The person who drinks juice is the Spaniard.
14. The baker lives in the fourth house.

## Puzzle plain:zebra-00056

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, horse, cat, fish
- color: blue, purple, red, green, white
- nationality: Dane, German, Norwegian, Swede, Brit
- job: teacher, baker, doctor, farmer, pilot

Clues:
1. There is exactly one house between the Dane and the occupant of the green house.
2. The horse owner lives directly to the left of whoever lives in the white house.
3. The Brit lives directly to the left of the baker.
4. The fish owner and the person in the green house are neighbours.
5. The Swede lives at one end of the row.
6. The German keeps the dog.
7. The fish owner lives next to the person in the red house.
8. The teacher lives in the house just left of the one where the person who keeps the horse lives.
9. The baker lives in the white house.
10. The German lives in the white house.
11. The pilot lives in house 2.
12. Whoever lives in the red house lives in house 2.
13. The fish owner and whoever lives in the purple house live two houses apart.
14. The owner of the cat lives next to the farmer.

## Puzzle plain:zebra-00091

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, tea
- nationality: Dane, Swede, Brit, German, Norwegian
- job: teacher, farmer, lawyer, pilot, doctor
- pet: rabbit, cat, fish, dog, horse

Clues:
1. The pilot lives in house 2.
2. The water drinker either works as the farmer or works as the lawyer.
3. The person who drinks juice lives immediately to the right of the tea drinker.
4. The person who keeps the fish is the German.
5. The Dane and the tea drinker are neighbours.
6. The farmer is the Brit.
7. The water drinker and the German are different people.
8. The Norwegian lives directly to the left of the milk drinker.
9. The owner of the horse lives in one of the two end houses.
10. The Brit lives somewhere to the right of the person who keeps the fish.
11. The owner of the rabbit either drinks tea or drinks water.
12. The water drinker lives directly to the left of the coffee drinker.
13. The Dane lives somewhere to the left of the person who keeps the dog.
14. The juice drinker works as the teacher.

## Puzzle paraphrase:zebra-00114

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, rabbit, horse
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- drink: coffee, tea, water, cocoa, juice
- job: lawyer, baker, farmer, teacher, doctor

Clues:
1. The cocoa drinker lives right beside the Spaniard.
2. The water drinker lives in a lower-numbered house than the tea drinker.
3. The fish keeper drinks cocoa.
4. The cocoa drinker is not next door to the juice drinker.
5. The Brit does not live next to the cat owner.
6. The Dane and the Spaniard have exactly one house between them.
7. The bird owner lives next door to the farmer.
8. The Dane lives immediately to the right of the Norwegian.
9. The horse keeper lives directly to the left of the doctor.
10. The Swede drinks water.
11. The lawyer keeps either the bird or the horse.
12. The cat lives in the fifth house.
13. The cocoa drinker is the teacher.
14. The Brit lives right beside the farmer.
15. The tea drinker is the farmer.

## Puzzle paraphrase:zebra-00181

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Swede, Spaniard
- color: white, green, yellow, blue, purple
- job: doctor, baker, farmer, teacher, lawyer
- pet: cat, dog, rabbit, horse, fish

Clues:
1. The blue house and the dog owner's house are neighbours.
2. The doctor lives in the yellow house.
3. The Norwegian has the rabbit.
4. The doctor is not in house 5.
5. The Dane occupies house 2.
6. The green house is where the horse is kept.
7. The farmer lives next door to the Norwegian.
8. The dog belongs to whoever lives in the purple house.
9. The horse lives in house 3.
10. The lawyer's house is immediately to the right of the blue house.
11. The Spaniard occupies house 4.
12. The Swede lives immediately to the left of the baker.
13. The fish owner lives next door to the Norwegian.

## Puzzle plain:zebra-00060

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, dog, fish, rabbit
- drink: coffee, tea, juice, water, cocoa
- hobby: hiking, tennis, chess, painting, golf
- color: blue, red, white, purple, green

Clues:
1. The person in the purple house lives in the house just left of the one where whoever lives in the red house lives.
2. The person who enjoys hiking and the juice drinker are neighbours.
3. The person in the green house and the person who enjoys tennis are neighbours.
4. The water drinker either keeps the fish or keeps the rabbit.
5. The person in the blue house keeps the rabbit.
6. The owner of the fish enjoys golf.
7. The coffee drinker either keeps the cat or keeps the rabbit.
8. The person who drinks tea lives in the purple house.
9. There is exactly one house between the cat owner and the occupant of the red house.
10. The person in the purple house lives in the third house.
11. The person who drinks water and whoever lives in the white house live in adjacent houses.
12. The owner of the dog and the painting enthusiast live two houses apart.
13. The person who drinks coffee enjoys chess.

## Puzzle paraphrase:zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The occupant of the yellow house is the doctor.
2. The German is not a neighbour of the pilot.
3. The cat owner lives in either the blue house or the white house.
4. Two houses separate the red house from the yellow house.
5. The dog owner lives immediately to the left of the yellow house's occupant.
6. The bird owner lives somewhere to the left of the Dane.
7. The lawyer and the occupant of the white house have exactly one house between them.
8. The fish owner lives immediately to the right of the teacher.
9. One house lies between the Brit and the pilot.
10. The lawyer and the Norwegian have exactly one house between them.
11. The Brit and the Dane do not live next to each other.
12. The rabbit owner lives in house 2.
13. Immediately to the right of the Norwegian is the purple house.
