if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    data = [
        {"player": "alice", "achievements": ["first_kill", "level_10"],
         "score": 2500, "region": "north", "active": True},
        {"player": "bob", "achievements": ["boss_slayer"],
         "score": 2800, "region": "south", "active": True},
        {"player": "charlie", "achievements": ["kill", "boss"],
         "score": 2200, "region": "east", "active": True},
        {"player": "diana", "achievements": ["boss"],
         "score": 1200, "region": "west", "active": False},
    ]

    active_data = [d for d in data if d['active']]

    print("=== List Comprehension Examples ===")
    high_scorers = [d['player'] for d in data if d['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {[d['score'] * 2 for d in data]}")

    active_p = [d['player'] for d in active_data]
    print(f"Active players: {active_p}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {d['player']: d['score'] for d in active_data}
    print(f"Player scores: {player_scores}")

    categories = [
        "high" if p['score'] >= 2500
        else "medium" if p['score'] >= 1500
        else "low" for p in data
    ]
    stats = {k: sum([1 for c in categories if c == k]) for k in categories}
    print(f"Score categories: {stats}")

    ach_count = {d['player']: len(d["achievements"]) for d in active_data}
    print(f"Achievements counts: {ach_count}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {d['player'] for d in data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {k for d in data for k in d['achievements']}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {d['region'] for d in active_data}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined analysis ===")
    all_scores = [d["score"] for d in active_data]
    avg = sum(all_scores) / len(all_scores)
    print(f"Total players: {len(data)}")
    total_ach_unique = len({a for d in active_data for a in d['achievements']})
    print(f"Total unique achievements: {total_ach_unique}")
    print(f"Average score: {avg}")

    top_entry = max([(d['score'], d) for d in active_data])
    top = top_entry[1]
    print(f"Top performer: {top['player']} ({top['score']} points, "
          f"{len(top['achievements'])} achievements)")
