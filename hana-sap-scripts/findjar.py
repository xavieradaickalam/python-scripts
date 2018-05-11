#!/usr/bin/python

import sys, os, os.path
import fnmatch

def findFileGenerator(rootDirectory, acceptanceFunction):
  for aCurrentDirectoryItem in [ os.path.join(rootDirectory, x) for x in os.listdir(rootDirectory) ]:
    if acceptanceFunction(aCurrentDirectoryItem):
      yield aCurrentDirectoryItem
    if os.path.isdir(aCurrentDirectoryItem):
      for aSubdirectoryItem in findFileGenerator(aCurrentDirectoryItem, acceptanceFunction):
        yield aSubdirectoryItem

if __name__ == "__main__":
  rootOfSearch = '.'
  if sys.argv[1:]:
    rootOfSearch = sys.argv[1]
  if sys.argv[2:]:
    classnameFragment = sys.argv[2].replace('.', '/')
    def anAcceptanceFunction (itemToTest):
      return not os.path.isdir(itemToTest) and fnmatch.fnmatch(itemToTest, '*.jar') and classnameFragment in os.popen('jar -tf %s' % itemToTest).read()
  else:
    def anAcceptanceFunction (itemToTest):
      return not os.path.isdir(itemToTest) and fnmatch.fnmatch(itemToTest, '*.jar')

  try:
    for x in findFileGenerator(rootOfSearch, anAcceptanceFunction):
      print x
  except Exception, anException:
    print anException
