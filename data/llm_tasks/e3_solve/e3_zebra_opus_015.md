# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_015.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01049-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, pilot, baker, lawyer
- drink: juice, cocoa, tea, milk, water
- nationality: Swede, Dane, Brit, Norwegian, German
- color: red, green, yellow, purple, blue

Clues:
1. The doctor lives in the fourth house.
2. Whoever lives in the green house either works as the doctor or works as the teacher.
3. The person in the red house drinks juice.
4. Whoever lives in the green house lives in the fourth house.
5. The person who drinks water is the Norwegian.
6. The German lives in the yellow house.
7. The Norwegian and the teacher live two houses apart.
8. The lawyer lives somewhere to the left of the person who drinks cocoa.
9. The Swede lives next to the tea drinker.
10. The teacher lives somewhere to the right of the person who drinks water.
11. The lawyer lives immediately to the right of the occupant of the blue house.
12. The baker lives in one of the two end houses.
13. The person who drinks cocoa and the Dane are neighbours.
14. The occupant of the blue house and the Brit are neighbours.
15. The person who drinks milk and the person who drinks water are not neighbours.
16. The person who drinks tea lives at one end of the row.
17. The Dane lives in one of the two end houses.
18. The occupant of the purple house drinks tea.
19. The cocoa drinker and the occupant of the yellow house live in adjacent houses.
20. The doctor lives in the house just left of the one where the person in the purple house lives.
21. The milk drinker lives in house 3.
22. The baker lives in the blue house.
23. The Norwegian lives in the first house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
