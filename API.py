
from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import asyncio
from AssemblyAi import start_transcription
import base64

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API"


@app.route('/auth',methods=["POST"])
def get_auth():
    datain = request.get_json()
    data = {
        "data": "XD",
        "message": "Login Completo",
        "status": "200"
    }
    response  = jsonify(data)
    
    return response,200




@app.route('/sendAudio',methods=["POST"])
async def get_audio():

    datain = request.get_json()
    print(datain['archivo'])
    base64_to_audio(datain['archivo'], "Audio/audio.mp3")
    data = {
        "message": "Audio Recibido",
        "status": "200"
    }
    response  = jsonify(data)


    await asyncio.create_task(start_transcription("Audio/audio.mp3"))


    return response,200


@app.route('/getPDF',methods=["GET"])
def get_pdf():
    return send_file('Video2PDF.pdf', as_attachment=True)



def base64_to_audio(base64_audio_string, output_file_path):
    try:
        # Decode the Base64 string
        audio_data = base64.b64decode(base64_audio_string)
        
        # Write the audio data to a file
        with open(output_file_path, "wb") as audio_file:
            audio_file.write(audio_data)

        print(f"Audio saved to {output_file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
