import web
from index_page import index_page
from latest import latest
from static import static

urls = (
    '/', 'index_page',
    '/latest', 'latest',
    '/css/(.+)', 'static'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
