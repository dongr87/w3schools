import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote=True)

def rot13(s):
    result = ''
    for v in s:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c <= ord('A') and c <= ord('Z'):
            if c> ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)

    return result

html = """
<h1>Enter some text to ROT13:</h1>
<form method="post">
<textarea name="text"  cols="36" rows="10" placeholder="Please enter here..." value="%(text)s" style="border: 1px solid blue; padding: 15px 18px; font-size: 1.2em;">
</textarea>
<br>
<div style="color: red;">%(error)s</div>
<br>
<input type="submit" style="background-color: #2F648C; padding: 3px 8px; width: 200px; height: 40px; text-align: center; color: #FFFFFF; margin-left: 90px;">
</form>
"""

class ROT13(webapp2.RequestHandler):
    def write_html(self, error = "", text =""):
        self.response.out.write(html % {"error": error,
                                "text": text})

    def get(self):
        self.write_html()

    def post(self):
        user_text = self.request.get('text')
        transformed_text = rot13(user_text)
        if user_text:
            self.write_html(transformed_text, transformed_text)
        else:
            self.write_html()

app = webapp2.WSGIApplication([('/', ROT13)],
                              debug = True)
