import streamlit as st
import nltk
import spacy
nltk.download('stopwords')
spacy.load('en_core_web_sm')

import pandas as pd
import pandas as pd
import base64,random
import time,dateime
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import  PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io random
from streamlit_tags import st_tags
from PIL import  Image
import pymysql
from Courses import ds_course,webcourse,android_course,ios_course,uiux_course, resume_videos, interview_videos
import pafy
import plotly.express as px
import youtube_dl


