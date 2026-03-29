import ffmpeg

(
    ffmpeg
    .input("input.mp4")
    .output("output1.wav", ac=1, ar=16000)
    .overwrite_output()
    .run()
)
