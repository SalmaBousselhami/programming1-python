from pathlib import Path

def math_processor(expression):
    parts = expression.split(" ")

    interim_parts = []

    for idx, part in enumerate(parts):
        if part in ["*", "/"]:
            if part == "*":
                interim_result = float(parts[idx - 1]) * float(parts[idx + 1])
            else:
                interim_result = float(parts[idx - 1]) / float(parts[idx + 1])
            del parts[idx + 1]
            interim_parts[-1] = str(interim_result)
        else:
            interim_parts.append(part)

    result = float(interim_parts[0])

    for idx, part in enumerate(interim_parts):
        if part in ["+", "-"]:
            if part == "+":
                result += float(interim_parts[idx + 1])
            else:
                result -= float(interim_parts[idx + 1])

    return str(result)

def bubble_sort(results):
    n = len(results)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(results[j].split(" = ")[0]) > float(results[j+1].split(" = ")[0]):
                results[j], results[j+1] = results[j+1], results[j]
    return results

file_path = Path(__file__).parent / "expressions.txt"

expressions = file_path.read_text().splitlines()
results = []

for expression in expressions:
    result = math_processor(expression)
    print(result)
    results.append(f"{result} = {expression}")

results_sorted = bubble_sort(results)

file_path_results = Path(__file__).parent / "results2.txt"
file_path_results.write_text("\n".join(results))

