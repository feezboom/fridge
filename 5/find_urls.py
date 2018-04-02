# -*- encoding: utf-8 -*-

import re

def find_urls(haystack):
	needle = '(https?//)?((\\w+)(\.)(\\w+/))*((\\w+)(\.)(\\w+)){0,1}'
	pattern = re.compile(needle)
	return pattern.findall(haystack)

	
