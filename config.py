import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=fc005049647046a5a0538fead2b71a42'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources=bbc-news&apiKey=fc005049647046a5a0538fead2b71a42'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
