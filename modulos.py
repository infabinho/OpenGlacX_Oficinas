from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from tkinter.filedialog import *

from datetime import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from math import *
import sys
import webbrowser
import shutil
import pycep_correios
from pycep_correios.excecoes import ExcecaoPyCEPCorreios
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import sqlite3
import base64
#import PIL # importa o PIL
#from PIL import Image, ImageTk, ImageSequence
from babel import numbers

from tkcalendar import Calendar, DateEntry



