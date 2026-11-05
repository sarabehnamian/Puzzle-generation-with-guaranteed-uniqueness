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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_006.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00042

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, farmer, baker, teacher
- nationality: Spaniard, Swede, Norwegian, Brit, German
- pet: bird, dog, horse, cat, rabbit
- color: blue, yellow, red, purple, white

Clues:
1. If the bird owner is not the doctor, then that person works as the teacher.
2. One of the neighbours of the baker is the Brit.
3. The person who keeps the bird and the occupant of the blue house are one and the same person.
4. The person in the red house lives two doors away from the Spaniard.
5. The owner of the cat lives in the second house from the right.
6. One of the neighbours of the person who keeps the rabbit works as the doctor.
7. The teacher lives in the fourth house from the right.
8. The right-hand neighbour of the cat owner works as the farmer.
9. The right-hand neighbour of whoever lives in the yellow house works as the lawyer.
10. The right-hand neighbour of the horse owner is the Norwegian.
11. The owner of the dog and the German are one and the same person.
12. One of the neighbours of the person who keeps the bird lives in the white house.

## Puzzle paraphrase:zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two houses apart.
2. The purple house is directly to the left of the tea drinker.
3. The coffee drinker lives next door to the dog owner.
4. The juice drinker and the white house's occupant live in adjacent houses.
5. The milk drinker lives in one of the two end houses.
6. The purple house is immediately to the right of the white house.
7. The coffee drinker keeps the bird.
8. The dog owner lives in the purple house.
9. The baker keeps the cat.
10. The doctor lives next door to the dog owner.
11. Exactly one house lies between the green house and the red house.
12. The farmer lives directly to the left of the purple house.
13. The green house is the middle house.
14. The green house and the horse owner are two houses apart.

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

## Puzzle hard:zebra_hard-00040

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, fish, horse, dog
- job: pilot, lawyer, baker, doctor, teacher
- nationality: Brit, Dane, German, Norwegian, Swede
- color: red, white, blue, yellow, purple

Clues:
1. The right-hand neighbour of the teacher keeps the rabbit.
2. The Dane lives two doors away from the Swede.
3. The baker lives somewhere between the Brit and the pilot.
4. The Norwegian and the teacher are one and the same person.
5. The right-hand neighbour of the Dane keeps the dog.
6. The German and the person in the purple house are one and the same person.
7. If the fish owner does not live in the purple house, then that person lives in the white house.
8. Exactly one house separates the Brit from the Norwegian.
9. The right-hand neighbour of the Swede lives in the red house.
10. The lawyer has only one neighbour.
11. The owner of the cat lives further to the right than whoever lives in the white house.
12. The teacher and the person in the white house are one and the same person.
13. One of the neighbours of whoever lives in the red house works as the doctor.
14. The left-hand neighbour of the person in the blue house lives in the white house.

## Puzzle plain:zebra-00062

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, German, Norwegian, Brit
- color: yellow, purple, white, green, red
- pet: dog, cat, horse, rabbit, fish
- drink: juice, water, tea, milk, coffee

Clues:
1. The German lives in the house just left of the one where the occupant of the red house lives.
2. The occupant of the purple house drinks tea.
3. The person who drinks coffee and the German live two houses apart.
4. The owner of the dog and whoever lives in the white house are neighbours.
5. The juice drinker lives directly to the left of the dog owner.
6. The coffee drinker keeps the dog.
7. The person who drinks water lives in the fourth house.
8. The rabbit owner lives in the first house.
9. The cat owner lives in the red house.
10. There is exactly one house between the Brit and the cat owner.
11. The owner of the cat is the Swede.
12. The occupant of the green house and the Norwegian live two houses apart.
13. The person in the purple house keeps the horse.
14. The person who drinks coffee and the Norwegian are different people.

## Puzzle paraphrase:zebra-00139

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, purple, red, white, blue
- pet: bird, rabbit, dog, horse, cat
- hobby: golf, chess, painting, tennis, cooking
- nationality: Brit, Spaniard, Dane, Norwegian, Swede

Clues:
1. The blue house's occupant is either the Brit or the Spaniard.
2. The Spaniard's hobby is tennis.
3. The dog owner lives directly to the right of the white house.
4. The Brit owns the horse.
5. The white house is directly to the left of the cooking enthusiast.
6. The Norwegian lives immediately to the left of the chess enthusiast.
7. The Norwegian and the Spaniard live in adjacent houses.
8. The bird owner and the yellow house are neighbours.
9. The Norwegian lives next door to the red house.
10. The cooking enthusiast lives immediately to the left of the Dane.
11. The painting enthusiast lives somewhere to the right of the rabbit owner.
12. The cooking enthusiast lives somewhere to the right of the yellow house.
13. The rabbit owner lives in a lower-numbered house than the cooking enthusiast.

## Puzzle hard:zebra_hard-00052

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, red, purple, white
- hobby: tennis, hiking, painting, golf, cooking
- nationality: Brit, Spaniard, Swede, Dane, German
- pet: cat, dog, rabbit, bird, horse

Clues:
1. Exactly one house separates the person who keeps the bird from the person who enjoys tennis.
2. The hiking enthusiast and the Spaniard are one and the same person.
3. The person who keeps the horse lives further to the right than the cooking enthusiast.
4. Whoever lives in the white house lives in the second house from the right.
5. If the person who enjoys tennis is not the Dane, then that person is the Spaniard.
6. Exactly 2 houses lie to the left of the home of the horse owner.
7. The right-hand neighbour of whoever lives in the red house keeps the cat.
8. The person who enjoys hiking and the person who keeps the rabbit are one and the same person.
9. If the German does not live in the purple house, then that person lives in the white house.
10. The occupant of the purple house lives somewhere between the person who enjoys painting and the occupant of the white house.
11. The cat owner and the person who enjoys painting are one and the same person.
12. If the Brit does not live in the blue house, then that person lives in the purple house.

## Puzzle hard:zebra_hard-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, cat, rabbit, dog
- job: baker, doctor, farmer, teacher, pilot
- drink: tea, cocoa, coffee, milk, juice
- hobby: chess, hiking, painting, tennis, golf

Clues:
1. The tea drinker lives somewhere between the fish owner and the tennis enthusiast.
2. Neither the cocoa drinker nor the pilot keeps the dog.
3. One of the neighbours of the person who drinks juice keeps the rabbit.
4. At least one house separates the owner of the horse from the fish owner.
5. If the owner of the dog is not the doctor, then that person works as the teacher.
6. The right-hand neighbour of the person who drinks tea enjoys golf.
7. The person who keeps the fish and the teacher are one and the same person.
8. The fish owner lives somewhere between the baker and the chess enthusiast.
9. The right-hand neighbour of the person who enjoys tennis works as the baker.
10. If the farmer does not enjoy chess, then that person enjoys tennis.
11. Exactly 0 houses lie to the left of the home of the dog owner.
12. The left-hand neighbour of the painting enthusiast enjoys hiking.
13. The left-hand neighbour of the milk drinker keeps the rabbit.

## Puzzle plain:zebra-00066

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, Norwegian, Dane
- job: lawyer, baker, doctor, pilot, farmer
- color: purple, yellow, white, green, blue
- hobby: tennis, painting, chess, cooking, golf

Clues:
1. The lawyer and whoever lives in the white house live in adjacent houses.
2. The farmer lives next to the person in the purple house.
3. The occupant of the yellow house either is the Brit or is the Norwegian.
4. The chess enthusiast lives in the blue house.
5. The golf enthusiast lives next to the person in the white house.
6. The Norwegian lives next to the Swede.
7. The farmer lives in house 2.
8. The baker and the person who enjoys painting live in adjacent houses.
9. The golf enthusiast lives somewhere to the right of whoever lives in the green house.
10. Whoever lives in the yellow house lives directly to the left of the doctor.
11. The person who enjoys cooking and the Dane live two houses apart.
12. The person who enjoys painting and the Spaniard live two houses apart.
13. The cooking enthusiast and the baker are different people.

## Puzzle plain:zebra-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, rabbit, dog
- job: teacher, farmer, pilot, lawyer, baker
- color: purple, green, blue, white, yellow
- nationality: Dane, Brit, Norwegian, Spaniard, German

Clues:
1. The occupant of the white house is the Spaniard.
2. Whoever lives in the blue house and the German live in adjacent houses.
3. The person who keeps the rabbit either lives in the purple house or lives in the white house.
4. The person who keeps the fish and whoever lives in the green house live in adjacent houses.
5. The person who keeps the fish lives somewhere to the right of the Norwegian.
6. The teacher lives somewhere to the left of the person who keeps the horse.
7. The farmer lives next to the Norwegian.
8. The occupant of the white house lives in the house just left of the one where the Dane lives.
9. The person who keeps the horse lives in the house just left of the one where the occupant of the yellow house lives.
10. There is exactly one house between the occupant of the blue house and the Spaniard.
11. The owner of the horse either works as the lawyer or works as the pilot.
12. The farmer keeps the cat.
13. The person in the blue house and the pilot live in adjacent houses.
14. The baker and the Brit live two houses apart.
