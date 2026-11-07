from recommender import recommend

def main():
    print("SMART MOVIE RECOMMENDATION SYSTEM")
    while True:
        print("\n1. Get recommendations")
        print("2. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            preference = input("Enter genre, movie title or description: ").strip()
            if not preference:
                print("Please enter a preference.")
                continue
            results = recommend(preference)
            if not results:
                print("No close text matches found. Try a different preference.")
            else:
                print("\nRecommended movies:")
                for item in results:
                    print(f"- {item['title']} ({item['genre']}) — similarity {item['score']:.2f}")
                print("Similarity is text overlap, not a guarantee you will like the item.")
        elif choice == "2":
            break
        else:
            print("Choose 1 or 2.")

if __name__ == "__main__":
    main()
