import dill

def save_session_pkl(name):
    dill.dump_session(name+'.pkl')

def load_session_pkl(name):
    dill.load_session(name +'.pkl')

def save_session_db(name):
    dill.dump_session(name+'.db')

def load_session_db(name):
    dill.load_session(name +'.db')