'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
#variable sentence is assigned to a list
print(Sentence)
#prints the whole items in the list
print(Sentence[1])
#prints the index 1 of list variable sentence, whixh is "look". Indexing starts from 0
Sentence.append("life")
#adds one more item "life" to the list
Sentence[4] = "sunny"
#reassigns the index 4 from "bright" to "sunny"
print(Sentence[4])
#sunny
print(Sentence[0] + " " + Sentence[3])
#Always the
print(Sentence)
#prints the variable sentence, with whole items
#output: 'Always', 'look', 'on', 'the', 'sunny', 'side', 'of', 'life'

#the code run as I predicted