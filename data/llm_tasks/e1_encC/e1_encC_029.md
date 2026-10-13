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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_029.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00113

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, baker, farmer, teacher
- drink: tea, milk, juice, water, coffee
- nationality: Swede, German, Norwegian, Spaniard, Brit
- color: red, yellow, purple, white, blue

Clues:
1. The blue house's occupant and the teacher are not neighbours.
2. The doctor lives in the fifth house.
3. The coffee drinker lives directly to the left of the teacher.
4. The blue house's occupant is either the farmer or the lawyer.
5. The juice drinker is not the Norwegian.
6. The white house is house 1.
7. The Swede is not the doctor.
8. The blue house stands right next to the yellow house.
9. The juice drinker and the Spaniard live next door to each other.
10. The Spaniard lives immediately to the left of the purple house's occupant.
11. The lawyer is either the Brit or the Spaniard.
12. Exactly one house lies between the milk drinker and the Norwegian.
13. The baker lives in the white house.
14. The water drinker is the baker.

## Puzzle hard:zebra_hard-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, green, white, yellow, purple
- job: baker, teacher, pilot, lawyer, doctor
- hobby: tennis, hiking, golf, painting, cooking
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The right-hand neighbour of the cat owner enjoys golf.
2. One of the neighbours of the horse owner keeps the dog.
3. The occupant of the red house lives further to the right than the owner of the bird.
4. The owner of the dog is not the same person as whoever lives in the yellow house.
5. Neither the cat owner nor whoever lives in the green house works as the teacher.
6. The lawyer lives somewhere between the occupant of the red house and whoever lives in the white house.
7. If the teacher does not keep the cat, then that person keeps the rabbit.
8. The pilot lives two doors away from the teacher.
9. The cooking enthusiast and the pilot are one and the same person.
10. The painting enthusiast lives somewhere between the horse owner and the person who enjoys tennis.
11. If the person in the purple house is not the doctor, then that person works as the pilot.
12. At least one house separates the owner of the bird from the horse owner.
13. The teacher lives in the fourth house from the right.
14. One of the neighbours of the teacher works as the doctor.
15. One of the neighbours of the lawyer lives in the yellow house.

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

## Puzzle plain:zebra-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, lawyer, farmer, pilot
- nationality: Norwegian, Brit, Swede, German, Spaniard
- drink: milk, cocoa, tea, water, coffee
- color: yellow, purple, red, white, green

Clues:
1. The cocoa drinker lives in the yellow house.
2. The German lives immediately to the right of whoever lives in the yellow house.
3. The person in the green house either is the Brit or is the Norwegian.
4. There is exactly one house between the Swede and the person in the white house.
5. The baker lives somewhere to the left of the pilot.
6. The doctor either drinks coffee or drinks tea.
7. The Swede lives in the second house.
8. The occupant of the purple house drinks tea.
9. The Brit works as the farmer.
10. The person who drinks cocoa lives directly to the left of the lawyer.
11. The cocoa drinker lives somewhere to the left of the Norwegian.
12. The Norwegian works as the doctor.
13. The farmer does not live in the green house.
14. The person who drinks milk is the German.
15. The baker lives next to the lawyer.

## Puzzle hard:zebra_hard-00083

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, German, Dane, Brit
- color: purple, red, yellow, blue, green
- drink: coffee, water, cocoa, tea, milk
- job: teacher, lawyer, baker, doctor, pilot

Clues:
1. The milk drinker and the Swede are one and the same person.
2. If the doctor does not live in the green house, then that person lives in the red house.
3. The right-hand neighbour of the person who drinks water is the Brit.
4. The German lives somewhere between the Swede and the person in the yellow house.
5. The person who drinks cocoa and the person in the green house are one and the same person.
6. The right-hand neighbour of the cocoa drinker lives in the yellow house.
7. The right-hand neighbour of the baker works as the pilot.
8. The coffee drinker lives two doors away from the Spaniard.
9. One of the neighbours of the lawyer lives in the blue house.
10. Exactly 1 house lies to the left of the home of the occupant of the yellow house.
11. At least one house separates the Dane from the baker.
12. The pilot lives somewhere between the doctor and the person in the yellow house.
13. If the pilot is not the German, then that person is the Spaniard.

## Puzzle plain:zebra-00044

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- pet: cat, bird, dog, fish, horse
- drink: milk, cocoa, water, coffee, tea
- color: green, purple, blue, white, yellow

Clues:
1. The person who drinks coffee lives in the third house.
2. The Spaniard either keeps the fish or keeps the horse.
3. The person who keeps the dog and the person who drinks water live in adjacent houses.
4. The person who keeps the dog and the Swede are neighbours.
5. The occupant of the purple house either keeps the fish or keeps the horse.
6. The person in the white house keeps the horse.
7. There is exactly one house between the cocoa drinker and the Dane.
8. The person who keeps the fish lives in the house just left of the one where the cat owner lives.
9. The person who drinks tea lives in the second house.
10. The person in the yellow house lives immediately to the right of the person who keeps the bird.
11. The owner of the cat lives in house 5.
12. The Brit lives in the third house.
13. The owner of the fish lives directly to the left of the person in the green house.

## Puzzle hard:zebra_hard-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, German
- color: yellow, white, green, blue, purple
- hobby: golf, chess, tennis, hiking, cooking
- drink: water, cocoa, tea, juice, milk

Clues:
1. The left-hand neighbour of the golf enthusiast drinks tea.
2. Exactly 2 houses lie to the left of the home of the Brit.
3. The occupant of the blue house and the hiking enthusiast are one and the same person.
4. At least one house separates the person who drinks juice from the German.
5. The person who enjoys chess and the person who drinks tea are one and the same person.
6. Exactly one house separates whoever lives in the purple house from the person who enjoys tennis.
7. The Spaniard lives somewhere between whoever lives in the green house and the person in the yellow house.
8. Exactly one house separates the Swede from the person in the yellow house.
9. The right-hand neighbour of the person in the purple house drinks cocoa.
10. One of the neighbours of the occupant of the white house enjoys cooking.
11. The person who drinks water lives somewhere between whoever lives in the blue house and the person who enjoys golf.
12. The juice drinker and the Norwegian are one and the same person.

## Puzzle paraphrase:zebra-00189

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, teacher, doctor, baker
- hobby: painting, tennis, cooking, hiking, golf
- pet: horse, rabbit, fish, dog, bird
- nationality: German, Dane, Swede, Spaniard, Brit

Clues:
1. The rabbit owner and the tennis enthusiast live two houses apart.
2. The Spaniard is the painting enthusiast.
3. The bird's owner lives immediately to the left of the doctor.
4. The Dane and the farmer live in neighbouring houses.
5. The Spaniard lives immediately to the right of the fish owner.
6. The golf enthusiast lives immediately to the left of the dog owner.
7. The lawyer occupies the fourth house.
8. One house lies between the Swede and the teacher.
9. The German lives immediately to the left of the dog owner.
10. The Swede lives somewhere to the left of the Spaniard.
11. The painting enthusiast does not live in house 5.
12. The Dane and the horse owner live two houses apart.
13. The cooking enthusiast is the farmer.

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
