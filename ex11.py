#!/usr/bin/python
# -*- coding: utf-8 -*-
print 'How old are you?',
age = int(raw_input())
print 'How tall are you?',
height = raw_input()
print 'How much do you weigh?',
weight = raw_input()

print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)

print 'How old is your sister?',
sis_age = int(raw_input())

# print "And you?"
# you_age = int(raw_input())

comb_age = age + sis_age
print 'So your combined age is %r.' % comb_age
