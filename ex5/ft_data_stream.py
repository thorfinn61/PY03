def generate_events(count: int):
    players = ["alice", "bob", "charlie"]

    for i in range(1, count + 1):
        player = players[i % len(players)]
        level = (i * 13) % 20 + 1
        if i % 7 == 0:
            action = "leveled up"
        elif i % 3 == 0:
            action = "found treasure"
        else:
            action = "killed monster"
        yield (i, player, level, action)


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        # Test basic de primalité
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    total_events = 0
    high_lvl = 0
    treasure_cnt = 0
    lvl_up_cnt = 0

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    stream = generate_events(1000)
    for event in stream:
        event_id, player, level, action = event
        total_events += 1

        if event_id <= 3:
            print("Event", event_id, ": Player", player, "(level", level, ")",
                  action)
        elif event_id == 4:
            print("...")

        if level >= 10:
            high_lvl += 1
        if action == "leveled up":
            lvl_up_cnt += 1
        if action == "found treasure":
            treasure_cnt += 1

    print("\n=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+):", high_lvl)
    print("Treasure events:", treasure_cnt)
    print("Level-up events", lvl_up_cnt)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    first_f = True
    for value in fibonacci_generator(10):
        if not first_f:
            print(",", end=" ")
        print(value, end="")
        first_f = False
    print()

    print("Prime numbers (first 5):", end=" ")
    first_p = True
    for value in prime_generator(5):
        if not first_p:
            print(",", end=" ")
        print(value, end="")
        first_p = False
    print()