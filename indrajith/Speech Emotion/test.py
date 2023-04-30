import os
from utils import convert, extract_feature


list_of_files = []
for file in os.listdir("./test"):
    list_of_files.append(f"{os.getcwd()}/test/{file}")

list_of_files = [
'/home/moe/Desktop/projects/sound_freq/speech_emotion_app/test/03-01-01-01-01-01-01.wav',
'/home/moe/Desktop/projects/sound_freq/speech_emotion_app/test/test_conversion.wav',
'/home/moe/Desktop/projects/sound_freq/speech_emotion_app/test/test_conversion.m4a'
]

def test_conversion():

    print("Testing Wav Conversion with test file...")
    result = convert(list_of_files[1])
    if isinstance(result,str) and result !="File Doesn't Exist" and result != "Invalid File: Must be in .wav format":
        print("WAV CONVERSION PASSED")
        os.remove(result)
    else:
        print("WAV CONVERSION FAILED")
    print("Testing Wav Conversion with empty input..")
    result = convert("")
    if result == "File Doesn't Exist":
        print("WAV CONVERSION PASSED")
    else:
        print("WAV CONVERSION FAILED")

    print("Testing Wav Conversion with non .wav input..")
    result = convert(list_of_files[2])
    if result == "Invalid File: Must be in .wav format":
        print("WAV CONVERSION PASSED")
    else:
        print("WAV CONVERSION FAILED")

def test_feature_extraction():
    print("Testing Feature Extraction with test file..")
    result = extract_feature(list_of_files[0])
    if len(result) > 1:
        print("FEATURE EXTRACTION PASSED")
    else:
        print("FEATURE EXTRACTION FAILED")
    print("Testing Feature Extraction with empty input..")
    result = extract_feature("")
    if result =="File Doesn't Exist":
        print("FEATURE EXTRACTION PASSED")
    else:
        print("FEATURE EXTRACTION FAILED")

test_feature_extraction()
test_conversion()
