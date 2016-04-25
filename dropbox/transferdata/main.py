#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transferdata import TransferData

def main():
	access_token = '****'	# get your access token from Dropbox Developers
	transferData = TransferData(access_token)

	file_from = 'test.txt'
	file_to = '/test_dropbox/test.txt'	# The full path to upload the file to, including the file name

	# API v1
	transferData.upload_file_v1(file_from=file_from, file_to=file_to)

	# API v2
	transferData.upload_file(file_from=file_from, file_to=file_to)

if __name__ == '__main__':
	main()