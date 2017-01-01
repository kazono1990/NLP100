#!/usr/bin/perl

use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

# 1文字毎にリスト化
my @str1 = split //, "パトカー";
my @str2 = split //, "タクシー";

# 1文字ずつ連結
my $join = '';
$join .= $str1[$_] . $str2[$_] for (0..$#str1);
print $join . "\n";
