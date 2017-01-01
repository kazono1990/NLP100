#!/usr/bin/perl

use strict;
use warnings;
use lib "..";
use LIB;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

my $N = 2;
my @str1 = split //, "paraparaparadise";
my @str2 = split //, "paragraph";
my @x = &LIB::getCharNgram(2, \@str1);
my @y = &LIB::getCharNgram(2, \@str2);

# XとYの和集合・積集合・差集合
my @union_set = &LIB::getUnion(\@x, \@y);
my @intersect_set = &LIB::getIntersectSet(\@x, \@y);
my @difference_set = &LIB::getDifferenceSet(\@x, \@y);

# 出力
print "Union_set : " . join(" ", sort @union_set) . "\n";
print "Product_set : " . join(" ", sort @intersect_set) . "\n";
print "Difference_set : " . join(" ", sort @difference_set) . "\n";
grep {"se" eq $_} @x ? print "\"se\" is in x\n" : print "\"se\" is not in x\n";
grep {"se" eq $_} @y ? print "\"se\" is in y\n" : print "\"se\" is not in y\n";
