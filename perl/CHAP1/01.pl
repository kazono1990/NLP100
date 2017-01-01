#!/usr/bin/perl

use strict;
use warnings;
use utf8;
binmode STDOUT, ':encoding(UTF-8)';

my $str = 'パタトクカシーー';
my @str = split('', $str);
my @odd = grep {$_ = $str[$_] if $_ % 2 == 0} (0..$#str);
print join('', @odd)."\n";
