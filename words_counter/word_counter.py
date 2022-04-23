'''WORDS COUNTER
This program hears your voice in a .wav file and shows you how many
times you said all the words that you mention on it. 

Take care Robin Scherbatsky, but um...
'''
from time import time
import speech_recognition as sr
from datetime import datetime

def execution_time(func):
    '''Decorator: Shows function time execution'''
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print('The execution elapsed ' + str(time_elapse.total_seconds()) + ' seconds')
    return wrapper


def audio_to_list(path: str)->list:
    '''Transform the audio file in a str variable and then split it out to a list

    Param str path Any filepath wich conduces to a .wav file
    Returns list word_list It contains all words that were heard in the audio file
    '''
    r = sr.Recognizer()
    audio_file = sr.AudioFile(path)

    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    string = r.recognize_google(audio, language='es-MX')
    print(string)
    string = string.lower()
    words_list = string.split()
    return words_list


def words_counter(words_list: list)->dict:
    '''Counts all words and their duplicates. Also order it from largest to smallest

    Param list words_list Any list of str word
    Returns dict sorted_dict It contains as a key all words that were given in 
    words_list and as a value the times that were appearing
    '''
    words_set = set(words_list)
    words_dict = {key: 0 for key in words_set}
    
    for key in words_list:
        words_dict[key] += 1

    sorted_tuples = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}

    return sorted_dict


@execution_time
def run():
    path = '/home/jona_vz/Platzi/curso_python_profesional/final_project/vox_02.wav'
    
    words_list = audio_to_list(path)
    words = words_counter(words_list)

    for key, value in words.items():
        print(f'{key} --- {value}')


if __name__ == '__main__':
    run()