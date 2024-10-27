from bk_asr import BcutASR, JianYingASR, KuaiShouASR


if __name__ == '__main__':
    #audio_file = "resources/test.mp3"
    audio_file = 'F:/pythonlearn/女友录音文件需求分析/output.wav'
    asr = BcutASR(audio_file)
    result = asr.run()
    results = result.to_srt()
    print(results)