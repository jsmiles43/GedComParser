#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:40:56 2017

@author: josephmiles
"""

import os


class GedComParser:
    
    def __init__(self, fileName, validTags):
        '''stores the file as well as the content in an array of lines, also stores the tags that are considired valid'''
        self.file = open(fileName, 'r', encoding = 'utf-8')
        self.lines = self.file.read().splitlines()
        if not validTags:
            raise TypeError("You must enter at least one valid tag")
        self.validTags = validTags
    
    def parseLine(self, line):
        '''This method parses the line  and checks the validity of the tag'''
        if line == '':
            raise ValueError("Your file contains empty strings")
        
        symbols = {}
        symbols['level'] =  line.split(' ', 1)[0]

        uncheckedSymbol1 = line.split(' ', 2)[1]
        if self.checkTag(uncheckedSymbol1):
            symbols['tag'] = uncheckedSymbol1
        if line.count(' ') > 1:
            uncheckedSymbol2 = line.split(' ', 2)[2]
            if self.checkTag(uncheckedSymbol2):
                symbols['tag'] = uncheckedSymbol2
        if 'tag' not in symbols:
            symbols['tag'] = 'Invalid Tag'
        
        return symbols

    def checkTag(self, tag):
        '''checks for an appropriate tag in a record'''
        return tag in self.validTags
        
        
        
    

tags = ['INDI','NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 
'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

parser = GedComParser(os.getcwd() + '/GedComData.txt', tags)


for record in parser.lines:
    symbols = parser.parseLine(record)
    print(record + '\n')
    print(symbols['level'] + '\n')
    print(symbols['tag'] + '\n\n')

