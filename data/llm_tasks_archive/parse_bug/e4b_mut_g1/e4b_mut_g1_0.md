# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 6-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose 2 variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 6
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_mut_g1\e4b_mut_g1_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g1-03

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Formal clues (with their English text):
1. at(yellow, 3)   "The occupant of the yellow house lives in house 3."
2. next_to(dane, dog)   "The Dane and the owner of the dog live in adjacent houses."
3. not_next_to(green, tennis)   "Whoever lives in the green house does not live next to the tennis enthusiast."
4. gap2(cooking, white)   "There is exactly one house between the person who enjoys cooking and the person in the white house."
5. before(german, fish)   "The German lives in a lower-numbered house than the owner of the fish."
6. left_of(golf, chess)   "The person who enjoys golf lives directly to the left of the chess enthusiast."
7. left_of(white, juice)   "The juice drinker lives immediately to the right of the occupant of the white house."
8. same(baker, dog)   "The person who keeps the dog works as the baker."
9. left_of(farmer, lawyer)   "The lawyer lives immediately to the right of the farmer."
10. gap2(cocoa, milk)   "The cocoa drinker and the person who drinks milk live two houses apart."
11. same(cat, red)   "The owner of the cat lives in the red house."
12. left_of(cat, teacher)   "The teacher lives immediately to the right of the owner of the cat."
13. before(golf, cooking)   "The person who enjoys golf lives in a lower-numbered house than the person who enjoys cooking."
14. same(doctor, fish)   "The doctor keeps the fish."
15. next_to(cat, tea)   "The cat owner and the tea drinker live in adjacent houses."
16. same(golf, purple)   "The person in the purple house enjoys golf."
17. gap2(horse, milk)   "There is exactly one house between the horse owner and the milk drinker."
18. left_of(dog, doctor)   "The person who keeps the dog lives in the house just left of the one where the doctor lives."
19. same(dog, water)   "The dog owner drinks water."
20. end(blue)   "The person in the blue house lives at one end of the row."
21. same(rabbit, swede)   "The Swede keeps the rabbit."
22. left_of(doctor, hiking)   "The doctor lives directly to the left of the hiking enthusiast."
23. same(green, lawyer)   "The person in the green house works as the lawyer."
24. next_to(green, norwegian)   "The occupant of the green house lives next to the Norwegian."
25. at(brit, 1)   "The Brit lives in the first house."

Solution: house 1: bird, brit, coffee, farmer, golf, purple; house 2: chess, cocoa, german, green, horse, lawyer; house 3: baker, dog, norwegian, painting, water, yellow; house 4: dane, doctor, fish, milk, tennis, white; house 5: cat, hiking, juice, pilot, red, spaniard; house 6: blue, cooking, rabbit, swede, tea, teacher
Solver mistakes: baker (put in house ?, correct 3); bird (put in house ?, correct 1); blue (put in house ?, correct 6); brit (put in house ?, correct 1); cat (put in house ?, correct 5); chess (put in house ?, correct 2); cocoa (put in house ?, correct 2); coffee (put in house ?, correct 1); cooking (put in house ?, correct 6); dane (put in house ?, correct 4); doctor (put in house ?, correct 4); dog (put in house ?, correct 3); farmer (put in house ?, correct 1); fish (put in house ?, correct 4); german (put in house ?, correct 2); golf (put in house ?, correct 1); green (put in house ?, correct 2); hiking (put in house ?, correct 5); horse (put in house ?, correct 2); juice (put in house ?, correct 5); lawyer (put in house ?, correct 2); milk (put in house ?, correct 4); norwegian (put in house ?, correct 3); painting (put in house ?, correct 3); pilot (put in house ?, correct 5); purple (put in house ?, correct 1); rabbit (put in house ?, correct 6); red (put in house ?, correct 5); spaniard (put in house ?, correct 5); swede (put in house ?, correct 6); tea (put in house ?, correct 6); teacher (put in house ?, correct 6); tennis (put in house ?, correct 4); water (put in house ?, correct 3); white (put in house ?, correct 4); yellow (put in house ?, correct 3)
Solver cell accuracy so far: 0.00

## Puzzle e4b-g1-02

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Formal clues (with their English text):
1. or(horse, cocoa, water)   "The horse owner either drinks cocoa or drinks water."
2. left_of(farmer, lawyer)   "The farmer lives in the house just left of the one where the lawyer lives."
3. not_next_to(green, tennis)   "The occupant of the green house and the person who enjoys tennis are not neighbours."
4. same(green, lawyer)   "The person in the green house works as the lawyer."
5. next_to(dane, dog)   "The Dane and the owner of the dog are neighbours."
6. gap2(cooking, white)   "There is exactly one house between the person who enjoys cooking and whoever lives in the white house."
7. gap2(horse, milk)   "There is exactly one house between the person who keeps the horse and the milk drinker."
8. left_of(doctor, hiking)   "The person who enjoys hiking lives immediately to the right of the doctor."
9. left_of(cat, teacher)   "The cat owner lives in the house just left of the one where the teacher lives."
10. same(baker, dog)   "The baker keeps the dog."
11. left_of(dog, doctor)   "The doctor lives immediately to the right of the dog owner."
12. same(dog, water)   "The person who drinks water keeps the dog."
13. left_of(golf, chess)   "The person who enjoys golf lives directly to the left of the person who enjoys chess."
14. at(blue, 6)   "The person in the blue house lives in house 6."
15. gap2(cocoa, milk)   "The person who drinks cocoa and the person who drinks milk live two houses apart."
16. next_to(cat, tea)   "The owner of the cat and the tea drinker are neighbours."
17. next_to(green, norwegian)   "Whoever lives in the green house and the Norwegian are neighbours."
18. end(golf)   "The golf enthusiast lives at one end of the row."
19. before(german, fish)   "The fish owner lives somewhere to the right of the German."
20. left_of(white, juice)   "The occupant of the white house lives directly to the left of the juice drinker."
21. same(water, yellow)   "The person who drinks water lives in the yellow house."
22. at(bird, 1)   "The person who keeps the bird lives in the leftmost house."
23. same(doctor, fish)   "The fish owner works as the doctor."
24. same(cat, red)   "The cat owner lives in the red house."
25. same(rabbit, swede)   "The owner of the rabbit is the Swede."
26. not_next_to(yellow, blue)   "The person in the yellow house and the person in the blue house are not neighbours."
27. end(brit)   "The Brit lives at one end of the row."

Solution: house 1: bird, brit, coffee, farmer, golf, purple; house 2: chess, cocoa, german, green, horse, lawyer; house 3: baker, dog, norwegian, painting, water, yellow; house 4: dane, doctor, fish, milk, tennis, white; house 5: cat, hiking, juice, pilot, red, spaniard; house 6: blue, cooking, rabbit, swede, tea, teacher
Solver mistakes: baker (put in house ?, correct 3); bird (put in house ?, correct 1); blue (put in house ?, correct 6); brit (put in house ?, correct 1); cat (put in house ?, correct 5); chess (put in house ?, correct 2); cocoa (put in house ?, correct 2); coffee (put in house ?, correct 1); cooking (put in house ?, correct 6); dane (put in house ?, correct 4); doctor (put in house ?, correct 4); dog (put in house ?, correct 3); farmer (put in house ?, correct 1); fish (put in house ?, correct 4); german (put in house ?, correct 2); golf (put in house ?, correct 1); green (put in house ?, correct 2); hiking (put in house ?, correct 5); horse (put in house ?, correct 2); juice (put in house ?, correct 5); lawyer (put in house ?, correct 2); milk (put in house ?, correct 4); norwegian (put in house ?, correct 3); painting (put in house ?, correct 3); pilot (put in house ?, correct 5); purple (put in house ?, correct 1); rabbit (put in house ?, correct 6); red (put in house ?, correct 5); spaniard (put in house ?, correct 5); swede (put in house ?, correct 6); tea (put in house ?, correct 6); teacher (put in house ?, correct 6); tennis (put in house ?, correct 4); water (put in house ?, correct 3); white (put in house ?, correct 4); yellow (put in house ?, correct 3)
Solver cell accuracy so far: 0.00

## Puzzle e4b-g1-12

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Formal clues (with their English text):
1. same(dog, german)   "The person who keeps the dog is the German."
2. left_of(water, white)   "The person who drinks water lives in the house just left of the one where whoever lives in the white house lives."
3. same(brit, white)   "The Brit lives in the white house."
4. before(golf, tennis)   "The golf enthusiast lives somewhere to the left of the tennis enthusiast."
5. next_to(coffee, norwegian)   "The coffee drinker and the Norwegian are neighbours."
6. left_of(green, teacher)   "The teacher lives immediately to the right of the occupant of the green house."
7. left_of(dane, farmer)   "The Dane lives directly to the left of the farmer."
8. gap2(cooking, yellow)   "There is exactly one house between the person who enjoys cooking and the occupant of the yellow house."
9. gap2(cocoa, spaniard)   "The person who drinks cocoa and the Spaniard live two houses apart."
10. same(juice, white)   "The juice drinker lives in the white house."
11. not_at(chess, 1)   "The chess enthusiast does not live in house 1."
12. same(spaniard, tennis)   "The Spaniard enjoys tennis."
13. same(doctor, red)   "The doctor lives in the red house."
14. same(horse, purple)   "Whoever lives in the purple house keeps the horse."
15. left_of(brit, blue)   "The Brit lives in the house just left of the one where the person in the blue house lives."
16. at(bird, 2)   "The owner of the bird lives in house 2."
17. left_of(rabbit, tennis)   "The owner of the rabbit lives in the house just left of the one where the tennis enthusiast lives."
18. same(golf, swede)   "The Swede enjoys golf."
19. not_same(dane, milk)   "The person who drinks milk is not the Dane."
20. before(teacher, painting)   "The teacher lives somewhere to the left of the painting enthusiast."
21. not_next_to(bird, fish)   "The person who keeps the bird does not live next to the fish owner."
22. next_to(doctor, tennis)   "The doctor and the tennis enthusiast are neighbours."
23. or(golf, farmer, pilot)   "The person who enjoys golf either works as the farmer or works as the pilot."
24. same(baker, green)   "The person in the green house works as the baker."
25. at(farmer, 5)   "The farmer lives in the fifth house."
26. left_of(tennis, cooking)   "The person who enjoys tennis lives directly to the left of the cooking enthusiast."
27. same(teacher, white)   "The teacher lives in the white house."

Solution: house 1: baker, dog, german, green, hiking, water; house 2: bird, brit, chess, juice, teacher, white; house 3: blue, cat, cocoa, golf, pilot, swede; house 4: dane, lawyer, painting, rabbit, tea, yellow; house 5: coffee, farmer, horse, purple, spaniard, tennis; house 6: cooking, doctor, fish, milk, norwegian, red
Solver mistakes: baker (put in house ?, correct 1); bird (put in house ?, correct 2); blue (put in house ?, correct 3); brit (put in house ?, correct 2); cat (put in house ?, correct 3); chess (put in house ?, correct 2); cocoa (put in house ?, correct 3); coffee (put in house ?, correct 5); cooking (put in house ?, correct 6); dane (put in house ?, correct 4); doctor (put in house ?, correct 6); dog (put in house ?, correct 1); farmer (put in house ?, correct 5); fish (put in house ?, correct 6); german (put in house ?, correct 1); golf (put in house ?, correct 3); green (put in house ?, correct 1); hiking (put in house ?, correct 1); horse (put in house ?, correct 5); juice (put in house ?, correct 2); lawyer (put in house ?, correct 4); milk (put in house ?, correct 6); norwegian (put in house ?, correct 6); painting (put in house ?, correct 4); pilot (put in house ?, correct 3); purple (put in house ?, correct 5); rabbit (put in house ?, correct 4); red (put in house ?, correct 6); spaniard (put in house ?, correct 5); swede (put in house ?, correct 3); tea (put in house ?, correct 4); teacher (put in house ?, correct 2); tennis (put in house ?, correct 5); water (put in house ?, correct 1); white (put in house ?, correct 2); yellow (put in house ?, correct 4)
Solver cell accuracy so far: 0.00

## Puzzle e4b-g0-02

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Formal clues (with their English text):
1. gap2(dane, norwegian)   "The Dane and the Norwegian live two houses apart."
2. not_same(golf, yellow)   "The person who enjoys golf does not live in the yellow house."
3. gap2(baker, tea)   "There is exactly one house between the baker and the tea drinker."
4. at(water, 1)   "The water drinker lives in the first house."
5. before(german, hiking)   "The German lives somewhere to the left of the hiking enthusiast."
6. gap2(brit, purple)   "The Brit and the person in the purple house live two houses apart."
7. same(blue, spaniard)   "The person in the blue house is the Spaniard."
8. left_of(tennis, doctor)   "The person who enjoys tennis lives directly to the left of the doctor."
9. or(cooking, baker, lawyer)   "The cooking enthusiast either works as the baker or works as the lawyer."
10. before(milk, hiking)   "The person who drinks milk lives somewhere to the left of the hiking enthusiast."
11. or(farmer, purple, red)   "The farmer either lives in the purple house or lives in the red house."
12. same(chess, horse)   "The person who keeps the horse enjoys chess."
13. or(cocoa, chess, painting)   "The cocoa drinker either enjoys chess or enjoys painting."
14. same(lawyer, swede)   "The lawyer is the Swede."
15. at(pilot, 4)   "The pilot lives in house 4."
16. left_of(white, golf)   "The occupant of the white house lives directly to the left of the golf enthusiast."
17. at(red, 1)   "The occupant of the red house lives in house 1."
18. same(chess, green)   "The occupant of the green house enjoys chess."
19. same(juice, white)   "The juice drinker lives in the white house."
20. or(fish, spaniard, swede)   "The owner of the fish either is the Spaniard or is the Swede."
21. at(spaniard, 2)   "The Spaniard lives in house 2."
22. same(dog, yellow)   "The owner of the dog lives in the yellow house."
23. same(dane, pilot)   "The pilot is the Dane."
24. not_next_to(cat, coffee)   "The owner of the cat and the person who drinks coffee are not neighbours."
25. same(bird, milk)   "The person who keeps the bird drinks milk."

Solution: house 1: cat, farmer, german, red, tennis, water; house 2: bird, blue, doctor, milk, painting, spaniard; house 3: baker, brit, coffee, cooking, dog, yellow; house 4: dane, hiking, juice, pilot, rabbit, white; house 5: fish, golf, lawyer, purple, swede, tea; house 6: chess, cocoa, green, horse, norwegian, teacher
Solver mistakes: baker (put in house ?, correct 3); bird (put in house ?, correct 2); blue (put in house ?, correct 2); brit (put in house ?, correct 3); cat (put in house ?, correct 1); chess (put in house ?, correct 6); cocoa (put in house ?, correct 6); coffee (put in house ?, correct 3); cooking (put in house ?, correct 3); dane (put in house ?, correct 4); doctor (put in house ?, correct 2); dog (put in house ?, correct 3); farmer (put in house ?, correct 1); fish (put in house ?, correct 5); german (put in house ?, correct 1); golf (put in house ?, correct 5); green (put in house ?, correct 6); hiking (put in house ?, correct 4); horse (put in house ?, correct 6); juice (put in house ?, correct 4); lawyer (put in house ?, correct 5); milk (put in house ?, correct 2); norwegian (put in house ?, correct 6); painting (put in house ?, correct 2); pilot (put in house ?, correct 4); purple (put in house ?, correct 5); rabbit (put in house ?, correct 4); red (put in house ?, correct 1); spaniard (put in house ?, correct 2); swede (put in house ?, correct 5); tea (put in house ?, correct 5); teacher (put in house ?, correct 6); tennis (put in house ?, correct 1); water (put in house ?, correct 1); white (put in house ?, correct 4); yellow (put in house ?, correct 3)
Solver cell accuracy so far: 0.50

## Puzzle e4b-g0-00

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, juice, coffee
- color: white, green, purple, yellow, red, blue
- pet: dog, cat, bird, rabbit, horse, fish
- hobby: chess, hiking, tennis, cooking, painting, golf
- job: farmer, lawyer, pilot, baker, doctor, teacher
- nationality: German, Norwegian, Brit, Swede, Spaniard, Dane

Formal clues (with their English text):
1. same(cocoa, tennis)   "The person who enjoys tennis drinks cocoa."
2. or(doctor, brit, norwegian)   "The doctor either is the Brit or is the Norwegian."
3. left_of(hiking, golf)   "The person who enjoys hiking lives in the house just left of the one where the person who enjoys golf lives."
4. gap2(german, swede)   "There is exactly one house between the German and the Swede."
5. same(hiking, pilot)   "The person who enjoys hiking works as the pilot."
6. at(cat, 2)   "The person who keeps the cat lives in the second house."
7. gap2(water, yellow)   "There is exactly one house between the person who drinks water and whoever lives in the yellow house."
8. same(teacher, tennis)   "The teacher enjoys tennis."
9. next_to(chess, juice)   "The person who enjoys chess lives next to the juice drinker."
10. or(dog, farmer, pilot)   "The owner of the dog either works as the farmer or works as the pilot."
11. left_of(red, blue)   "Whoever lives in the red house lives in the house just left of the one where the occupant of the blue house lives."
12. or(white, doctor, lawyer)   "The person in the white house either works as the doctor or works as the lawyer."
13. same(coffee, swede)   "The Swede drinks coffee."
14. gap2(cat, lawyer)   "There is exactly one house between the person who keeps the cat and the lawyer."
15. same(blue, teacher)   "The teacher lives in the blue house."
16. same(baker, golf)   "The person who enjoys golf works as the baker."
17. same(pilot, swede)   "The pilot is the Swede."
18. not_at(spaniard, 6)   "The Spaniard does not live in house 6."
19. same(cooking, horse)   "The person who enjoys cooking keeps the horse."
20. next_to(cooking, water)   "The person who enjoys cooking lives next to the water drinker."
21. same(cat, purple)   "The owner of the cat lives in the purple house."
22. same(brit, chess)   "The chess enthusiast is the Brit."
23. not_same(fish, painting)   "The person who enjoys painting does not keep the fish."
24. end(white)   "Whoever lives in the white house lives at one end of the row."
25. left_of(cat, bird)   "The bird owner lives immediately to the right of the cat owner."
26. before(tea, milk)   "The tea drinker lives in a lower-numbered house than the person who drinks milk."

Solution: house 1: doctor, norwegian, painting, rabbit, tea, white; house 2: cat, coffee, hiking, pilot, purple, swede; house 3: baker, bird, golf, milk, spaniard, yellow; house 4: cooking, german, green, horse, juice, lawyer; house 5: brit, chess, dog, farmer, red, water; house 6: blue, cocoa, dane, fish, teacher, tennis
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 0.50
