import urllib.request as ur
import json as j


def get_answers(id):  
    url = "https://play.kahoot.it/rest/kahoots/"+id

    json = j.loads(ur.urlopen(url).read())
    
    print(f"\n{json.get('title')}\n")

    questions = json.get("questions")

    for index, slide in enumerate(questions):
        print(f"{index+1}. {slide['question']}\n")
        correct_choice_index = -1
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"]:
                correct_choice_index = i
                print(f"({chr(65+i)}) {slide['choices'][i].get('answer')} [CORRECT]")
                break
        print()
        for i in range(len(slide.get("choices"))):
            if i == correct_choice_index:
                continue
            print(f"({chr(65+i)}) {slide['choices'][i].get('answer')}")
        print()

if __name__ == "__main__":
    get_answers(input("[-] QUIZ ID: "))
       