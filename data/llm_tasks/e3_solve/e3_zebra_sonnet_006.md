# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_006.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01103-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, yellow, blue, red, purple
- drink: coffee, juice, milk, water, tea
- job: teacher, pilot, baker, doctor, lawyer
- nationality: Brit, Spaniard, Swede, Dane, German

Clues:
1. The baker lives directly to the left of the doctor.
2. The person in the blue house lives in the fourth house.
3. The person who drinks milk lives next to the pilot.
4. The occupant of the white house works as the baker.
5. The Spaniard lives in the house just left of the one where the baker lives.
6. The doctor lives in the fourth house.
7. Whoever lives in the red house is the Brit.
8. Whoever lives in the purple house lives directly to the left of the Swede.
9. There is exactly one house between the German and the person who drinks water.
10. The Brit lives immediately to the right of the Dane.
11. The baker and whoever lives in the purple house are neighbours.
12. The person in the yellow house lives in a lower-numbered house than the Swede.
13. There is exactly one house between the Swede and the teacher.
14. The coffee drinker lives in the blue house.
15. Whoever lives in the blue house is not the Swede.
16. The Brit works as the lawyer.
17. The juice drinker lives in the second house.
18. Whoever lives in the white house is not the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
