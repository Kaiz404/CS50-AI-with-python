from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Not(And(AKnight, AKnave)),  # Game Rules
    Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave),


    Or(AKnave, And(AKnave, AKnight))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Not(And(AKnight, AKnave)),  # Game Rules
    Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave),
    
    Not(And(AKnight, BKnight)),  # A and B cannot both be knights or knaves
    Not(And(AKnave, BKnave)),

    Or(AKnave, And(AKnave, BKnave))  # If A's statement is true, A is a Knight, or else A is a Knave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Not(And(AKnight, AKnave)),  # Game Rules
    Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave),
    
    
    Not(And(AKnight, BKnight)),  # A and B cannot both be knights or knaves
    Not(And(AKnave, BKnave)),

    Or(AKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # Logic for A's statement, If A is telling a lie A is a Knave
    Or(BKnave, Or(Not(And(AKnight, BKnight)), Not(And(AKnave, BKnave))))  # Logic for B's statement, If B is telling a lie B is a Knave
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Not(And(AKnight, AKnave)),  # Game Rules
    Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)),
    Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)),
    Or(CKnight, CKnave),
    
    Not(And(AKnight, BKnight, CKnight)),  # ABC cannot all be knights or knaves
    Not(And(AKnave, BKnave, CKnave)),

    # Logic for A's statement
    # 1) A said it is a Knight thus it is a Knight
    # 2) A said it is a Knave, but if this is the truth it contradicts its own statement
    Or(AKnight, AKnave),

    # Logic for B's first statement
    # 1) If A's statement from what B says is fundamentally flawed, B is a Knave
    Or(BKnave, And(AKnight, AKnave)),

    # Logic for B's second statement
    # 1) C is a Knave thus B is a Knight
    # 2) C is a Knight thus B is a Knave
    # B and C must be different roles
    Or(And(BKnight, CKnave), And(BKnave, CKnight)),

    # Logic for C's statement,
    # 1) A is a Knave thus C is a Knave
    # 2) A is a Knight thus C is a Knight
    # A and C must be the same Role
    Or(And(AKnight, CKnight), And(AKnave, CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
