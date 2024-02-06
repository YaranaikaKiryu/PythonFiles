def FunctionReplacedAndCased(EnterRepeatedWord, WordToReplace, WordReplacement):
    d = EnterRepeatedWord.lower()
    result_1 = d.replace(WordToReplace, WordReplacement)
    result_1 = result_1.upper()
    print(result_1)
    return result_1

print("==========")
EnterRepeatedWord = input("Enter sentence with repeated words >> ")
WordToReplace = input("Enter word to replace >> ")
WordReplacement = input("Enter word for the replaced one >> ")

result_1 = FunctionReplacedAndCased(EnterRepeatedWord, WordToReplace, WordReplacement)