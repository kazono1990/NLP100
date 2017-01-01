#!/usr/bin/perl

use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

# 入力
my $str = "Hello, world!";

# cipher の呼び出し
print "暗号化 : " . &cipher($str) . "\n";
print "復号化 : " . &cipher(&cipher($str)) . "\n";

# 暗号化関数cipher
sub cipher {
	my @str = split //, shift;

	my $cipher = '';
	foreach my $char (@str) {
		$cipher .= $char =~ /[a-z]/ ? chr(219 - ord($char)) : $char;
	}
	return $cipher;
}
