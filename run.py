from webapp import app
from environs import Env




if __name__ == '__main__':
    env = Env()
    env.read_env('.envs')
    app.config['SECRET'] = env.str('SECRET')
    UPLOAD_FOLDER = f'./files'
    app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
    app.config['MAX_CONTENT_PATH']= 16 * 1024 * 1024
    app.run(debug=True)