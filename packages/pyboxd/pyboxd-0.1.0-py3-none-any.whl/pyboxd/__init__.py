"""Top-level package for Pyboxd."""

__author__ = """Juan Antonio Fernandez Cruz"""
__email__ = 'fercruzjuan2002@gmail.com'
__version__ = '0.1.0'

from .film import Film  
from .lists import UserList  
from .user import User  

__all__ = ['Film', 'UserList', 'User']
