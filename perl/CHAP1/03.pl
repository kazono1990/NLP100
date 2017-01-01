#!/usr/bin/perl

use strict;
use warnings;

my $str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
# 前処理 (, と. を削除)
$str =~ s/\,|\.//g;

# スペースで分割してそれぞれの文字数 (長さ) のリストを作成
my @list = ();
push(@list, length $_) foreach split(' ', $str);
print shift(@list) . '.' . join('', @list) . "\n";
