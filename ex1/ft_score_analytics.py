import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No score provided. "
            "Usage: python3 ft_score_analytics.py <score1> ..."
        )
    else:
        scores = []
        try:
            for arg in sys.argv[1:]:
                score = int(arg)
                scores += [score]
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / (len(sys.argv) - 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError:
            print(f"oops, I typed '{arg}' instead of '1000'")
