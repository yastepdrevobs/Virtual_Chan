#some imports
import openai
import speech_recognition as sr

#variables and keys
openai.api_key = ""             #insert your API here
user_input=""
user_settings_role=""

#voice recognition module
def text_from_voice():
  speech_recognition = sr.Recognizer()  
  with sr.Microphone() as sourse:                                              
    audio = speech_recognition.listen(sourse,phrase_time_limit=6)
    audio_user_input = ""  
    try:
        audio_user_input = speech_recognition.recognize_google(audio)
        print("\n*****audio recognition*****\n"+audio_user_input+"\n***audio recognition ended***\n")
    except Exception as e:
        print("Exeption: "+ str(e))
  return audio_user_input

#twitch module
def twitch_chat():
    chat_input = ""
    return chat_input
    #coming soon

#openAI API module
def text_to_ai(user_input,system_input,big_fucking_data):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":str(system_input)},
        {"role":"user","content":str(user_input)},
        {"role":"assistant","content":str(big_fucking_data)}]
  )
  response_text = response["choices"][0]["message"]["content"]
  return response_text

#some UI starts here
user_settings1=input("choose way of interacting:\n 1: audio mode\n 2: text mode\n 3: twitch mode\n")

#input tipe change
if int(user_settings1)==1:
   print("\n*****Listening your voice*****\n")
   user_input = text_from_voice()
elif int(user_settings1)==2:
   user_input = input("Input qestion\n")
elif int(user_settings1)==3:
   user_input = twitch_chat()
else:
  print("cringer")

#more UI
user_settings_role=input("\nPrint the role of A.I\n")
calibration_data=input("\ninput some calibration data, so A.I. can answer properly\n")

#main cycle
while True:
    print(text_to_ai(user_input, user_settings_role, calibration_data))
    if int(user_settings1)==1:
        print("\n\n*****Listening your voice*****\n\n")
    else:
        print("voice unavaileble")
    if int(user_settings1)==1:
       user_input = text_from_voice()
    elif int(user_settings1)==2:
       user_input = input("Input qestion\n")