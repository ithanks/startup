#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


#from __future__ import division, unicode_literals

from datetime import date, datetime, timedelta
from collections import Counter, defaultdict, namedtuple
import os
import pickle
import re
import site
import sys

import numpy as np
import pandas as pd
from pandas.io.packers import pack, unpack  # pickle이 느릴 때
import scipy as sp

from konlpy.tag import Twitter
from konlpy.utils import pprint
