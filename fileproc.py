base_url = 'https://cointelegraph.com'
links = set()

with open('result.txt', 'r') as file:
    for line in file:
        links.add(line.strip())

sorted(links)

with open('sorted.txt', 'w') as fout:
    for link in links:
        if base_url not in link:
            continue
        fout.write(f"{link}\n")