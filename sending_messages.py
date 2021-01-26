def send_messages(unsent,sent):
    while unsent:
        uploading=unsent.pop()
        print(f"getting ready to print: {uploading}")
        sent.append(uploading)
        # for draft in unsent:
        #     print(draft)
def sent_messages(sent):
    print("the following messages have been sent: ")
    for message in sent:
        print(message)
unsent=['hello','hey','good luck','buenos dias','see you']
sent=[]

send_messages(unsent[:],sent)
sent_messages(sent)