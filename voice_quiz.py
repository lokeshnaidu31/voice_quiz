import speech_recognition as sr
def get_audio_input(p):
    rec=sr.Recognizer()
    with sr.Microphone() as s:
        print(p)
        audio=rec.listen(s)
        try:
            return rec.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry i couldn't understand")
        except Exception as e:
            print(f"an error occured :{e}")
        return None
def quiz():
    questions=[{"question":"Color of grass?",
                "options":["A)green","B)blue","C)brown","D)pink"],
                "correct":"option a"},
               {"question":"pm of india?",
                "options":["A)jagan","B)modi","C)pawan","D)kcr"],
                "correct":"option b"},
               {"question":"voting eligibility age in india?",
                "options":["A)<15","B)<18","C)<12","D)>=18"],
                "correct":"option d"}]
    score = 0
    print("---------------------------INSTRUCTIONS------------------------------------")
    print("1) You will be asked 3 questions and 4 options will be given for each question")
    print("2) To select your answer, say 'option a/b/c/d'")
    print("3) For correct answers, you will be awarded +10 marks")
    print("4) For incorrect answers, you will be deducted -5 marks")
    print("---------------------------LET'S GET STARTED-------------------------------")
    for q in questions:
        print(f"[question]:{q['question']}")
        for opt in q['options']:
            print(opt)
        answer=get_audio_input("tell your answer.....")
        print(answer)
        if answer is not None and answer.lower()==q['correct']:
            print("correct!")
            score+=10
        else:
            print("incorrect!")
            score-=5
        print("-----------------------------------------------------------------------\n")
    print(f"Your final score is: {score} / 30")
    if score >= 25:
        print("--------------EXCELLENT! SCORE KEEP IT UP-------------------------------")
    elif score >= 15:
        print("--------------------GOOD SCORE, NICE------------------------------------")
    else:
        print("--------------------SORRY, YOU FAILED--------------------------------")
            
print("to participate say 'hello!'")
a=get_audio_input("listening.....")
if a is not None and a.lower()=="hello":
    quiz()
else:
    print("looking like you are not intrested in partisipating,ok bye")
