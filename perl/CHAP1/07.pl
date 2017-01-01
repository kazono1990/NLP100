#!/usr/bin/perl

use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

my ($x, $y, $z) = qw/12 気温 22.4/;
print &template($x, $y, $z);

sub template {
	my ($x, $y, $z) = @_;
	return $x . "時の" . $y . "は" . $z;
}
