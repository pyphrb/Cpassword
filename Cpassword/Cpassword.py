#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pinyin.pinyin import PinYin
import logging
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
logging.basicConfig(level=logging.DEBUG,\
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', \
    datefmt='%Y-%m-%d %H:%M:%S', filename='log/info.log', filemode='w')
class Cpassword():
    
    def __init__(self, pinyinusername):
        self.pinyinusername = pinyinusername
        self.yinwen = None
        self.pinyin = PinYin()
        self.pinyin.load_word()
        self.num = 0
        self.strname = ''
        self.struser = ''
        self.listDict = []
        self.threadlist = []
        self.strnameDict = []
    def run(self):
        self.returnUser = self.readYz()
        print self.returnUser
        if self.returnUser is not False:
            for self.userxing in self.pinyin.hanzi2pinyin(self.returnUser):
                self.strname = self.strname + self.userxing
                self.strnameDict.append(self.strname)
            self.strname = ''
            for self.userxing in self.pinyin.hanzi2pinyin(self.returnUser):
                self.strname = self.strname + self.userxing[0]
                self.strnameDict.append(self.strname)

            for self.userxing in self.pinyin.hanzi2pinyin(self.returnUser):
                #self.strname = self.strname + self.userxing
                self.strnameDict.append(self.userxing)
            self.usernameList = list(set(self.strnameDict))
            self.createDict(self.usernameList)

    def createDict(self, userstr):
        self.userstr = userstr
        print self.userstr
        self.strlist = self.userstr
        self.writeFile = open('output/userdict.txt', 'a')
        with open('libload/dict.txt') as self.openDict:
            for self.line in self.openDict:
                self.writeFile.write(self.line)
                self.listDict.append(self.line)
        for self.userDict in self.strlist:
            for self.i in self.listDict:
                self.writeFile.write(self.userDict + self.i.strip() + '\n')
        self.writeFile.close()

    def readYz(self):
        with open('libload/payload.txt') as self.cpassDict:
            for self.line in self.cpassDict.readlines():
                if self.pinyinusername == self.line.split('-')[0]:
                    self.num = self.num + 1
                    return self.line.split('-')[1].strip()
        if self.num == 0:
            print self.pinyinusername + '   not found in libload/payload.txt'
            logging.info(self.pinyinusername + '  not found chinese name please enter lib/payload.txt' + '\n')
            return False
if __name__ == '__main__':
    print '[*]---------------------------------------------------------------------------------------[*]'
    print '[*]------------------we are hacker--We are security---------------------------------------[*]'
    print '[*]-------------user dict create success you can see in output/userdict.txt---------------[*]'
    print '[*]------------------------------------pyphrb---------------------------------------------[*]'
    print '[*]---------------------------------qq:959297822------------------------------------------[*]'
    print '[*]if you have no find something aboutnot found chinese name please enter lib/payload.txt [*]'
    print '[*]else you have no find something please enter name in libload/payload.txt that meaning right[*]'
    print '[*]---------------------------------------------------------------------------------------[*]'
    if os._exists('output/userdict.txt'):
        os.remove('output/userdict.txt')
    with open('input/username.txt') as username:
        for line in username:
            cpass = Cpassword(line.strip())
            cpass.run()

