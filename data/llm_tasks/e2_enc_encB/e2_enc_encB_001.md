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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encB/e2_enc_encB_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Teal, Amber, Crimson, Violet, Ivory
- instrument: Drums, Violin, Harp, Flute, Piano
- fruit: Plum, Cherry, Mango, Lemon, Apple
- country: Chile, Norway, Kenya, Japan, Peru

Clues:
1. The ivory house is at the far right.
2. The violet house is directly left of the ivory house.
3. There is exactly one house between the teal house and the crimson house.
4. The crimson house is somewhere to the right of the teal house.
5. The piano player lives in the ivory house.
6. The flute player lives directly left of the piano player.
7. The harp player lives in the crimson house.
8. The violinist lives directly right of the drummer.
9. The apple eater is the piano player.
10. The mango eater is the harp player.
11. The lemon eater lives directly right of the mango eater.
12. The cherry eater is the violinist.
13. The Japanese resident lives in the violet house.
14. The Kenyan resident eats mango.
15. The Norwegian lives next to the Kenyan.
16. The Chilean lives directly left of the Norwegian.

## Puzzle zebra/0/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, nurse, farmer, judge, tailor
- vehicle: van, jeep, truck, moped, coach
- fruit: kiwi, mango, grape, peach, lemon
- hobby: yoga, dance, golf, chess, sewing

Clues:
1. The judge lives in the middle house.
2. The baker lives next to the judge.
3. The tailor lives next to the judge.
4. The farmer lives somewhere to the left of the nurse.
5. The tailor lives somewhere to the left of the baker.
6. The nurse rides the moped.
7. The tailor drives the coach.
8. The jeep driver lives next to the van driver.
9. The truck driver lives somewhere to the left of the tailor.
10. The baker does not drive the van.
11. The kiwi eater drives the coach.
12. The mango eater rides the moped.
13. The peach eater is the judge.
14. The lemon eater drives the jeep.
15. The golfer is the judge.
16. The yoga fan eats lemon.
17. The nurse enjoys sewing.
18. The chess player lives directly right of the dancer.

## Puzzle zebra/3/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Abe, Bea, Cid, Dot, Eli
- instrument: banjo, cello, harp, oboe, sitar
- snack: bagel, donut, muffin, scone, waffle
- color: azure, crimson, ebony, ivory, violet

Clues:
1. Eli lives in the middle house.
2. Bea and Dot live at opposite ends of the row.
3. Abe lives directly right of Dot.
4. Cid's house is crimson.
5. The violet house is at one end of the row, but it is not Dot's.
6. The azure house is directly right of the ivory house.
7. Abe's house is not ivory.
8. The cellist lives in the crimson house.
9. The sitar player lives in Abe's house.
10. The harpist lives at one end of the row.
11. The harpist lives somewhere left of the banjo player.
12. Bea does not play the banjo.
13. The donut is eaten by the cellist.
14. The muffin is eaten in the violet house.
15. The bagel is eaten by the sitar player.
16. The scone is not eaten by the banjo player.

## Puzzle zebra/2/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Elena, Carla, Boris, Anna, Dmitri
- fruit: Pear, Kiwi, Peach, Fig, Lime
- pet: Hamster, Lizard, Tortoise, Parrot, Beagle
- sport: Squash, Cycling, Hockey, Rowing, Cricket

Clues:
1. Dmitri lives in the last house.
2. Anna lives next to Dmitri.
3. There is exactly one house between Elena and Boris.
4. Boris lives somewhere to the right of Elena.
5. The pear eater is Elena.
6. The lime eater lives in the last house.
7. The fig eater lives next to the lime eater.
8. The kiwi eater is Carla.
9. The beagle owner eats lime.
10. The parrot owner eats fig.
11. Boris owns the tortoise.
12. The lizard owner lives directly right of the hamster owner.
13. Anna plays rowing.
14. The cricket player owns the beagle.
15. The hockey player owns the tortoise.
16. The squash player does not live next to the hockey player.

## Puzzle zebra/0/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: amber, teal, pink, grey, brown
- instrument: piano, flute, harp, drums, cello
- snack: nuts, cake, pie, chips, cookie
- country: Peru, Cuba, Chad, Fiji, Iran

Clues:
1. The amber house is in the middle.
2. The pink house is not next to the amber house.
3. The teal house is directly left of the grey house.
4. The brown house is next to the amber house.
5. The grey house is not the rightmost house.
6. The Iranian lives directly left of the brown house.
7. The Peruvian lives next to the Iranian but not in the brown house.
8. The Cuban lives in the brown house.
9. The Fijian lives somewhere to the left of the Chadian.
10. The cello player is the Iranian.
11. The drummer is the Cuban.
12. The pianist and the harpist live next to each other.
13. The pianist lives in the grey house.
14. The person eating chips plays the drums.
15. The pie eater plays the harp.
16. The cookie eater is the Iranian.
17. The nut eater is not the Chadian.

## Puzzle zebra/1/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- pet: dog, cat, bird, fish, rabbit
- drink: tea, coffee, milk, juice, water
- hobby: sailing, chess, golf, yoga, darts

Clues:
1. The green house is directly left of the red house.
2. The yellow house is directly right of the red house.
3. The blue house is somewhere to the right of the yellow house.
4. The white house is at one end of the row.
5. The water drinker lives in the white house.
6. The tea drinker lives in the green house.
7. The tea drinker lives directly right of the water drinker.
8. The milk drinker lives in the red house.
9. The juice drinker lives directly left of the coffee drinker.
10. The rabbit lives in the white house.
11. The cat drinks tea.
12. The dog lives in the red house.
13. The fish lives next to the dog.
14. The yoga fan drinks water.
15. The chess player owns the cat.
16. The darts player owns the dog.
17. The golfer lives next to the darts player.

## Puzzle zebra/0/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- flower: rose, tulip, lily, daisy, iris
- gem: ruby, opal, jade, onyx, pearl
- herb: basil, thyme, sage, mint, dill
- tool: saw, drill, hammer, wrench, plane

Clues:
1. The rose is in the middle house.
2. The iris is directly right of the lily.
3. The lily is in house 1 or house 2.
4. The tulip is in one of the two end houses.
5. The jade is in the rose's house.
6. The pearl is in the daisy's house.
7. The opal is in one of the two end houses.
8. The opal is somewhere to the right of the ruby.
9. The onyx is not in house 2.
10. The onyx goes with the mint.
11. The dill is directly right of the mint.
12. The basil goes with the jade.
13. The thyme goes with the opal.
14. The hammer is in the rose's house.
15. The wrench is in the tulip's house.
16. The drill goes with the sage.
17. The saw is directly right of the plane.

## Puzzle zebra/0/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- pet: dog, cat, fish, bird, horse
- drink: tea, coffee, milk, juice, water
- job: doctor, teacher, chef, pilot, artist

Clues:
1. The doctor lives in the leftmost house.
2. The yellow house is the far right house.
3. The green house is directly right of the blue house.
4. The white house is directly right of the green house.
5. The red house is next to the blue house.
6. The chef lives in the blue house.
7. The milk drinker lives in the middle house.
8. The fish owner drinks milk.
9. The pilot lives next to the artist.
10. The artist lives in the yellow house.
11. The cat lives directly right of the dog.
12. The pilot keeps the bird.
13. The pilot drinks juice.
14. The dog owner drinks tea.
15. The coffee drinker lives somewhere to the left of the water drinker.

## Puzzle zebra/0/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: ivory, navy, coral, mauve, khaki
- pet: ferret, goat, owl, gecko, pony
- music: jazz, rock, folk, blues, punk
- drink: mocha, kefir, sake, punch, broth

Clues:
1. The ivory house is directly left of the khaki house.
2. The navy house is directly right of the khaki house.
3. The coral house is not next to the mauve house.
4. The coral house is somewhere to the left of the mauve house.
5. The ferret lives in the khaki house.
6. The pony lives next to the ferret.
7. The pony does not live in the ivory house.
8. The gecko lives next to the owl.
9. The owl lives somewhere to the left of the gecko.
10. The folk fan keeps the ferret.
11. The rock fan lives directly right of the folk fan.
12. The jazz fan keeps the gecko.
13. The punk fan lives somewhere to the left of the blues fan.
14. The mocha drinker likes folk.
15. The broth drinker lives in the navy house.
16. The punch drinker likes jazz.
17. The sake drinker does not live in the coral house.

## Puzzle zebra/2/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- race: Dwarf, Gnome, Human, Orc, Elf
- weapon: Axe, Staff, Sword, Spear, Bow
- mount: Boar, Wolf, Horse, Griffin, Bear
- gem: Opal, Pearl, Ruby, Onyx, Jade

Clues:
1. The Human lives in the middle house.
2. The Gnome lives directly left of the Human.
3. The Orc lives next to the Human.
4. The Elf lives somewhere to the right of the Dwarf.
5. The Sword belongs to the Human.
6. The Bow belongs to the Elf.
7. The Spear wielder lives directly left of the Elf.
8. The Gnome does not use the Axe.
9. The Horse rider wields the Sword.
10. The Bear rider wields the Bow.
11. The Griffin rider lives directly left of the Bear rider.
12. The Wolf rider lives next to the Horse rider.
13. The Ruby belongs to the Horse rider.
14. The Onyx belongs to the Orc.
15. The Pearl belongs to the Gnome.
16. The Jade owner lives somewhere to the right of the Onyx owner.
