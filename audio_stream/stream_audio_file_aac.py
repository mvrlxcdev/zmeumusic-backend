import requests
from flask import Response, stream_with_context

def stream_audio_file_aac(audio_url, request_headers):
    headers = {}
    if 'Range' in request_headers:
        headers['Range'] = request_headers['Range']

    r = requests.get(audio_url, headers=headers, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    response = Response(stream_with_context(generate()), status=206)
    response.headers['Content-Type'] = 'audio/aac'
    response.headers['Accept-Ranges'] = 'bytes'

    if 'Content-Range' in r.headers:
        response.headers['Content-Range'] = r.headers['Content-Range']
    if 'Content-Length' in r.headers:
        response.headers['Content-Length'] = r.headers['Content-Length']

    return response