if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = set(['first_kill', "level_10", "treasure_hunter", "speed_demon"])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set([
        'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon', 'perfectionist'
    ])
    print(f"Player alice achievements : {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {alice | bob | charlie}")
    print(f"Total unique achievements: {len(alice | bob | charlie)}")
    print(f"\nCommon to all players: {alice & bob & charlie}")
    unique_alice = alice - (bob | charlie)
    unique_bob = bob - (alice | charlie)
    unique_charlie = charlie - (alice | bob)
    rare = unique_alice | unique_bob | unique_charlie
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")
