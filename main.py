from flask import Flask, request

from audio_stream.get_audio_url_aac import get_audio_url_aac
from audio_stream.get_audio_url_mpeg import get_audio_url_mpeg
from audio_stream.stream_audio_file_aac import stream_audio_file_aac
from audio_stream.stream_audio_file_mpeg import stream_audio_file_mpeg
from youtube_music_api.search import search_with_filter

app = Flask(__name__)


@app.route('/getLinkAAC')
def stream_audio():
    youtube_url = request.args.get('url')

    if not youtube_url:
        return "No URL provided", 400

    audio_url = get_audio_url_aac(youtube_url)

    return stream_audio_file_aac(audio_url, request.headers)


@app.route('/getLinkMpeg')
def stream_audio_mpeg():
    youtube_url = request.args.get('url')

    if not youtube_url:
        return "No URL provided", 400

    audio_url = get_audio_url_mpeg(youtube_url)

    return stream_audio_file_mpeg(audio_url, request.headers)

@app.route('/')
def default():
    return "bobi bob"

@app.route('/search')
def search_songs():
    if 'Range' not in request.headers:
        search = request.args.get('q')
        search_filter = request.args.get('filter')
        return search_with_filter(q=search, search_filter=search_filter)


if __name__ == "__main__":
    app.run(port=8080, debug=True)


