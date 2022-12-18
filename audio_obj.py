import wavlon as wavlon
import clutil as cl

class razz_audio_object:
    stage1 = [] #pattern stage
    stage2 = [] #pattern superficill

    def save(self,path="examples/output.razz"):
        print("saving .razz file")
        with open(path, 'w') as f:
            f.write("pattrn : {\n")
            for x in self.stage1:
                f.write("    "+x.__str__()+"\n")
            f.write("}\n\n")
            f.write("superficill : {\n")
            for x in self.stage2:
                f.write("    "+x["current"].__str__()+": "+x["count"].__str__()+"\n")
            f.write("}\n\n")

    def truetone(self,path="examples/output.wav"):
        audio=[]
        prev = 30
        depth = 0
        print("generating waveform truetone: 0%")
        for x in self.stage2:
            print(cl.lnup+"generating waveform truetone: "+(round(depth/len(self.stage2))*100).__str__()+"%")
            depth+=1
            audio=wavlon.append_sinewave(audio,freq=200+(((prev+x["current"])/2)*100),duration_milliseconds=200*x["count"])
            audio=wavlon.append_sinewave(audio,freq=200+(x["current"]*300),duration_milliseconds=200*x["count"])
            prev=x["current"]
        print(cl.lnup+"generating waveform truetone: 100%")
        print("saving to file (can take a while)")
        wavlon.save_wav(path,audio)