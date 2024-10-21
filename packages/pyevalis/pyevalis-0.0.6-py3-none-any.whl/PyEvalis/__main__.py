import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of parameters.")
        print("Usage: pyevalis <inputFileName> <resultFileName>")
    else:
        inputFileName = sys.argv[1]
        resultFileName = sys.argv[2]
        #DecisionTree.DecisionTree(inputFileName, resultFileName)


if __name__ == "__main__":
    main()
