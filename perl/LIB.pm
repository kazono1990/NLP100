package LIB;

use strict;
use warnings;
use utf8;

# *******************************************************************
# 単語 N グラムを返す
#
# $param  N, List
# $return 単語N-gram
# *******************************************************************

sub getWordNgram {
	my ($n, $array) = @_;
	my @ngram = ();
	for(my $i = 0; $i < $#{$array} + 2 - $n; $i++) {
		my $hoge = '';
		$hoge .= $array->[$i + $_] for (0..$n-1);
		push(@ngram, $hoge);
	}
	return @ngram;
}

# *******************************************************************
# 文字 N グラムを返す
#
# $param  N, List
# $return 文字N-gram
# *******************************************************************

sub getCharNgram {
	my ($n, $array) = @_;
	my @ngram = ();
	my @char = split('', join('', @{$array}));
	for(my $i = 0; $i < $#char + 2 - $n; $i++) {
		my $hoge = '';
		$hoge .= $char[$i + $_] for (0..$n-1);
		push(@ngram, $hoge);
	}
	return @ngram;
}

# *******************************************************************
# 2つの配列の和集合 (X∪Y) を返す
#
# $param  配列 X, 配列 Y
# $return 和集合 (X∪Y)
# *******************************************************************
sub getUnion {
	my ($array1, $array2) = @_;
	my %cnt = ();
	return grep { ++$cnt{$_} == 1} (@{$array1}, @{$array2});
}

# *******************************************************************
# 2つの配列の積集合 (X∩Y) を返す
#
# $param  配列 X, 配列 Y
# $return 積集合 (X∩Y)
# *******************************************************************
sub getIntersectSet {
	my ($array1, $array2) = @_;
	my %cnt = ();
	return grep {++$cnt{$_} == 2} (@{$array1}, @{$array2});
}

# *******************************************************************
# 2つの配列の差集合 (X-Y) を返す
#
# $param  配列 X, 配列 Y
# $return 積集合 (X∩Y)
# *******************************************************************
sub getDifferenceSet {
	my ($array1, $array2) = @_;
	return grep { my $t=$_; ! grep /^$t$/, @{$array2}; } @{$array1};
}

# おまじない
1;
