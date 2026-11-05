# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The farmer lives in the house just left of the one where the lawyer lives.
2. The person who keeps the cat lives next to the tea drinker.
3. The dog owner lives directly to the left of the doctor.
4. Whoever lives in the white house lives in the house just left of the one where the juice drinker lives.
5. The person who keeps the cat lives in the house just left of the one where the teacher lives.
6. There is exactly one house between the person who enjoys cooking and the person in the white house.
7. The occupant of the red house keeps the cat.
8. The Brit lives at one end of the row.
9. The baker keeps the dog.
10. The German lives directly to the left of the Norwegian.
11. There is exactly one house between the person who keeps the horse and the milk drinker.
12. Whoever lives in the blue house does not live next to the occupant of the green house.
13. Whoever lives in the purple house enjoys golf.
14. The person who keeps the rabbit is the Swede.
15. The Brit and whoever lives in the yellow house live two houses apart.
16. Whoever lives in the yellow house lives in the third house.
17. The fish owner lives somewhere to the right of the German.
18. The dog owner drinks water.
19. The lawyer lives in the green house.
20. The occupant of the green house and the tennis enthusiast are not neighbours.
21. The golf enthusiast lives somewhere to the left of the person who enjoys cooking.
22. The Dane and the dog owner are neighbours.
23. The doctor lives directly to the left of the hiking enthusiast.
24. The occupant of the green house and the Norwegian are neighbours.
25. The person who enjoys golf lives in the house just left of the one where the person who enjoys chess lives.
26. The doctor keeps the fish.
27. The person who drinks cocoa and the person who drinks milk live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
