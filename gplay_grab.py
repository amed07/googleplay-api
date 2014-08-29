#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import shutil

import os
from os import listdir
from os.path import isfile, join


import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt

# Connect
api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)


def get_apk(packagename, friendly_name):

	# Get the version code and the offer type from the app details
	m = api.details(packagename)
	doc = m.docV2
	vc = doc.details.appDetails.versionCode
	ot = doc.offer[0].offerType

	easy_name = friendly_name + "-" + str(vc)
	filename = easy_name +".apk"

	# logic to check if we have this version here
	if do_we_already_have(friendly_name, easy_name):
		print "We already have " + easy_name + " skipping download"
	else:
		print "Downloading " + easy_name + " from the Google Play Store."
		# Download
		print "Downloading %s..." % sizeof_fmt(doc.details.appDetails.installationSize),
		data = api.download(packagename, vc, ot)
		open(filename, "wb").write(data)
		print "Done"
		#shutil.move(filename, '../analyzed_apks2/'+friendly_name+'/')



def do_we_already_have(appname, appversionname):
	answer = False
	if not os.path.exists('analyzed_apks2/'+appname+'/'):
		os.makedirs('analyzed_apks2/'+appname+'/')
		return answer
	dirs = [os.listdir('analyzed_apks2/'+appname+'/')]
	for file in dirs:
		if str(file).find(appversionname) > 0:
			answer = True
	return answer


get_apk("com.tencent.mm", "wechat")
get_apk("jp.naver.line.android", "line")
get_apk("com.kakao.talk", "kakao")
get_apk("com.didirelease.view", "didi")
get_apk("com.viber.voip", "viber")
get_apk("com.whatsapp", "whatsapp")
get_apk("com.opengarden.firechat", "firechat")
get_apk("com.rebelvox.voxer", "voxer")
get_apk("com.xiaomi.channel", "mitalk")
get_apk("im.yixin", "yixin")
get_apk("com.facebook.orca", "facebook")
get_apk("com.instagram.android", "instagram")
