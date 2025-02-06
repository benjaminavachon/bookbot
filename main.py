def word_count(text):
    return len(text.split())

def letter_count(text):
    final = {}
    for i in text:
        j = i.lower()
        if(j in final):
            final[j] += 1
        else:
            final[j] = 1
    return final

def sort_on(dic):
    return dic["num"]

def report(text):
    final = letter_count(text)
    final_list = []

    for i in final:
        final_list.append({"letter":i,"num":final[i]})
    #print(final_list)

    final_list.sort(reverse=True,key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(str(word_count(text))+" words found in the document")
    for i in final_list:
        #print(i)
        if(i["letter"].isalpha()):
            print("The '"+i["letter"]+"' character was found "+str(i["num"])+" times")
    print("--- End report ---")

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    report(file_contents)
main()
