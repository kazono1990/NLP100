#!/usr/bin/perl

use strict;
use warnings;

# str を分割し、先頭の要素から順に unshift 関数を適用
my $str = "stressed";
my @reverse = ();
unshift(@reverse, $_) foreach split('', $str);
print "reverse : " . join("", @reverse) . "\n";
