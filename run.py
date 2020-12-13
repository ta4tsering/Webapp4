from webapp import app
from environs import Env




if __name__ == '__main__':
    env = Env()
    env.read_env('.envs')
    app.config['SECRET'] = env.str('SECRET')
    app.run(debug=True)