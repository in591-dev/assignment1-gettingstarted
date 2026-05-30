### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "e9fe5d14de84a453e70e90c98dc4b96f44fa400a60da1bf1635bba2b5fe35d6d"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "That question is invalid. Please check for any grammatical errors or whether you asked it correctly. Please try again"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
# The secret passphrase is: pcap
#"Are encoding and encryption the same? - Yes/No":
# No
#"Is it possible to decrypt a message without a key? - Yes/No":
# No
#"Is it possible to decode a message without a key? - Yes/No":
# Yes
#"Is a hashed message supposed to be un-hashed? - Yes/No":
# No
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#e9fe5d14de84a453e70e90c98dc4b96f44fa400a60da1bf1635bba2b5fe35d6d
#"Is MD5 a secured hashing algorithm? - Yes/No":
# No
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
# 4
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
# 2
