#!/usr/bin/perl

use strict;
use warnings;

# . を削除し, スペース毎に分割して各単語毎にリスト化
my $str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
$str =~ s/\.//g;
my @word = split(" ", $str);

my %hash = ();
my @num = qw/1 5 6 7 8 9 15 16 19/;
for(my $i = 0; $i < $#word + 1; $i++) {
	my @char = split //, $word[$i];
	if(grep {$_ == $i + 1} @num) {
		$hash{$char[0]} = $i + 1; # 先頭の1文字を key に
	} else {
		$hash{$char[0] . $char[1]} = $i + 1; # 先頭の2文字を key に
	}
}

# 元素番号順 (単語の位置の昇順) に出力
foreach my $key (sort {$hash{$a} <=> $hash{$b}} keys %hash) {
	print "$hash{$key} : $key\n";
}
