import os

# MONGODB

mongodb = {
    'host': os.getenv('MONGOHOST', '127.0.0.1'),
    'port': int(os.getenv('MONGOHOST', '27017'))
}

# DAREDEVIL

daredevil = {
    'host': '0.0.0.0',
    'port': 8000,
    'debug': os.getenv('DAREDEVIL_DEBUG', 'False') == 'True'
}
