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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_mut_g1/e4b_mut_g1_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g1-00

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Formal clues (with their English text):
1. before(dog, tea)   "The dog owner lives in a lower-numbered house than the tea drinker."
2. same(teacher, tennis)   "The teacher enjoys tennis."
3. left_of(juice, cat)   "The cat owner lives immediately to the right of the juice drinker."
4. gap2(swede, white)   "The Swede and the person in the white house live two houses apart."
5. same(horse, pilot)   "The horse owner works as the pilot."
6. next_to(purple, spaniard)   "Whoever lives in the purple house lives next to the Spaniard."
7. gap2(tea, tennis)   "The tea drinker and the tennis enthusiast live two houses apart."
8. same(cat, cooking)   "The owner of the cat enjoys cooking."
9. next_to(cocoa, dog)   "The person who drinks cocoa and the owner of the dog live in adjacent houses."
10. at(blue, 3)   "The occupant of the blue house lives in house 3."
11. same(bird, dane)   "The owner of the bird is the Dane."
12. same(brit, tea)   "The Brit drinks tea."
13. next_to(cocoa, norwegian)   "The person who drinks cocoa and the Norwegian live in adjacent houses."
14. same(green, hiking)   "The hiking enthusiast lives in the green house."
15. next_to(green, red)   "Whoever lives in the green house lives next to the occupant of the red house."
16. same(chess, yellow)   "The person who enjoys chess lives in the yellow house."
17. left_of(farmer, rabbit)   "The farmer lives in the house just left of the one where the person who keeps the rabbit lives."
18. next_to(doctor, red)   "The doctor lives next to the person in the red house."
19. next_to(baker, cocoa)   "The baker lives next to the person who drinks cocoa."
20. same(coffee, golf)   "The person who drinks coffee enjoys golf."
21. gap2(cat, lawyer)   "There is exactly one house between the person who keeps the cat and the lawyer."
22. left_of(rabbit, painting)   "The person who keeps the rabbit lives in the house just left of the one where the painting enthusiast lives."
23. at(juice, 2)   "The juice drinker lives in house 2."
24. before(milk, juice)   "The person who drinks milk lives in a lower-numbered house than the person who drinks juice."

Solution: house 1: bird, dane, doctor, green, hiking, milk; house 2: dog, juice, norwegian, red, teacher, tennis; house 3: blue, cat, cocoa, cooking, farmer, swede; house 4: baker, brit, chess, rabbit, tea, yellow; house 5: fish, lawyer, painting, spaniard, water, white; house 6: coffee, german, golf, horse, pilot, purple
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-04

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Formal clues (with their English text):
1. next_to(green, yellow)   "The occupant of the green house lives next to the person in the yellow house."
2. gap2(brit, red)   "The Brit and the person in the red house live two houses apart."
3. same(dog, teacher)   "The teacher keeps the dog."
4. not_at(water, 2)   "The person who drinks water does not live in house 2."
5. same(green, lawyer)   "The person in the green house works as the lawyer."
6. same(horse, red)   "The occupant of the red house keeps the horse."
7. left_of(tennis, red)   "The person in the red house lives immediately to the right of the tennis enthusiast."
8. same(golf, tea)   "The tea drinker enjoys golf."
9. next_to(coffee, dane)   "The coffee drinker lives next to the Dane."
10. gap2(milk, yellow)   "The person who drinks milk and the person in the yellow house live two houses apart."
11. next_to(coffee, juice)   "The coffee drinker and the juice drinker are neighbours."
12. same(swede, white)   "The person in the white house is the Swede."
13. left_of(cat, red)   "The person in the red house lives immediately to the right of the person who keeps the cat."
14. same(milk, spaniard)   "The milk drinker is the Spaniard."
15. same(juice, red)   "The person in the red house drinks juice."
16. same(doctor, swede)   "The Swede works as the doctor."
17. next_to(baker, dog)   "The baker and the dog owner live in adjacent houses."
18. at(rabbit, 4)   "The owner of the rabbit lives in house 4."
19. next_to(bird, german)   "The bird owner and the German are neighbours."
20. before(farmer, purple)   "The farmer lives somewhere to the left of the person in the purple house."
21. left_of(blue, green)   "The person in the green house lives immediately to the right of the occupant of the blue house."
22. left_of(fish, painting)   "The owner of the fish lives directly to the left of the person who enjoys painting."
23. at(hiking, 6)   "The hiking enthusiast lives in the sixth house."
24. not_same(fish, spaniard)   "The Spaniard and the person who keeps the fish are different people."
25. at(cooking, 2)   "The person who enjoys cooking lives in house 2."

Solution: house 1: bird, blue, chess, farmer, milk, spaniard; house 2: cocoa, cooking, fish, german, green, lawyer; house 3: dog, norwegian, painting, teacher, water, yellow; house 4: baker, brit, golf, purple, rabbit, tea; house 5: cat, coffee, doctor, swede, tennis, white; house 6: dane, hiking, horse, juice, pilot, red
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-07

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Formal clues (with their English text):
1. left_of(dog, spaniard)   "The dog owner lives in the house just left of the one where the Spaniard lives."
2. gap2(brit, dog)   "There is exactly one house between the Brit and the person who keeps the dog."
3. gap2(baker, german)   "The baker and the German live two houses apart."
4. at(pilot, 4)   "The pilot lives in the fourth house."
5. left_of(brit, golf)   "The Brit lives in the house just left of the one where the golf enthusiast lives."
6. gap2(rabbit, tea)   "There is exactly one house between the person who keeps the rabbit and the person who drinks tea."
7. end(green)   "The occupant of the green house lives at one end of the row."
8. next_to(milk, tea)   "The person who drinks milk and the person who drinks tea are neighbours."
9. next_to(purple, red)   "Whoever lives in the purple house and the occupant of the red house are neighbours."
10. at(cooking, 1)   "The cooking enthusiast lives in house 1."
11. same(cocoa, red)   "The person who drinks cocoa lives in the red house."
12. left_of(german, blue)   "Whoever lives in the blue house lives immediately to the right of the German."
13. before(german, rabbit)   "The German lives in a lower-numbered house than the owner of the rabbit."
14. same(norwegian, red)   "Whoever lives in the red house is the Norwegian."
15. left_of(white, lawyer)   "The person in the white house lives in the house just left of the one where the lawyer lives."
16. at(doctor, 1)   "The doctor lives in the first house."
17. same(brit, cat)   "The Brit keeps the cat."
18. next_to(lawyer, teacher)   "The lawyer lives next to the teacher."
19. same(brit, water)   "The water drinker is the Brit."
20. same(chess, juice)   "The person who drinks juice enjoys chess."
21. left_of(norwegian, juice)   "The juice drinker lives immediately to the right of the Norwegian."
22. gap2(german, teacher)   "There is exactly one house between the German and the teacher."
23. same(bird, painting)   "The bird owner enjoys painting."
24. next_to(german, tennis)   "The German and the tennis enthusiast are neighbours."
25. left_of(fish, dane)   "The fish owner lives directly to the left of the Dane."

Solution: house 1: cocoa, cooking, doctor, dog, norwegian, red; house 2: baker, chess, horse, juice, purple, spaniard; house 3: brit, cat, farmer, tennis, water, yellow; house 4: fish, german, golf, pilot, tea, white; house 5: bird, blue, dane, lawyer, milk, painting; house 6: coffee, green, hiking, rabbit, swede, teacher
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
