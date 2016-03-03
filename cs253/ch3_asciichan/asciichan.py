import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                                  autoescape = True)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

class MainPage(BaseHandler):
    def render_base(self, title="", art="", error=""):
        arts =db.GqlQuery("select * from Art order by created desc")

        self.render("base.html", title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_base()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title=title, art=art)
            a.put()

            self.redirect("/")
        else:
            error="need both title and art!"
            self.render_base(title, art, error)


app = webapp2.WSGIApplication([('/', MainPage)],
                                                      debug=True)
