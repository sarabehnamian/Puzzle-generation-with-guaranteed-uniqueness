# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The golf enthusiast is the Swede.
2. The person who enjoys golf does not live in the first house.
3. The water drinker and the person in the white house live in adjacent houses.
4. The person who enjoys golf either works as the farmer or works as the pilot.
5. The Spaniard enjoys tennis.
6. There is exactly one house between the person who drinks cocoa and the Spaniard.
7. The person who drinks juice lives in the white house.
8. The teacher lives in the white house.
9. The person in the red house works as the doctor.
10. The person who enjoys chess lives in the second house.
11. The person who enjoys tennis lives next to the cooking enthusiast.
12. The milk drinker and the Dane are different people.
13. The person who keeps the horse lives in the purple house.
14. The lawyer lives in the yellow house.
15. The fish owner works as the doctor.
16. The cooking enthusiast and the occupant of the yellow house live two houses apart.
17. The teacher lives somewhere to the left of the person who enjoys painting.
18. The coffee drinker lives next to the Norwegian.
19. The person in the green house works as the baker.
20. The person who keeps the bird lives in house 2.
21. The farmer lives immediately to the right of the Dane.
22. The doctor and the person who enjoys tennis are neighbours.
23. The dog owner is the German.
24. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.
25. The bird owner and the fish owner are not neighbours.
26. The Brit and the person in the blue house are neighbours.
27. The person in the white house is the Brit.
28. The doctor lives at one end of the row.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
