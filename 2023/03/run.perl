#!/usr/bin/perl
use strict;

my @schema;

while (<>) {
    chomp;
    # my @line = split;
    # print(@line);
    # print("\n");
    push @schema, [ split // ];
}
for my $i (0..$#schema) {
    print(join("", @{$schema[$i]}));
    for (my $j = 0; $j < $#{$schema[$i]}; ++$j) {
	# print($schema[$i][$j]);
	my $last = $j;
	while ($schema[$i][$last] =~ /[0-9]/) {
	    ++$last;
	}
	if ($j != $last) {
	    my $n = join("", @{$schema[$i]}[$j..($last-1)]);
	    print("\t\$j=$j \$last=$last \$n=$n");
	    my $ia = $i == 0 ? $i : $i-1;
	    my $iz = $i == $#schema ? $i : $i+1;
	    my $ja = $j == 0 ? $j : $j-1;
	    my $jz = $last == $#{$schema[$i]} ? $last : $last;
	    print(" \$ia=$ia \$iz=$iz \$ja=$ja \$jz=$jz");
	    $j = $last;
	}
    }
    print("\n");
}
