

@main.route('/')
def index():
    '''
    Home page function returns news sources
    '''

    news_sources = get_sources()


    title = "Welcome to news-app"
    return render_template('index.html',title = title, sources = news_sources)
