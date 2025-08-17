from pipeline import chain

BANNER = "RAG Q&A — Project 1 (type 'exit' to quit)"

def main() -> None:
    print(BANNER)
    while True:
        try:
            query = input("Query: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not query:
            continue
        if query.lower() == 'exit'.lower():
            print("Goodbye!")
            break

        try:
            print()
            print( chain.invoke(query) )
            print()
        except Exception:
            print("Error: unable to process the query. Please check your setup and try again.\n")

if __name__ == "__main__":
    main()

# Created By Amit Mahapatra