#!/usr/bin/perl

use strict;
use warnings;
use lib "..";
use LIB;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

my $str = "I am an NLPer";
my @word = split(" ", $str);

my $N = 2;
my @ngram_word = &LIB::getWordNgram($N, \@word);
my @ngram_char = &LIB::getCharNgram($N, \@word);
print "単語$N-グラム : " . join(" ", @ngram_word) . "\n";
print "文字$N-グラム : " . join(" ", @ngram_char) . "\n";
