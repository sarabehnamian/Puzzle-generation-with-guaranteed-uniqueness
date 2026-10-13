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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_016.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00053

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, cooking, painting, hiking, tennis
- job: lawyer, pilot, teacher, doctor, baker
- color: blue, purple, green, yellow, red
- pet: horse, bird, fish, rabbit, cat

Clues:
1. The chess enthusiast and the pilot are one and the same person.
2. The person who keeps the cat does not live to the right of the rabbit owner.
3. None of the neighbours of the doctor works as the teacher.
4. The right-hand neighbour of the doctor enjoys cooking.
5. The left-hand neighbour of the person who enjoys painting works as the teacher.
6. Whoever lives in the blue house lives two doors away from the person who keeps the horse.
7. The tennis enthusiast lives somewhere between the person who keeps the rabbit and whoever lives in the yellow house.
8. The person who enjoys chess and the occupant of the red house are one and the same person.
9. The owner of the bird and the person who enjoys hiking are one and the same person.
10. Exactly one house separates whoever lives in the purple house from whoever lives in the red house.
11. Whoever lives in the blue house is not the same person as the owner of the cat.
12. Exactly 1 house lies to the left of the home of the person in the blue house.
13. Whoever lives in the purple house lives two doors away from the teacher.
14. At least one house separates the lawyer from the person who enjoys chess.

## Puzzle plain:zebra-00073

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, tea
- nationality: Norwegian, Swede, Dane, Spaniard, Brit
- hobby: tennis, cooking, painting, chess, hiking
- job: teacher, lawyer, baker, doctor, farmer

Clues:
1. The Norwegian and the Spaniard live two houses apart.
2. The doctor and the Swede live in adjacent houses.
3. The cooking enthusiast lives next to the person who drinks tea.
4. There is exactly one house between the Dane and the person who drinks water.
5. The baker and the hiking enthusiast live two houses apart.
6. The Brit works as the baker.
7. The person who enjoys tennis lives directly to the left of the juice drinker.
8. The Swede and the teacher live two houses apart.
9. The farmer lives in house 4.
10. The Brit lives directly to the left of the Spaniard.
11. The milk drinker enjoys painting.
12. The person who enjoys painting lives in house 5.

## Puzzle paraphrase:zebra-00163

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, baker, farmer
- pet: bird, horse, dog, rabbit, fish
- hobby: painting, hiking, golf, tennis, chess
- drink: cocoa, water, tea, juice, coffee

Clues:
1. The chess player lives somewhere to the left of the golfer.
2. The golfer does not live next door to the water drinker.
3. The doctor's hobby is hiking.
4. Chess is the hobby of the cocoa drinker.
5. The last house belongs to the rabbit owner.
6. The horse is kept at one end of the row.
7. The chess player does not own the fish.
8. The chess player lives right beside the farmer.
9. The hiker and the horse owner live two doors apart.
10. The juice drinker lives immediately to the left of the lawyer.
11. The baker and the doctor are not next-door neighbours.
12. The water drinker lives at one of the ends of the row.
13. The dog owner lives in the middle house.
14. The horse owner lives directly to the left of the chess player.
15. The tennis player is the baker.
16. The coffee drinker and the doctor are separated by exactly one house.

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

## Puzzle hard:zebra_hard-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, lawyer, teacher, doctor
- pet: dog, fish, rabbit, cat, horse
- drink: coffee, milk, water, juice, tea
- nationality: Swede, Spaniard, Brit, Dane, German

Clues:
1. The lawyer and the water drinker are one and the same person.
2. The person who keeps the horse and the pilot are one and the same person.
3. The Brit and the farmer are one and the same person.
4. One of the neighbours of the teacher keeps the horse.
5. The lawyer and the Swede are one and the same person.
6. The right-hand neighbour of the person who keeps the dog keeps the rabbit.
7. One of the neighbours of the lawyer is the Spaniard.
8. One of the neighbours of the owner of the dog drinks coffee.
9. The person who keeps the cat and the coffee drinker are one and the same person.
10. One of the neighbours of the person who keeps the horse drinks coffee.
11. The farmer lives in the third house from the right.
12. The Dane and the person who drinks tea are one and the same person.
13. The pilot lives somewhere between the person who drinks juice and the person who keeps the rabbit.
14. The person who drinks milk does not live in the rightmost house.

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

## Puzzle plain:zebra-00027

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, tennis, cooking
- nationality: Dane, German, Spaniard, Norwegian, Brit
- color: green, purple, white, yellow, red
- drink: tea, milk, water, cocoa, coffee

Clues:
1. The coffee drinker and the person in the red house are neighbours.
2. The chess enthusiast lives somewhere to the right of whoever lives in the white house.
3. The occupant of the red house lives in the house just left of the one where the cocoa drinker lives.
4. The person who drinks water lives immediately to the right of the person who enjoys hiking.
5. The person in the purple house lives in the fourth house.
6. The person who enjoys painting is the Spaniard.
7. The Dane lives in the leftmost house.
8. Whoever lives in the purple house and the tea drinker are not neighbours.
9. The Brit lives in the house just left of the one where the Spaniard lives.
10. The person who enjoys tennis lives in the house just left of the one where the occupant of the purple house lives.
11. The person who enjoys hiking lives in the house just left of the one where the Norwegian lives.
12. The tennis enthusiast lives next to the occupant of the yellow house.

## Puzzle paraphrase:zebra-00139

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, purple, red, white, blue
- pet: bird, rabbit, dog, horse, cat
- hobby: golf, chess, painting, tennis, cooking
- nationality: Brit, Spaniard, Dane, Norwegian, Swede

Clues:
1. The blue house's occupant is either the Brit or the Spaniard.
2. The Spaniard is the tennis enthusiast.
3. The dog owner lives immediately to the right of the white house.
4. The Brit is the horse owner.
5. The white house is directly to the left of the cooking enthusiast.
6. The Norwegian lives directly to the left of the chess player.
7. The Norwegian and the Spaniard live in adjacent houses.
8. The bird owner and the yellow house are neighbours.
9. The Norwegian and the red house are next-door neighbours.
10. The cooking enthusiast lives immediately to the left of the Dane.
11. The painting enthusiast lives somewhere to the right of the rabbit owner.
12. The cooking enthusiast lives somewhere to the right of the yellow house.
13. The rabbit owner lives in a lower-numbered house than the cooking enthusiast.

## Puzzle hard:zebra_hard-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, German, Norwegian, Spaniard
- pet: fish, dog, cat, horse, bird
- job: farmer, lawyer, baker, doctor, teacher
- drink: coffee, milk, juice, water, tea

Clues:
1. The tea drinker lives in the fourth house from the right.
2. The owner of the fish lives in the fifth house from the right.
3. The right-hand neighbour of the owner of the horse drinks water.
4. The baker and the Swede are one and the same person.
5. The left-hand neighbour of the person who drinks coffee works as the lawyer.
6. One of the neighbours of the owner of the cat works as the lawyer.
7. The left-hand neighbour of the milk drinker is the Brit.
8. The Norwegian lives in the rightmost house.
9. The baker does not live to the right of the doctor.
10. Exactly 1 house lies to the left of the home of the person who keeps the dog.
11. The Spaniard is not the same person as the tea drinker.
12. The left-hand neighbour of the person who keeps the horse works as the doctor.
13. If the water drinker is not the baker, then that person works as the teacher.
