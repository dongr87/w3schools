import webapp2


months = ['January',
                  'February',
                  'March',
                  'April',
                  'May',
                  'June',
                  'July',
                  'August',
                  'September',
                  'October',
                  'November',
                  'December']

month_abbrs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbrs.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        digit_day = int(day)
        if digit_day < 32 and digit_day > 0:
            return digit_day

def valid_year(year):
    if year and year.isdigit():
        digit_year = int(year)
        if digit_year > 1900 and digit_year <= 2020:
            return digit_year

def escape_html(s):
    for (i, o) in (('"', '&quot;'),
                       ('&', '&amp;'),
                       ('>', '&gt;'),
                       ('<', '&lt;')):
        s = s.replace(i, o)
    return s

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label> Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label> Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red;">%(error)s</div>

    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                                             "month": escape_html(month),
                                                             "day": escape_html(day),
                                                             "year": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        if month and day and year:
            self.redirect("/thanks")
        else:
            self.write_form("That dosen't look valid to me, friend.",
                                      user_month, user_day, user_year)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid date!")

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)],
                              debug=True)

