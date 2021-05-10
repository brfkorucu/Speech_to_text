import os
import speech_recognition as sr
import optparse
import playsound

def adding_path(ffmpeg_dir):
    os.system("setx path '%path%';'{}'".format(ffmpeg_dir))

def mp3_to_flac(audio_file, output_aud_dir):
    os.system("ffmpeg -y -i {} -ac 1 {}".format(audio_file, output_aud_dir))
    return output_aud_dir
    
def speech_text(output_aud_dir, text_dir):
    process = sr.Recognizer()
    with sr.AudioFile(output_aud_dir) as source:
        audio_data = process.record(source)
        text = process.recognize_google(audio_data)
        if text:
            with open(text_dir, "a+") as file:
                file.write(text)
        else :
            print("speech_recogniton cannot solve flac file")
            exit(0)

def main():
    parser = optparse.OptionParser("usage%prog " + "-a <audio-file_dir> -o <output-directory> -f <ffmpeg-bin-directory> -t <text.txt directory with name ")
    parser.add_option("-a", dest="audio_file", type="string", help="specify audio file directory")
    parser.add_option("-o", dest="output_aud_dir", type="string", help="specify output audio file directory")
    parser.add_option("-f", dest="ffmpeg_dir", type="string", help="specify ffmpeg bin directory")
    parser.add_option("-t", dest="text_dir", type="string", help="specify text directory with text name")
    (options, args) = parser.parse_args()
    audio_file = options.audio_file
    output_aud_dir = options.output_aud_dir
    ffmpeg_dir = options.ffmpeg_dir
    text_dir = options.text_dir
    if audio_file == None or output_aud_dir == None or text_dir == None:
        print(parser.usage)
        exit(0)
    try : 
        mp3_to_flac(audio_file, output_aud_dir)
    except:
        print("run script with admin/root permissions")
        if ffmpeg_dir :
            adding_path(ffmpeg_dir)
            mp3_to_flac(audio_file, output_aud_dir)
        else:
            print("Add ffmpeg bin directory")
            exit(0)
    speech_text(output_aud_dir,text_dir)
    if text_dir :
        print("SUCESS!!!")
        playsound.playsound(r"C:\Users\HOPE\Desktop\WorkSpace\Project-Miner\censor-beep-sound-effect.mp3")
    else :
        print("Something went wrong")
        playsound.playsound(r"C:\Users\HOPE\Desktop\WorkSpace\Project-Miner\censor-beep-sound-effect.mp3")
        playsound.playsound(r"C:\Users\HOPE\Desktop\WorkSpace\Project-Miner\censor-beep-sound-effect.mp3")
        
if __name__ == "__main__":
    main()