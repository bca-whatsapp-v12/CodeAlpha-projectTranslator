from flask import Flask, request
import requests

app = Flask(__name__)

def translate_free(text, to_lang):
    try:
        url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{to_lang}"
        data = requests.get(url, timeout=5).json()
        return data['responseData']['translatedText']
    except:
        return text

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    original = ""
    if request.method == 'POST':
        original = request.form.get('text','').strip()
        to_lang = request.form.get('to_lang','hi')
        if original:
            result = translate_free(original, to_lang)
    
    html = """
    <div style='font-family:sans-serif; max-width:550px; margin:auto; padding:20px;'>
    <h2 style='text-align:center; color:#1a73e8;'>Chaitra's Translator</h2>
    <form method='POST' style='background:#f8f9fa; padding:20px; border-radius:15px;'>
    <input type='text' name='text' value='%s' style='padding:12px; width:92%%;'>
    <br><br>
    <select name='to_lang' style='padding:10px; width:100%%;'>
    <option value='hi'>Hindi</option>
    <option value='kn'>Kannada</option>
    <option value='en'>English</option>
    </select>
    <br><br>
    <button style='padding:12px; width:100%%; background:#1a73e8; color:white; border:none; border-radius:8px;'>Translate</button>
    </form>
    <div style='text-align:center; margin-top:20px; background:#e8f0fe; padding:20px; border-radius:10px;'><h2>%s</h2></div>
    </div>
    """ % (original, result)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
