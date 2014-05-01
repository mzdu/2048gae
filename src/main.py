import webapp2
import jinja2
import os
import logging


jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))


def doRender(handler, tname = 'index.html', values = {}):

    temp = jinja_environment.get_template(tname)
    handler.response.out.write(temp.render(values))
    return True

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        values = dict()
        values['css'] = ['/static/css/main.css']
        values['javascript'] = ['/static/js/bind_polyfill.js',
                                '/static/js/classlist_polyfill.js',
                                '/static/js/animframe_polyfill.js',
                                '/static/js/keyboard_input_manager.js',
                                '/static/js/html_actuator.js',
                                '/static/js/grid.js',
                                '/static/js/tile.js',
                                '/static/js/local_storage_manager.js',
                                '/static/js/game_manager.js',
                                '/static/js/application.js',
                                ]
        
        doRender(self, 'index.html', values)
        
app = webapp2.WSGIApplication([('/.*', MainPageHandler)],debug = True)
    

