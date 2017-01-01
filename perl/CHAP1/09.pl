#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw/shuffle/;

# 入力 (単語毎 にリスト化)
my $input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
my @str = split / /, $input;

# 並び替え処理
my $typoglycemia = '';
foreach my $word (@str) {
	# 文字数が4以下はそのまま
	if(length $word <= 4) {
		$typoglycemia .= $word . " ";
	}
	# それ以外は先頭と末尾以外を並び替える
	else {
		my @char = split //, $word;
		my $first = shift @char; # 先頭
		my $last = pop @char;    # 末尾
		$typoglycemia .= $first . join('', shuffle(@char)) . $last . " ";
	}
}

# 出力
print $typoglycemia;
