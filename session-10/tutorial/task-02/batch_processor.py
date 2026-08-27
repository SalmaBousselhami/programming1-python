from pathlib import Path

file_path = Path(__file__).parent / "expressions.txt"

expressions = file_path.read_text().splitlines()
results = []

for expression in expressions:
    result = eval(expression)
    print(result)
    results.append(f"{result} = {expression}")

results.sort(key=lambda x: float(x.split(" = ")[0]))

file_path_results = Path(__file__).parent / "results.txt"
file_path_results.write_text("\n".join(results))

