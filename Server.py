import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = "/sql/client_information.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
