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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_mut_g0\e4b_mut_g0_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


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
Solver mistakes: baker (put in house ?, correct 3); bird (put in house ?, correct 3); blue (put in house ?, correct 6); brit (put in house ?, correct 5); cat (put in house ?, correct 2); chess (put in house ?, correct 5); cocoa (put in house ?, correct 6); coffee (put in house ?, correct 2); cooking (put in house ?, correct 4); dane (put in house ?, correct 6); doctor (put in house ?, correct 1); dog (put in house ?, correct 5); farmer (put in house ?, correct 5); fish (put in house ?, correct 6); german (put in house ?, correct 4); golf (put in house ?, correct 3); green (put in house ?, correct 4); hiking (put in house ?, correct 2); horse (put in house ?, correct 4); juice (put in house ?, correct 4); lawyer (put in house ?, correct 4); milk (put in house ?, correct 3); norwegian (put in house ?, correct 1); painting (put in house ?, correct 1); pilot (put in house ?, correct 2); purple (put in house ?, correct 2); rabbit (put in house ?, correct 1); red (put in house ?, correct 5); spaniard (put in house ?, correct 3); swede (put in house ?, correct 2); tea (put in house ?, correct 1); teacher (put in house ?, correct 6); tennis (put in house ?, correct 6); water (put in house ?, correct 5); white (put in house ?, correct 1); yellow (put in house ?, correct 3)
Solver cell accuracy so far: 0.00

## Puzzle e4b-g0-01

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Formal clues (with their English text):
1. next_to(green, norwegian)   "The person in the green house lives next to the Norwegian."
2. before(german, fish)   "The German lives somewhere to the left of the person who keeps the fish."
3. same(baker, dog)   "The person who keeps the dog works as the baker."
4. end(golf)   "The person who enjoys golf lives at one end of the row."
5. gap2(cocoa, milk)   "There is exactly one house between the person who drinks cocoa and the milk drinker."
6. left_of(doctor, hiking)   "The hiking enthusiast lives immediately to the right of the doctor."
7. same(green, lawyer)   "The person in the green house works as the lawyer."
8. not_next_to(green, tennis)   "Whoever lives in the green house and the person who enjoys tennis are not neighbours."
9. at(brit, 1)   "The Brit lives in the first house."
10. same(dog, water)   "The person who drinks water keeps the dog."
11. gap2(horse, milk)   "The owner of the horse and the milk drinker live two houses apart."
12. same(rabbit, swede)   "The Swede keeps the rabbit."
13. at(blue, 6)   "Whoever lives in the blue house lives in the last house."
14. next_to(cat, tea)   "The cat owner and the tea drinker live in adjacent houses."
15. left_of(golf, chess)   "The person who enjoys golf lives directly to the left of the person who enjoys chess."
16. left_of(cat, teacher)   "The teacher lives immediately to the right of the cat owner."
17. same(doctor, fish)   "The owner of the fish works as the doctor."
18. left_of(farmer, lawyer)   "The lawyer lives immediately to the right of the farmer."
19. next_to(dane, dog)   "The Dane lives next to the dog owner."
20. left_of(white, juice)   "Whoever lives in the white house lives in the house just left of the one where the person who drinks juice lives."
21. same(cat, red)   "The person in the red house keeps the cat."
22. at(yellow, 3)   "The person in the yellow house lives in house 3."
23. left_of(dog, doctor)   "The owner of the dog lives in the house just left of the one where the doctor lives."
24. gap2(cooking, white)   "There is exactly one house between the cooking enthusiast and the occupant of the white house."

Solution: house 1: bird, brit, coffee, farmer, golf, purple; house 2: chess, cocoa, german, green, horse, lawyer; house 3: baker, dog, norwegian, painting, water, yellow; house 4: dane, doctor, fish, milk, tennis, white; house 5: cat, hiking, juice, pilot, red, spaniard; house 6: blue, cooking, rabbit, swede, tea, teacher
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-03

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Formal clues (with their English text):
1. left_of(baker, milk)   "The milk drinker lives immediately to the right of the baker."
2. at(dane, 3)   "The Dane lives in the third house."
3. same(cooking, german)   "The person who enjoys cooking is the German."
4. same(brit, white)   "The occupant of the white house is the Brit."
5. same(dog, water)   "The owner of the dog drinks water."
6. next_to(fish, horse)   "The owner of the fish and the person who keeps the horse are neighbours."
7. at(cocoa, 5)   "The cocoa drinker lives in the fifth house."
8. next_to(chess, doctor)   "The chess enthusiast lives next to the doctor."
9. left_of(teacher, blue)   "Whoever lives in the blue house lives immediately to the right of the teacher."
10. or(lawyer, milk, water)   "The lawyer either drinks milk or drinks water."
11. or(juice, horse, rabbit)   "The person who drinks juice either keeps the horse or keeps the rabbit."
12. left_of(blue, brit)   "The Brit lives immediately to the right of the person in the blue house."
13. left_of(norwegian, fish)   "The owner of the fish lives immediately to the right of the Norwegian."
14. same(pilot, yellow)   "The pilot lives in the yellow house."
15. before(red, rabbit)   "The person in the red house lives in a lower-numbered house than the owner of the rabbit."
16. same(baker, tea)   "The baker drinks tea."
17. next_to(brit, purple)   "The Brit and the person in the purple house live in adjacent houses."
18. gap2(lawyer, milk)   "There is exactly one house between the lawyer and the milk drinker."
19. same(golf, spaniard)   "The Spaniard enjoys golf."
20. same(milk, tennis)   "The tennis enthusiast drinks milk."
21. same(coffee, golf)   "The golf enthusiast drinks coffee."
22. before(red, spaniard)   "The person in the red house lives in a lower-numbered house than the Spaniard."
23. same(painting, water)   "The person who drinks water enjoys painting."
24. same(cat, cooking)   "The owner of the cat enjoys cooking."

Solution: house 1: baker, cat, cooking, german, red, tea; house 2: bird, milk, pilot, swede, tennis, yellow; house 3: dane, green, hiking, juice, rabbit, teacher; house 4: blue, dog, lawyer, norwegian, painting, water; house 5: brit, chess, cocoa, farmer, fish, white; house 6: coffee, doctor, golf, horse, purple, spaniard
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-04

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Formal clues (with their English text):
1. at(white, 3)   "The person in the white house lives in the third house."
2. left_of(bird, horse)   "The person who keeps the bird lives directly to the left of the person who keeps the horse."
3. at(spaniard, 6)   "The Spaniard lives in the last house."
4. left_of(cat, juice)   "The cat owner lives directly to the left of the juice drinker."
5. end(cocoa)   "The person who drinks cocoa lives at one end of the row."
6. at(golf, 4)   "The golf enthusiast lives in the fourth house."
7. same(horse, yellow)   "The person who keeps the horse lives in the yellow house."
8. left_of(baker, green)   "The baker lives in the house just left of the one where the occupant of the green house lives."
9. end(chess)   "The chess enthusiast lives in one of the two end houses."
10. at(blue, 6)   "Whoever lives in the blue house lives in the sixth house."
11. same(fish, german)   "The German keeps the fish."
12. gap2(dog, milk)   "There is exactly one house between the owner of the dog and the person who drinks milk."
13. gap2(blue, norwegian)   "There is exactly one house between the person in the blue house and the Norwegian."
14. same(dane, purple)   "Whoever lives in the purple house is the Dane."
15. same(doctor, tea)   "The person who drinks tea works as the doctor."
16. next_to(horse, lawyer)   "The horse owner and the lawyer are neighbours."
17. before(tea, pilot)   "The pilot lives somewhere to the right of the person who drinks tea."
18. same(german, teacher)   "The German works as the teacher."
19. same(painting, rabbit)   "The painting enthusiast keeps the rabbit."
20. same(bird, farmer)   "The farmer keeps the bird."
21. at(swede, 5)   "The Swede lives in the fifth house."
22. left_of(coffee, bird)   "The owner of the bird lives immediately to the right of the person who drinks coffee."
23. gap2(golf, tennis)   "The golf enthusiast and the tennis enthusiast live two houses apart."
24. next_to(hiking, white)   "The hiking enthusiast lives next to the person in the white house."

Solution: house 1: cat, chess, dane, doctor, purple, tea; house 2: fish, german, hiking, juice, red, teacher; house 3: baker, brit, coffee, painting, rabbit, white; house 4: bird, farmer, golf, green, milk, norwegian; house 5: cooking, horse, pilot, swede, water, yellow; house 6: blue, cocoa, dog, lawyer, spaniard, tennis
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-07

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Formal clues (with their English text):
1. same(painting, white)   "The occupant of the white house enjoys painting."
2. left_of(rabbit, lawyer)   "The rabbit owner lives directly to the left of the lawyer."
3. or(dog, doctor, pilot)   "The dog owner either works as the doctor or works as the pilot."
4. or(coffee, cooking, tennis)   "The coffee drinker either enjoys cooking or enjoys tennis."
5. or(blue, juice, tea)   "The person in the blue house either drinks juice or drinks tea."
6. gap2(blue, milk)   "The person in the blue house and the milk drinker live two houses apart."
7. at(teacher, 3)   "The teacher lives in the third house."
8. left_of(horse, bird)   "The person who keeps the horse lives directly to the left of the person who keeps the bird."
9. left_of(fish, yellow)   "The person who keeps the fish lives directly to the left of the person in the yellow house."
10. not_next_to(doctor, milk)   "The doctor and the milk drinker are not neighbours."
11. not_same(green, norwegian)   "The Norwegian does not live in the green house."
12. at(tennis, 5)   "The person who enjoys tennis lives in house 5."
13. next_to(doctor, horse)   "The doctor lives next to the person who keeps the horse."
14. at(spaniard, 3)   "The Spaniard lives in the third house."
15. next_to(baker, cocoa)   "The baker and the cocoa drinker are neighbours."
16. left_of(yellow, hiking)   "Whoever lives in the yellow house lives in the house just left of the one where the hiking enthusiast lives."
17. left_of(brit, tea)   "The person who drinks tea lives immediately to the right of the Brit."
18. before(cocoa, horse)   "The cocoa drinker lives somewhere to the left of the person who keeps the horse."
19. left_of(german, swede)   "The German lives in the house just left of the one where the Swede lives."
20. same(coffee, green)   "The person who drinks coffee lives in the green house."
21. same(baker, golf)   "The golf enthusiast works as the baker."
22. at(purple, 5)   "Whoever lives in the purple house lives in the fifth house."
23. same(dog, hiking)   "The person who keeps the dog enjoys hiking."
24. left_of(swede, milk)   "The milk drinker lives immediately to the right of the Swede."

Solution: house 1: baker, blue, german, golf, juice, rabbit; house 2: cocoa, fish, lawyer, painting, swede, white; house 3: cat, chess, milk, spaniard, teacher, yellow; house 4: brit, dog, hiking, pilot, red, water; house 5: farmer, horse, norwegian, purple, tea, tennis; house 6: bird, coffee, cooking, dane, doctor, green
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
