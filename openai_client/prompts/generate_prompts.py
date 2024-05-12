import pickle
languages = ["Python", "Rust", "C++", "Javascript", "Java", "Swift", "Whitespace", "C#", "Go", "PHP", "Cobol", "Fortran", "Kotlin", "Ruby"]
computer_scientists = [
    "Alan Turing",
    "Grace Hopper",
    "Donald Knuth",
    "Ada Lovelace",
    "John von Neumann",
    "Tim Berners-Lee",
    "Barbara Liskov",
    "Dennis Ritchie",
    "Vint Cerf",
    "Linus Torvalds"
]
algorithms = [
    "Floyd Warshall",
    "Dijkstra",
    "Fast fourier transform",
    "Binary search",
    "Merge sort",
    "Quick sort",
    "Radix sort",
    "Kruskal's",
    "Prim's",
    "Edmonds-Karp",
    "Euclidean"
]
prompts = []
for i in range(0, len(languages)):
    for j in range(i + 1, len(languages)):
        prompts.append(f"Make your fun fact comparing these two languages: {languages[i]} and {languages[j]}")
for i in range(0, len(languages)):
    prompts.append(f"Make your fun fact about this language: {languages[i]}")
for i in range(0, len(computer_scientists)):
    prompts.append(f"Make your fun fact about this computer scientist: {computer_scientists[i]}")
for i in range(0, len(algorithms)):
    prompts.append(f"Make your fun fact about the {algorithms[i]} algorithm")

with open("./openai_client/prompts/prompts.pkl", "wb") as file:
    pickle.dump(prompts, file)